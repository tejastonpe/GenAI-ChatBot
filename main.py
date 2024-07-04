import streamlit as st
import os
from functions import pdftext_to_vector_single
from chatbot import  query_data

st.title("ChatBot")

uploaded_files = st.file_uploader("Choose PDFs", accept_multiple_files=True, type=["pdf"])

if st.button("Upload Documents"):        
    if uploaded_files:
        for uploaded_file in uploaded_files:
            pdftext_to_vector_single(uploaded_file)
        st.success("All PDF files processed and stored successfully.")

query = st.text_input("Enter your query:")
if st.button("Submit query"):        
    if query:
        response = query_data(query)
        st.write("Response:", response)