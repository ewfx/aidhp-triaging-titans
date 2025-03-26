# Customer Suggestions Chatbot and Service API

This project provides a Flask-based API and a chatbot system for retrieving and serving customer suggestions stored in a MongoDB database.

#### Features:
- Connects to a MongoDB database using the `pymongo` library.
- Provides an API endpoint to retrieve customer suggestions based on a `customer_id`.

#### API Endpoint:
- **GET `/customer/<customer_id>`**
  - Retrieves the suggestion for a specific customer.
  - **Response:**
    - If a suggestion exists:
      ```json
      {
        "suggestion": "<suggestion_text>"
      }
      ```
    - If no suggestion is found:
      ```json
      {
        "error": "Suggestion not found"
      }
      ```
How to run

1.create a virtual environment:
Create a virtual environment to isolate dependencies:

python -m venv venv

Activate the virtual environment:
On Windows: venv\Scripts\activate

2. Install Dependencies:

Install the required libraries using the requirements.txt file:
pip install -r requirements.txt

3. launch the chatbot through service.py
   location is chatbot/service.py
   This file implements a Flask API to fetch customer suggestions from a MongoDB database.
   

4. Run the scripts one by one:( this step is optional, we ran these and trained the 
   Note:- This step is optional because we ran these scripts, internally scripts has integrated GPT-3.5-turbo model, model has trained the dataset and persisted in mongo db collection.
python generate_transaction_suggestions.py
python generate_suggestions_by_sentimentScore.py
python customer_financial_suggestions.py
python customer_preferences.py

5.Verify MongoDB Connection:

Ensure your MongoDB instance is running and accessible. Update the connection string in the scripts if necessary.
 mongo db connection string: mongodb+srv://rajeshthatha:N3bZbLn8sebU52kZ@cluster0.6de1t.mongodb.net/
 
 collections are :-
 transaction_history_trained_data
 customer_sentimentscore_trained_data
 customer_preferences_trained_data
 customer_financial_trained_data

6.Logs for each script will be saved in their respective log files 

  financial_suggestions.log, interests_preferences_suggestions.log, test_data_processing.log, transaction_suggestions.log

