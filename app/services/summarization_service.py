from transformers import pipeline


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    
    if not text or text.strip() == "":
        return "Texto vazio ou inválido para resumo."

  
    max_length = 512
    text_parts = [text[i:i + max_length] for i in range(0, len(text), max_length)]
    summaries = []

    for part in text_parts:
        if part.strip():  
            
            summary = summarizer(part, max_length=100, min_length=30, do_sample=False)
            summaries.append(summary[0]['summary_text'])

    final_summary = " ".join(summaries)
    return final_summary