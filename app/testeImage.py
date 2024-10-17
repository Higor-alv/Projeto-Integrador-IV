from PIL import Image
import pytesseract

# Se necessário, defina o caminho do Tesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Abra uma imagem
image = Image.open('C:/Users/higor/Downloads/IMAGEMTESTE2.jpg')

# Extraia texto da imagem
text = pytesseract.image_to_string(image)

# Imprima o texto extraído
print(text)