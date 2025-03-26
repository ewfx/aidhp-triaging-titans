import pandas as pd
import openai
import random
import string
import pymongo
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="transaction_suggestions.log",  # Log file name
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Log the start of the script
start_time = datetime.now()
logging.info("Script started.")

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

# Load the transaction data
input_file = 'Data/transaction_data.csv'

# MongoDB connection
client = pymongo.MongoClient("mongodb+srv://rajeshthatha:N3bZbLn8sebU52kZ@cluster0.6de1t.mongodb.net/")
db = client["Hackathon_2025"]  # Replace with your database name
cash_transactions_collection = db["transaction_history_trained_data"]  # Replace with your collection name

try:
    data = pd.read_csv(input_file)
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    exit()

# Check if the data was read correctly
if data.empty:
    print("The input file is empty or not read correctly.")
    exit()

# Define a function to generate suggestions using GPT-3.5-turbo
def generate_suggestion(payment_mode, category):
    prompt = f"""
    Provide a suggestion for a customer making a payment using '{payment_mode}' in the category '{category}'.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant providing suggestions for customers."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,
            temperature=0.7
        )
        suggestion = response['choices'][0]['message']['content'].strip()
        return suggestion
    except Exception as e:
        print(f"Error generating suggestion for Payment_Mode '{payment_mode}' and Category '{category}': {e}")
        return "No suggestion available."

# Apply the GPT-based suggestion generation function to the data
data['suggestion'] = data.apply(
    lambda row: generate_suggestion(row['Payment_Mode'], row['Category']), axis=1
)


# Generate a random string of fixed length (e.g., 8 characters)
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
print(f"Random String: {random_string}")

# Save the suggestions to a new CSV file
output_file = 'Data/transaction_suggestions_'+random_string+'.csv'

try:
    data.to_csv(output_file, index=False)
    print(f"Suggestions saved to '{output_file}'")
except Exception as e:
    print(f"Error saving the suggestions: {e}")


try:
    data = pd.read_csv(output_file)
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    exit()

# Convert the DataFrame to a list of dictionaries
data_dict = data.to_dict("records")

# Insert the data into the MongoDB collection
try:
    cash_transactions_collection.insert_many(data_dict)
    print(f"Data successfully saved to the MongoDB collection '{cash_transactions_collection.name}'.")
except Exception as e:
    print(f"Error saving the data to MongoDB: {e}")

# Log the end of the script
end_time = datetime.now()
logging.info(f"Script ended. Total execution time: {end_time - start_time}")