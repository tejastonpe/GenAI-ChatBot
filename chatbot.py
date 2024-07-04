import streamlit as st
from functions import get_query_embedding
from connections import collection,db, model

def search_in_mongodb(query_vector):
    Aggregation_query = [
        {
            "$vectorSearch": {
                "queryVector": query_vector,
                "path": "embedding",
                "numCandidates": 100,
                "limit": 5,
                "index": "vector_search"
            }
        },
        {
            "$project": {
                "text": 1,
                "_id": 0
            }
        }
    ]
    try:
        results = collection.aggregate(Aggregation_query)
        data_retrived = list(results)
        
        if not data_retrived:
            print("No Relevent Information found")
                
        return data_retrived
    except Exception as e:
        print("aggregation query error:", e)
        return []

def query_data(query):
    query_embedding = get_query_embedding(query)    
    results = search_in_mongodb(query_embedding)
    
    output = []
    for result in results:
        output.append(result['text'])    
    response=get_exact_answer(output,query)
    return response

def get_exact_answer(data,query):
    if data:
        prompt = f"""
        Your task is to generate a meaningful answer in 200 words,from the following data & user query:
        data:{data}
        user query:{query}
        if data not found then give responce 'Not able to give Answer'
        """
        response = model.generate_content(prompt)
        return response.text.strip()      
