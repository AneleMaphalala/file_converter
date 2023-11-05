from pdf2docx import Converter

def pdf_to_docx():
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()
 


if __name__ == '__main__':
    pdf_file = input('Enter pdf file name: ')
    docx_file = input('Enter the name of the new document file: ')
    pdf_to_docx()
    print('Successfully converted from pdf into document file!')