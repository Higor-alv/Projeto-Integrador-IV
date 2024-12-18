document.getElementById('uploadPdfBtn').addEventListener('click', async () => {
    const fileInput = document.getElementById('upload');
    const file = fileInput.files[0];

    if (!file) {
        alert("Por favor, selecione um arquivo.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const loader = document.getElementById('loader');
    loader.style.display = 'block';

    try {
        const response = await fetch('http://127.0.0.1:8000/extract/', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error("Erro ao processar o arquivo.");
        }

        const data = await response.json();
        loader.style.display = 'none';

        const chat = document.getElementById('chat');
        chat.style.display = 'block';

        
        const chatOutput = document.getElementById('chatOutput');
        chatOutput.innerHTML = `<p>${data.extracted_text}</p>`;

      
        const sendBtn = document.getElementById('sendBtn');
        sendBtn.disabled = false;

    
        window.extractedText = data.extracted_text;
        window.summary = data.summary || "Resumo não disponível.";  

    } catch (error) {
        loader.style.display = 'none';
        alert(error.message);
    }
});

document.getElementById('sendBtn').addEventListener('click', async () => {
    const question = document.getElementById('chatInput').value;

    if (!question) {
        alert("Por favor, digite uma pergunta.");
        return;
    }

    const chatOutput = document.getElementById('chatOutput');
    chatOutput.innerHTML += `<div><strong>Você:</strong> ${question}</div>`;

    const loader = document.getElementById('loader');
    loader.style.display = 'block';

    try {
       
        const context = window.extractedText;

        
        if (!context) {
            throw new Error("Texto extraído não encontrado. Certifique-se de ter feito o upload de um arquivo.");
        }

        
        const qaResponse = await fetch('http://127.0.0.1:8000/qa/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                context: context, 
                question: question 
            })
        });

        
        if (!qaResponse.ok) {
            const errorDetails = await qaResponse.text();
            throw new Error(`Erro ao obter resposta: ${errorDetails}`);
        }

        const answerData = await qaResponse.json();

       
        chatOutput.innerHTML += `<div><strong>Resposta:</strong> ${answerData.answer}</div>`;
        document.getElementById('chatInput').value = '';

    } catch (error) {
        console.error("Erro ao obter resposta da API:", error);
        alert(error.message); 
    } finally {
        loader.style.display = 'none';
    }
});

document.getElementById('downloadPdfBtn').addEventListener('click', () => {
    const summary = window.summary; 

    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    
    const pageWidth = doc.internal.pageSize.getWidth() - 20; 
    const summaryLines = doc.splitTextToSize(summary, pageWidth);


    doc.setFontSize(16);
    doc.text("Resumo:", 10, 10);
    doc.setFontSize(12);
    doc.text(summaryLines, 10, 20);


    doc.save("resumo.pdf");
});
