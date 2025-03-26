import pymongo

# MongoDB connection
client = pymongo.MongoClient("mongodb+srv://rajeshthatha:N3bZbLn8sebU52kZ@cluster0.6de1t.mongodb.net/")
db = client["Hackathon_2025"]  # Replace with your database name

# List of collections to query
collections = ["customer_financial_trained_data", "customer_preferences_trained_data", "customer_sentimentscore_trained_data", "transaction_history_trained_data"]  # Replace with your collection names

# Define the Customer_Id to fetch
customer_id = "C100001"  # Replace with the desired Customer_Id

# Initialize a dictionary to store results
results = {}

# Query each collection
try:
    for collection_name in collections:
        collection = db[collection_name]
        # Fetch data for the given Customer_Id
        data = list(collection.find({"Customer_Id": customer_id}, {"_id": 0}))  # Exclude the _id field
        results[collection_name] = data  # Store the results in the dictionary

    # Print the combined results
    for collection_name, data in results.items():
        print(f"Data from collection '{collection_name}':")
        if data:
            for record in data:
                print(record)
        else:
            print(f"No data found for Customer_Id: {customer_id} in collection '{collection_name}'")

except Exception as e:
    print(f"Error fetching data from MongoDB: {e}")