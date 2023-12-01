import fitz  # pip install PyMuPDF
from datetime import datetime
import os, io

# https://github.com/UB-Mannheim/tesseract/wiki Download and install tessaract in the link to do ocr operations

def highlight_text(pdf_path, output_path, search_text_list):
    doc = fitz.open(pdf_path)

    for page_num in range(doc.page_count):
        page = doc[page_num]
        ocr_page = page.get_textpage_ocr(flags=3, language='eng', full=True, dpi=600, tessdata=r"C:\Program Files\Tesseract-OCR\tessdata")
        for search_txt in search_text_list:
            ls = ocr_page.search(search_txt)
            if ls:
                print(search_txt + " ---- Highlighted" )
                highlight = page.add_highlight_annot(ls)
                highlight.set_colors({"stroke":(1, 0, 0)}) 

    doc.save(output_path)
    doc.close()

if __name__ == "__main__":

    # change pdf path
    input_pdf_path = r"D:\TEMP\PDF_READ_HIGHLIGHT\highlight.pdf"

    input_folder_name = os.path.dirname(input_pdf_path)
    time_stamp = str(datetime.now().strftime("%m%d%Y_%H%M"))
    output_pdf_name = "output_" + time_stamp + ".pdf"
    output_pdf_path =  os.path.join(input_folder_name, output_pdf_name)
    
    # list of strings to search and highlight in pdf file
    search_text_list = ["india", "area", "text", "friend"]
    highlight_text(input_pdf_path, output_pdf_path, search_text_list)

