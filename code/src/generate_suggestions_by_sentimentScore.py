import pandas as pd
import openai
import random
import string
import logging
from datetime import datetime
import pymongo

# Configure logging
logging.basicConfig(
    filename="test_data_processing.log",
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
collection = db["customer_sentimentscore_trained_data"]  # Replace with your collection name

# Load the Excel file
input_file = 'Data/Social_Media_Sentiment_data.xlsx'
try:
    data = pd.read_excel(input_file, engine='openpyxl')
    logging.info(f"Successfully loaded data from '{input_file}'.")
except Exception as e:
    logging.error(f"Error reading the Excel file: {e}")
    exit()

# Check if the required columns exist
required_columns = ['Intent', 'Content', 'Sentiment_Score']
if not all(column in data.columns for column in required_columns):
    logging.error(f"One or more required columns are missing: {required_columns}")
    exit()

# Define a function to generate suggestions using GPT-3.5-turbo
def generate_suggestion(intent, content, sentiment_score):
    prompt = f"""
    Based on the following details:
    - Intent: {intent}
    - Content: {content}
    - Sentiment Score: {sentiment_score}

    Provide a helpful suggestion tailored to the intent and sentiment score.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant providing suggestions based on intent, content, and sentiment score."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.7
        )
        suggestion = response['choices'][0]['message']['content'].strip()
        return suggestion
    except Exception as e:
        logging.error(f"Error generating suggestion for Intent '{intent}', Content '{content}', and Sentiment_Score '{sentiment_score}': {e}")
        return "No suggestion available."

# Define a function to predict sentiment type
def predict_sentiment_type(sentiment_score):
    if sentiment_score > 0.5:
        return "Positive"
    elif sentiment_score < -0.5:
        return "Negative"
    else:
        return "Neutral"

# Define a function to calculate churn score based on sentiment score
def calculate_churn_score(sentiment_score):
    churn_score = (1 - sentiment_score) * 50  # Scale to a range of 0 to 100
    return max(0, min(100, churn_score))  # Ensure churn score is within 0 to 100

# Apply the functions to the data
logging.info("Generating suggestions, predicting sentiment type, and calculating churn score.")
data['Suggestion'] = data.apply(
    lambda row: generate_suggestion(row['Intent'], row['Content'], row['Sentiment_Score']), axis=1
)
data['Sentiment_Type'] = data['Sentiment_Score'].apply(predict_sentiment_type)
data['Churn_Score'] = data['Sentiment_Score'].apply(calculate_churn_score)

# Generate a random string for the output file name
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
logging.info(f"Generated random string: {random_string}")

# Save the updated data to a new Excel file
output_file = f'Data/Test-Data-Processed-{random_string}.xlsx'
try:
    data.to_excel(output_file, index=False, engine='openpyxl')
    logging.info(f"Processed data saved to '{output_file}'.")
except Exception as e:
    logging.error(f"Error saving the processed data: {e}")

try:
    data = pd.read_excel(output_file, engine='openpyxl')  # Correctly read the Excel file
    logging.info(f"Successfully reloaded the Excel file '{output_file}'.")
except Exception as e:
    logging.error(f"Error reading the Excel file: {e}")
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