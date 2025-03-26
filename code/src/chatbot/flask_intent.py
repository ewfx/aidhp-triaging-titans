from flask import Flask, request, jsonify
import nltk
from nltk.tokenize import word_tokenize
import json

# Download NLTK data files (only need to run once)
nltk.download('punkt')

# Load product data from JSON file
with open('./chatbot/products_intent.json', 'r') as f:
    products = json.load(f)

app = Flask(__name__)

context = {}

def get_response(tag, user_id):
    for intent in products['intents']:
        if intent['tag'] == tag:
            if intent['context'][0]:
                context[user_id] = intent['context'][0]
            return intent['responses']
    return ["Sorry, I don't understand that."]

def classify_text(text):
    tokens = word_tokenize(text.lower())
    for intent in products['intents']:
        for pattern in intent['patterns']:
            pattern_tokens = word_tokenize(pattern.lower())
            if all(token in tokens for token in pattern_tokens):
                return intent['tag']
    return "noanswer"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_id = data.get('user_id', 'default')
    text = data.get('text', '')
    
    if user_id in context:
        tag = context[user_id]
        del context[user_id]
    else:
        tag = classify_text(text)
    
    responses = get_response(tag, user_id)
    return jsonify({'tag': tag, 'responses': responses})

if __name__ == '__main__':
    app.run(debug=True)