from time import time
from pdf2image import convert_from_path
import pytesseract
import re
import fitz
from PIL import Image
import io


# part 0 - OCR extraction using OCR.space API
# https://ocr.space/

# part 1: OCR extraction
### Using PyMuPDF (fitz) for OCR extraction
def ocr_pdf_to_text(pdf_path, output_path=None):
    if output_path is None:
        output_path = pdf_path.replace('.pdf', '.txt')
    
    doc = fitz.open(pdf_path)
    with open(output_path, "w", encoding="utf-8") as f:
        for i, page in enumerate(doc, 1):
            pix = page.get_pixmap(dpi=300)
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            text = pytesseract.image_to_string(img, lang="eng")
            f.write(text + "\n")

    return text

t0 = time()
text = ocr_pdf_to_text("document.pdf")
### Alternative method using pdf2image and pytesseract
# pages = convert_from_path('document.pdf', 300)
# text = ""

# for page in pages:
#     text += pytesseract.image_to_string(page, lang='eng')

# with open('document.txt', 'w', encoding='utf-8') as f:
#     f.write(text)

t1 = time()
print(f"Time taken for OCR: {t1 - t0} seconds")
print("Text extraction complete. Check document.txt for results.")

