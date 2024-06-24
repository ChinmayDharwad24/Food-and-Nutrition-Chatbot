import streamlit as st
from transformers import pipeline

# Initialize the model and tokenizer
model_name = "gpt2"
generator = pipeline('text-generation', model=model_name)

# Function to get response from GPT-2
def get_response(prompt):
    responses = generator(prompt, max_length=100, num_return_sequences=1)
    return responses[0]['generated_text']

# Streamlit UI
st.title("Food and Nutrition Chatbot")
st.write("Ask me anything about recipes, nutrition, and dietary advice!")

query = st.text_input("Enter your query here:")

if query:
    response = get_response(query)
    st.write("**Response:**")
    st.write(response)
