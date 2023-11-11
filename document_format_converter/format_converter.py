from pdf2docx import Converter

def pdf_to_docx():
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()

def docx_to_pdf():
    '''
    Add code to convert 
    document file to a pdf file
    '''
 

if __name__ == '__main__':
    print("The types of conversions" + "\n1. PDF to DOCUMENT" + "\n2. DOCUMENT to PDF")
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
        print('Succesffuly converted from docx to pdf file!')
 
