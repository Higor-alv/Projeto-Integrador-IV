from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

def answer_question(question: str, context: str) -> dict:
    if not context or not question:
        return {"error": "Contexto ou pergunta inválida."}

    response = qa_pipeline(question=question, context=context)
    return {"question": question, "answer": response['answer'], "score": response['score']}
