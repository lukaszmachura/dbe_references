# import pytesseract
# from pytesseract import Output
# from PIL import Image
# import cv2

# img = cv2.imread('a.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# text = pytesseract.image_to_string(gray, lang='eng')
# print(text)