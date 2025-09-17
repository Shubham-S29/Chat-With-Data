# Chat-With-Data🤖✨

A smart, terminal-based AI chatbot that uses the Gemini API to answer questions about your Excel data. No more manual searching—just ask and get insights instantly!

### 🌟 About The Project

**ChatWithData** is a Python-based tool designed to bridge the gap between complex data in spreadsheets and the need for quick, natural language answers. Instead of filtering, sorting, or writing formulas in Excel, you can simply ask questions like "What were the total sales in the North region?" and get an immediate, accurate response.

This project leverages the power of Google's Gemini API to understand user questions, analyze the provided data context, and generate intelligent answers while strictly adhering to the information within the dataset.

**Key Features:**

* **AI-Powered Q&A:** Uses the Gemini 1.5 Flash model for fast and intelligent responses.
* **Excel/CSV Integration:** Easily loads and processes data from `.xlsx` files using the pandas library.
* **Context-Aware:** Answers are based *only* on the data you provide, preventing hallucinations or out-of-scope answers.
* **Terminal-Based Interface:** A lightweight and clean command-line interface for easy interaction.
* **Secure:** Keeps your API key safe using an environment file.

### 🛠️ Tech Stack

This project is built with a few key technologies:

* **Python:** The core programming language.
* **Google Gemini API:** For the natural language understanding and generation.
* **Pandas:** For loading and handling the Excel data.
* **python-dotenv:** For managing environment variables securely.

### 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

**Prerequisites:**

* Python 3.8+ installed
* A Gemini API Key from [Google AI Studio](https://aistudio.google.com)

**Installation & Setup:**

1. **Clone the repository**
   ```sh
   git clone https://github.com/Shubham-S29/Chat-With-Data.git
   cd Chat-With-Data
    ```
2.  **Create and activate a virtual environment:**
    ```sh
    # Create the environment
    python -m venv venv
    # Activate it (Windows)
    venv\Scripts\activate
    ```
3.  **Create a `requirements.txt` file** by running this command in your terminal:
    ```sh
    pip freeze > requirements.txt
    ```
    *(This is a good practice before you push your final code to GitHub)*

4.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
5.  **Create a `.env` file** in the root directory and add your API key:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```
6.  **Run the chatbot!**
    ```sh
    python chatbot.py
    ```

### 💡 Example Usage (Demo)

Once the chatbot is running, you can start asking questions.

```
--- Data Analyst Chatbot ---
Ask questions about your sales data. Type 'exit' to quit.

You: What was the total profit for all laptops sold?
Bot: The total profit for all laptops sold is 49000.

You: Which region had the highest sales?
Bot: The West region had the highest sales with a total of 150000.

You: Who is Shah Rukh Khan?
Bot: I cannot answer this question as it is outside the scope of the provided data.

You: exit
Bot: Goodbye!
```