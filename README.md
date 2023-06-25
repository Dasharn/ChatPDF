# ChatPDF - Question-Answering and Summarization Tool

ChatPDF is a web application built with Streamlit that allows users to upload a PDF file, generate a summary of its content, and ask questions related to the PDF for automated answering. The application utilizes the OpenAI API for text summarization and question answering. The goal of this application is to build a sort of learning platform allowing users to learn more efficiently.

## Features

- Upload a PDF file
- Generate a summary of the PDF content
- Ask questions related to the PDF content
- Get automated answers to questions

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/chatpdf.git
   cd chatpdf
   pip install requirements.txt
   python app.py
   ```
   
2. Set Up OpenAI credentials:
* Go [here](https://beta.openai.com/) 
   * Create an account
   * Obtain an API key
   * Replace "YOUR_OPENAI_API_KEY" 

## Usage

1. Run the application `streamlit run app.py`

2. Access the application in your browser

3. Upload a PDF file by clicking on the "Choose a PDF file button"

4. Generate a summary:

    Check the "Generate Summary" checkbox.
    Select the complexity level from the dropdown menu.
    The summary will be displayed below.
5. Ask questions:

    * Enter your question in the text input field.
    * Click the "Ask" button.
    * The answer to your question will be displayed below.

# License
    This project is licensed under the MIT License.



