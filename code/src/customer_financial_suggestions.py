import pandas as pd
import openai
import random
import string
import logging
from datetime import datetime
import pymongo  

# Configure logging
logging.basicConfig(
    filename="financial_suggestions.log",
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
collection = db["customer_financial_trained_data"]  # Replace with your collection name

# Load the Excel file
input_file = 'Data/Test-Data-Updated.xlsx'
try:
    data = pd.read_excel(input_file, engine='openpyxl')
    logging.info(f"Successfully loaded data from '{input_file}'.")
except Exception as e:
    logging.error(f"Error reading the Excel file: {e}")
    exit()

# Check if the required columns exist
required_columns = ['Account_type', 'Income per year (in dollars)', 'Credit Score', 'Occupation']
if not all(column in data.columns for column in required_columns):
    logging.error(f"One or more required columns are missing: {required_columns}")
    exit()

# Define a function to generate financial suggestions using GPT-3.5-turbo
def generate_financial_suggestion(account_type, income, credit_score, occupation):
    prompt = f"""
    Based on the following financial details:
    - Account Type: {account_type}
    - Income per Year: ${income}
    - Credit Score: {credit_score}
    - Occupation: {occupation}

    Provide a personalized financial suggestion tailored to the individual's financial profile.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a financial advisor providing personalized financial suggestions based on account type, income, credit score, and occupation."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        suggestion = response['choices'][0]['message']['content'].strip()
        return suggestion
    except Exception as e:
        logging.error(f"Error generating suggestion for Account Type '{account_type}', Income '{income}', Credit Score '{credit_score}', and Occupation '{occupation}': {e}")
        return "No suggestion available."

# Apply the GPT-based suggestion generation function to the data
logging.info("Generating financial suggestions using GPT-3.5-turbo.")
data['Financial_Suggestion'] = data.apply(
    lambda row: generate_financial_suggestion(
        row['Account_type'], 
        row['Income per year (in dollars)'], 
        row['Credit Score'], 
        row['Occupation']
    ), axis=1
)

# Generate a random string for the output file name
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
logging.info(f"Generated random string: {random_string}")

# Save the suggestions to a new Excel file
output_file = f'Data/Financial-Suggestions-{random_string}.xlsx'
try:
    data.to_excel(output_file, index=False, engine='openpyxl')
    logging.info(f"Financial suggestions saved to '{output_file}'.")
except Exception as e:
    logging.error(f"Error saving the financial suggestions: {e}")

# Save the data to MongoDB
try:
    records = data.to_dict(orient='records')
    collection.insert_many(records)
    print(f"Data successfully saved to the MongoDB collection '{collection.name}'.")
    logging.info(f"Data successfully saved to the MongoDB collection '{collection.name}'.") 
except Exception as e:
    logging.error(f"Error saving data to MongoDB: {e}")

# Log the end of the script
end_time = datetime.now()
logging.info(f"Script ended. Total execution time: {end_time - start_time}")