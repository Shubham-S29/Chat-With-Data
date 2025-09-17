import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv  # <-- 1. IMPORT THE LIBRARY

# --- Configuration ---
# Name of your Excel file
EXCEL_FILE_NAME = "sales_data.xlsx"
# ---------------------

def initialize_ai():
    """Configures the Gemini API and returns the model."""
    load_dotenv()  # <-- 2. LOAD VARIABLES FROM .env FILE

    try:
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            print("Error: GOOGLE_API_KEY not found.")
            print("Please make sure you have a .env file with GOOGLE_API_KEY='your_key' in it.")
            return None
            
        genai.configure(api_key=api_key)
        generation_config = genai.types.GenerationConfig(
            temperature=0.0,
            max_output_tokens=256
        )
        model = genai.GenerativeModel('gemini-1.5-flash-latest', generation_config=generation_config)
        return model
    except Exception as e:
        print(f"Error during AI initialization: {e}")
        return None

def get_data_context(df):
    """Creates a text summary of the DataFrame's structure for the AI."""
    column_names = df.columns.tolist()
    data_preview = df.head(100).to_string()
    
    context = f"""
DataFrame Columns: {column_names}
Data Preview:
{data_preview}
"""
    return context

def generate_pandas_code(model, query, data_context):
    """Asks Gemini to convert a natural language query into Pandas code."""
    prompt = f"""
You are an expert Python programmer specializing in the Pandas library. Your task is to convert the user's question into a single, executable line of Python Pandas code that operates on a DataFrame named 'df'.

Based on the following DataFrame schema and data preview, generate the appropriate Pandas code.

{data_context}

Rules:
1.  The DataFrame is available in a variable named `df`.
2.  Your response must be ONLY the Python code. Do not add any explanation, comments, or markdown formatting like ```python ... ```.
3.  Handle potential misspellings in the user's query by finding the closest match in the data.
4.  If the question cannot be answered from the data, is nonsensical, or is not related to the data, respond with the single word: 'Error'.

User Question: "{query}"

Pandas Code:
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"An error occurred while communicating with the Gemini API: {e}")
        return "Error"

def chat():
    """Main function to run the chatbot loop."""
    
    try:
        df = pd.read_excel(EXCEL_FILE_NAME)
    except FileNotFoundError:
        print(f"Error: '{EXCEL_FILE_NAME}' not found. Please make sure the Excel file is in the same directory.")
        return

    model = initialize_ai()
    if not model:
        return
        
    print("Ask me anything about your data. Type 'exit' to quit.")

    data_context = get_data_context(df)

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            break

        pandas_code = generate_pandas_code(model, user_input, data_context)

        if pandas_code.lower() == 'error':
            print("Bot: I'm sorry, I can't answer that question. It might be outside the scope of the available data.")
            continue
            
        
        try:
            result = eval(pandas_code, {'df': df, 'pd': pd})
            print(f"Bot (Answer): {result}")
        except Exception as e:
            print(f"Bot: I encountered an error trying to calculate that: {e}")
            print("Bot: This might be due to an incorrect formula from the AI. Please try rephrasing your question.")

if __name__ == "__main__":
    chat()