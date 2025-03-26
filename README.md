# Flask Service for Customer Suggestions

## Overview
This is a Flask-based API service that retrieves customer suggestions from a MongoDB database. The service provides an endpoint to fetch suggestions for a specific customer based on their `Customer_Id`.

## Features
- Connects to a MongoDB database
- Retrieves customer suggestions based on `Customer_Id`
- Returns data in JSON format

## Prerequisites
Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- pymongo

or run below requirements file
pip install -r requirements.txt

## Installation
1. Clone the repository or copy the `service.py` file to your working directory.
2. Install the required dependencies using:
   ```sh
   pip install flask pymongo
   ```

## Configuration
Update the MongoDB connection URI in `service.py`:
```python
client = MongoClient("mongodb+srv://<username>:<password>@<cluster>.mongodb.net/")
```
Replace `<username>`, `<password>`, and `<cluster>` with your MongoDB credentials.

## Mongo DB collections are :- 
 transaction_history_trained_data
 customer_sentimentscore_trained_data
 customer_preferences_trained_data
 customer_financial_trained_data

## Running the Service
To start the Flask application, run:
```sh
python service.py
```
The service will start in debug mode and be accessible at `http://127.0.0.1:5000/`.

## API Endpoint
### Get Customer Suggestion
**Endpoint:**
```
GET /customer/<customer_id>
```

**Description:** Retrieves the suggestion for a given `customer_id`.

**Response:**
- If a suggestion is found:
  ```json
  {
    "suggestion": "<suggested_value>"
  }
  ```
- If no suggestion is found:
  ```json
  {
    "error": "Suggestion not found"
  }
  ```

## Notes
- Ensure that your MongoDB collection contains documents with a `Customer_Id` field.
- The `_id` field is not included in the response.
- Modify database and collection names as needed.

## License
This project is for demonstration purposes. Modify as needed.

## Optional to run these scripts
Note:- This step is optional because we ran these scripts, internally scripts has integrated GPT-3.5-turbo model, model has trained the dataset and persisted in mongo db collection.
python generate_transaction_suggestions.py
python generate_suggestions_by_sentimentScore.py
python customer_financial_suggestions.py
python customer_preferences.py
