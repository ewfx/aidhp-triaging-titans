from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://rajeshthatha:N3bZbLn8sebU52kZ@cluster0.6de1t.mongodb.net/")  # Update with your MongoDB URI
db = client["Hackathon_2025"]  # Replace with your database name
collection = db["transaction_history_trained_data"]  # Replace with your collection name

@app.route('/customer/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = collection.find_one({"Customer_Id": customer_id})
    
    # if customer:
    #     customer['_id'] = str(customer['_id'])  # Convert ObjectId to string
    #     return jsonify(customer)
    # else:
    #     return jsonify({"error": "Customer not found"}), 404

    if customer and "suggestion" in customer:
        return jsonify({"suggestion": customer["suggestion"]})
    else:
        return jsonify({"error": "Suggestion not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)