from transformers import pipeline

# Carregar o modelo
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    max_length = 1024  # ou qualquer limite que você ache adequado
    # Dividir o texto em partes menores
    text_parts = [text[i:i + max_length] for i in range(0, len(text), max_length)]
    summaries = []

    for part in text_parts:
        summary = summarizer(part, max_length=130, min_length=30, do_sample=False)
        summaries.append(summary[0]['summary_text'])

    # Juntar os resumos das partes
    final_summary = " ".join(summaries)
    return final_summary
