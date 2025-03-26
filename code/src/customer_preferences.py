import pandas as pd
import openai
import random
import string
import logging
from datetime import datetime
import pymongo

# Configure logging
logging.basicConfig(
    filename="interests_preferences_suggestions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Log the start of the script
start_time = datetime.now()
logging.info("Script started.")

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

# MongoDB connection
client = pymongo.MongoClient("mongodb+srv://rajeshthatha:N3bZbLn8sebU52kZ@cluster0.6de1t.mongodb.net/")
db = client["Hackathon_2025"]  # Replace with your database name
collection = db["customer_preferences_trained_data"]  # Replace with your collection name

# Load the Excel file
input_file = 'Data/customer-data.xlsx'
try:
    data = pd.read_excel(input_file, engine='openpyxl')
    logging.info(f"Successfully loaded data from '{input_file}'.")
except Exception as e:
    logging.error(f"Error reading the Excel file: {e}")
    exit()

# Check if the required columns exist
required_columns = ['Interests', 'Preferences']
if not all(column in data.columns for column in required_columns):
    logging.error(f"One or more required columns are missing: {required_columns}")
    exit()

# Define a function to generate suggestions using GPT-3.5-turbo
def generate_suggestion(interests, preferences):
    prompt = f"""
    Based on the following details:
    - Interests: {interests}
    - Preferences: {preferences}

    Provide a helpful suggestion tailored to the interests and preferences.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant providing suggestions based on interests and preferences."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.7
        )
        suggestion = response['choices'][0]['message']['content'].strip()
        return suggestion
    except Exception as e:
        logging.error(f"Error generating suggestion for Interests '{interests}' and Preferences '{preferences}': {e}")
        return "No suggestion available."

# Apply the GPT-based suggestion generation function to the data
logging.info("Generating suggestions using GPT-3.5-turbo.")
data['Suggestion'] = data.apply(
    lambda row: generate_suggestion(row['Interests'], row['Preferences']), axis=1
)

# Generate a random string for the output file name
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
logging.info(f"Generated random string: {random_string}")

# Save the suggestions to a new Excel file
output_file = f'Data/Test-Data-Suggestions-{random_string}.xlsx'
try:
    data.to_excel(output_file, index=False, engine='openpyxl')
    logging.info(f"Suggestions saved to '{output_file}'.")
except Exception as e:
    logging.error(f"Error saving the suggestions: {e}")

try:
    data = pd.read_excel(output_file)
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    exit()

# Convert the DataFrame to a list of dictionaries
data_dict = data.to_dict("records")

# Insert the data into the MongoDB collection
try:
    collection.insert_many(data_dict)
    print(f"Data successfully saved to the MongoDB collection '{collection.name}'.")
except Exception as e:
    print(f"Error saving the data to MongoDB: {e}")

# Log the end of the script
end_time = datetime.now()
logging.info(f"Script ended. Total execution time: {end_time - start_time}")