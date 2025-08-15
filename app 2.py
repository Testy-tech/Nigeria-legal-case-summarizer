import streamlit as st
from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# App title
st.title("🇳🇬 Nigeria Legal Case Summarizer")
st.write("Paste a Nigerian court judgment below and get a concise summary.")

# Text input
judgment_text = st.text_area("Enter case text here:")

if st.button("Summarize"):
    if judgment_text.strip():
        summary = summarizer(judgment_text, max_length=150, min_length=40, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please paste the case text first.")
