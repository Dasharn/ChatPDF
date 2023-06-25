import streamlit as st
import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize
import openai

# Set up OpenAI credentials
openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text

# Function to process and tokenize text
def process_text(text):
    sentences = sent_tokenize(text)
    return sentences

# Function to generate summary using OpenAI
def generate_summary(sentences, complexity_level):
    complexity_prompt = {
        "child": "This is a summary suitable for children:",
        "high school": "This is a summary suitable for high school students:",
        "university student": "This is a summary suitable for university students:",
        "professional": "This is a summary suitable for professionals:"
    }
    input_text = f"{complexity_prompt[complexity_level]} {' '.join(sentences)}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        temperature=0.3,
        max_tokens=150
    )
    summary = response.choices[0].text.strip()
    return summary

# Function to answer user questions using OpenAI
def answer_question(question, text):
    input_text = f"Question: {question}\nContext: {text}\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        temperature=0.3,
        max_tokens=30
    )
    answer = response.choices[0].text.strip()
    return answer

# Streamlit application
def main():
    st.title("ChatPDF - Question-Answering and Summarization Tool")

    # File upload section
    st.header("Upload PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        text = extract_text_from_pdf(uploaded_file)
        sentences = process_text(text)

        # Summary section
        if st.checkbox("Generate Summary"):
            complexity_level = st.selectbox(
                "Select Complexity Level",
                ("child", "high school", "university student", "professional")
            )
            summary = generate_summary(sentences, complexity_level)
            st.subheader("Summary")
            st.write(summary)

        # Question-answering section
        st.header("Ask Questions")
        question = st.text_input("Enter your question")
        if st.button("Ask"):
            if not question:
                st.warning("Please enter a question.")
            else:
                answer = answer_question(question, text)
                st.subheader("Answer")
                st.write(answer)

# Run the Streamlit application
if __name__ == "__main__":
    main()
