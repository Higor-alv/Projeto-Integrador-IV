from transformers import pipeline
import re

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def clean_text(text: str) -> str:
    text = text.replace("\r", " ").replace("\n", " ").replace("\\", "")
    text = re.sub(r'http\S+|www\S+|[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text

def split_text_into_chunks(text: str, max_length: int) -> list:
    words = text.split(' ')
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) >= max_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks

def summarize_text(text: str) -> str:
    if not text or text.strip() == "":
        return "Texto vazio ou inválido para resumo."

    cleaned_text = clean_text(text)
    max_length = 512  # Defina o limite de caracteres para a divisão do texto
    text_parts = split_text_into_chunks(cleaned_text, max_length)
    summaries = []

    for part in text_parts:
        if part.strip():
            summary = summarizer(part, max_length=150, min_length=50, do_sample=False, length_penalty=1.0)
            summaries.append(summary[0]['summary_text'])

    final_summary = " ".join(summaries)
    return final_summary
