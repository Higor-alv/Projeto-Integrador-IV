document.getElementById('uploadPdfBtn').addEventListener('click', async () => {
    const fileInput = document.getElementById('pdfUpload');
    const file = fileInput.files[0];
    if (!file) {
        alert("Por favor, selecione um arquivo PDF.");
        return;
    }
    
    const formData = new FormData();
    formData.append("file", file);
    
    const loader = document.getElementById('loader');
    loader.style.display = 'block';
    
    const response = await fetch('http://127.0.0.1:8000/extract_pdf/', {
        method: 'POST',
        body: formData
    });
    
    const data = await response.json();
    generatePDF(data);
    loader.style.display = 'none';
});

document.getElementById('uploadImageBtn').addEventListener('click', async () => {
    const fileInput = document.getElementById('imageUpload');
    const file = fileInput.files[0];
    if (!file) {
        alert("Por favor, selecione uma imagem.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const loader = document.getElementById('loader');
    loader.style.display = 'block';
    
    const response = await fetch('http://127.0.0.1:8000/extract_image/', {
        method: 'POST',
        body: formData
    });
    
    const data = await response.json();
    generatePDF(data);
    loader.style.display = 'none';
});

document.getElementById('uploadDocxBtn').addEventListener('click', async () => {
    const fileInput = document.getElementById('docxUpload');
    const file = fileInput.files[0];
    if (!file) {
        alert("Por favor, selecione um arquivo DOCX.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const loader = document.getElementById('loader');
    loader.style.display = 'block';

    try {
        const response = await fetch('http://127.0.0.1:8000/extract_docx/', {
            method: 'POST',
            body: formData
        });

        // Checa se a resposta foi bem-sucedida
        if (!response.ok) {
            throw new Error('Erro na extração do arquivo DOCX');
        }

        const data = await response.json();

        // Verifica se a resposta contém os dados necessários
        if (data.error) {
            alert(`Erro: ${data.error}`);
        } else {
            // Gera o PDF com os dados retornados
            generatePDF(data);
        }
    } catch (error) {
        console.error('Erro:', error);
        alert('Houve um erro ao processar o arquivo.');
    } finally {
        loader.style.display = 'none';
    }
});

function generatePDF(data) {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();
    let y = 10;
    const lineHeight = 10;
    const margin = 10;
    const pageWidth = doc.internal.pageSize.getWidth();

    doc.text("Texto Extraído:", margin, y);
    y += lineHeight;

    const extractedTextLines = doc.splitTextToSize(data.extracted_text, pageWidth - 2 * margin);
    extractedTextLines.forEach(line => {
        doc.text(line, margin, y);
        y += lineHeight;
        if (y > doc.internal.pageSize.getHeight() - margin) {
            doc.addPage();
            y = 10;
        }
    });

    y += lineHeight;

    doc.text("Resumo:", margin, y);
    y += lineHeight;

    const summaryLines = doc.splitTextToSize(data.summary, pageWidth - 2 * margin);
    summaryLines.forEach(line => {
        doc.text(line, margin, y);
        y += lineHeight;
        if (y > doc.internal.pageSize.getHeight() - margin) {
            doc.addPage();
            y = 10;
        }
    });

    doc.save("resultado.pdf");
}
