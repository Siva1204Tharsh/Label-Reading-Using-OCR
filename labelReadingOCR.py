try:
    from PIL import Image
except ImportError:
    import Image


import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # r-reverse slash

def recognizeText(image):
    text=pytesseract.image_to_string(Image.open(image))
    return text

info=recognizeText('TEST3.jpg')
print(info)

file=open('label.txt','a')
file.write(info)
file.close()
print('File saved')

