from pdf2docx import Converter
from docx2pdf import convert

def pdf_to_docx():
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()

def docx_to_pdf():
    convert(docx_file, pdf_file) 

if __name__ == '__main__':
    while True:
        print("The types of conversions\n1. PDF to DOCUMENT\n2. DOCUMENT to PDF\n3. Exit\n")
        type_of_conversion = input("\nEnter the number of the conversion you want: ")

        if type_of_conversion == "1":
            pdf_file = input('Enter pdf file name: ')
            docx_file = input('Enter the name of the new document file: ')
            pdf_to_docx()
            print('Successfully converted from pdf into document file!')

        elif type_of_conversion == "2":
            docx_file = input("Enter the document file name: ")
            pdf_file = input("Enter the name of the new document: ")
            docx_to_pdf()
            print('Successfuly converted from document to pdf file!')

        elif type_of_conversion == "3":
            print('Exiting the program.\nGoodbye!')
            break

        else:
            print("Invalid input.\nPlease enter a valid option.")