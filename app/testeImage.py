from PIL import Image
import pytesseract

image = Image.open('C:/Users/higor/Downloads/IMAGEMTESTE2.jpg')

text = pytesseract.image_to_string(image)


print(text)