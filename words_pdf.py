# Count Words in pdf

import PyPDF2
import re


def count_words_in_pdf(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = pdf_reader.numPages
    count = 0
    for i in range(num_pages):
        page = pdf_reader.getPage(i)
        count += len(re.findall(r'\w+', page.extract_text()))
    # return print(count)
    return count

count_words_in_pdf(r'')
