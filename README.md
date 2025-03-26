# 🚀 Project Name

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Running the Application]
- [Features]
- [File Descriptions]
- [Notes]
- [Tech Stack](#tech-stack)
- [Team](#team)


---

## 🎯 Introduction
A brief overview of your project and its purpose. Mention which problem statement are your attempting to solve. Keep it concise and engaging.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
What inspired you to create this project? Describe the problem you're solving.

## ⚙️ What It Does
Explain the key features and functionalities of your project.

## 🛠️ How We Built It
Briefly outline the technologies, frameworks, and tools used in development.

## 🚧 Challenges We Faced
Describe the major technical or non-technical challenges your team encountered.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/aidhp-triaging-titans.git
   ```
2. Install dependencies  
   ```sh
   npm install  # or pip install -r requirements.txt (for Python)
   ```
3. Run the project  
   ```sh
   npm start  # or python app.py
   ```

## 🏃 Running the Application
-----------------------
1. Start the Flask API:
   - Run `flask_intent.py` to start the backend server:
     ```bash
     python flask_intent.py
     ```
   - The server will run on `http://127.0.0.1:5000`.
 
2. Start the Chatbot Interface:
   - Run [chatbot_flask_intent.py](http://_vscodecontentref_/1) to launch the Tkinter-based chatbot interface:
     ```bash
     python chatbot_flask_intent.py
     ```
## 🏃 Features
--------
1. **Flask API (`flask_intent.py`)**:
   - Processes user input and matches it to predefined intents in `products_intent.json`.
   - Returns appropriate responses based on the matched intent.
 
2. **Tkinter Chatbot (`chatbot_flask_intent.py`)**:
   - Provides a graphical interface for user interaction.
   - Displays user and bot messages with icons.
   - Supports scrolling and dynamic responses.
 
3. **Intent Matching**:
   - Uses NLTK for tokenizing user input and matching it to predefined patterns in `products_intent.json`.
 
4. **Image Recommendations**:
   - Displays relevant images (e.g., credit card or savings account options) based on user input.

## 🏃 File Descriptions
-----------------
1. `flask_intent.py`:
   - Backend API for processing user input and returning responses.
   - Uses `products_intent.json` for intent matching.
 
2. [chatbot_flask_intent.py](http://_vscodecontentref_/2):
   - Frontend chatbot application built with Tkinter.
   - Interacts with the Flask API to display responses.
 
3. `products_intent.json`:
   - JSON file containing predefined intents, patterns, responses, and contexts.
 
4. [user_icon.png](http://_vscodecontentref_/3) and [bot_icon.png](http://_vscodecontentref_/4):
   - Icons used in the chatbot interface for user and bot messages.
 
5. `credit_card.png` and `savings.png` (optional):
   - Images displayed in the chatbot interface for specific recommendations.
 
## 🏃 Notes
-----
- Ensure that the Flask server is running before starting the chatbot interface.
- Adjust file paths for images if they are located in a different directory.
"""

## 🏗️ Tech Stack
- 🔹 Frontend: React 
- 🔹 Backend: Node.js / Flask / Gen AI
- 🔹 Database: Mongo DB
- 🔹 Other: NLTK / chatbot

## 👥 Team
- **TriagingTitan** - [GitHub](#) | [LinkedIn](#)
