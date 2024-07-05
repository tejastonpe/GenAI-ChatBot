# Chatbot
This repository contains the code for Chatbot. The chatbot is designed to give information based information stored in a vector database. The web interface is built using Streamlit using these user can add multiple files to database, and the backend MongoDB Atlas for vector storage and the Gemini API for generating meaningful responses.

### Features
* **Streamlit Web Interface:** A simple and interactive web interface for users to ask questions and receive answers.Also user can upload multiple pdf's to store into database.
* **PDF Conversion:** Convert PDFs into a vector database by embedding text data.
* **MongoDB Atlas:** Store the embedded information in MongoDB Atlas for efficient retrieval.
* **Gemini API Integration:** Use the Gemini API to provide accurate answers based on the prompt.

### Project Structure
* **main.py:** Main file to run the Streamlit web application.
* **functions.py:** Contains functions for processing and embedding text data from PDFs.
* **connections.py:** Functions for interacting with MongoDB Atlas and Gemini API
* **chatbot.py:** contains searching relavent information from database to give answers
* **.env:** Environment variables for API keys and database connections.
