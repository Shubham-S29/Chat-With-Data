# chatbot.py

import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

# --- SETUP ---
# Load environment variables from the .env file
load_dotenv()

# Configure the Gemini API with your key
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file")
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    exit()

# --- DATA LOADING ---
def load_data(file_path):
    """Loads data from an Excel file into a pandas DataFrame."""
    try:
        df = pd.read_excel(file_path)
        print("Excel data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the Excel file: {e}")
        return None

# --- GEMINI INTERACTION ---
def get_gemini_response(data_context, question):
    """
    Sends a prompt with data context and a question to the Gemini API.
    """
    # Create the generative model with the updated model name
    # OLD: model = genai.GenerativeModel('gemini-pro')
    # NEW:
    model = genai.GenerativeModel('gemini-1.5-flash-latest')

    # This is the core prompt engineering part
    prompt = f"""
    You are an expert data analyst. Your task is to answer questions based ONLY on the provided dataset.
    The dataset is as follows:

    {data_context}

    User's Question: "{question}"

    Rules:
    1. Analyze the data context provided above to answer the user's question.
    2. Do not use any external knowledge or information outside of the provided data.
    3. If the user's question cannot be answered using ONLY the provided data, you MUST respond with the exact phrase: "I cannot answer this question as it is outside the scope of the provided data."
    4. Provide clear, concise answers. If the question involves calculations, perform them and show the result.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Provide a more specific error message for API issues
        return f"An error occurred with the Gemini API. Please check your API key and model name. Details: {e}"

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Path to your Excel file
    excel_file_path = "sales_data.xlsx"

    # Load the data
    dataframe = load_data(excel_file_path)

    if dataframe is not None:
        # Convert the top few rows of the DataFrame to a string to use as context
        # This is more efficient than sending the entire file
        data_context_for_prompt = dataframe.head().to_string()

        print("\n--- Data Analyst Chatbot ---")
        print("Ask questions about your sales data. Type 'exit' to quit.")

        # Main loop to take user input
        while True:
            user_question = input("\nYou: ")
            if user_question.lower() == 'exit':
                print("Bot: Goodbye!")
                break

            # Get the response from Gemini
            bot_response = get_gemini_response(data_context_for_prompt, user_question)
            print(f"Bot: {bot_response}")

