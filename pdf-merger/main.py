import os 
from PyPDF2 import PdfMerger

def merge_pdf_files(pdf_list, output, directory):
    merger = PdfMerger()
 
    for pdf in pdf_list:
        merger.append(os.path.join(directory, pdf))

    merger.write(output)
    merger.close()

def search_pdf_files(directory):
    pdf_list = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    return pdf_list

def main():
    directory = input('Enter the path to the pdf files: ') or '.'
    pdf_list = search_pdf_files(directory)

    if not pdf_list:
      print("No PDF files found in the directory. Skipping merge.")
      return

    input_name = input('Enter the name of the pdf file: ') or 'output'
    output = input_name + '.pdf'
    merge_pdf_files(pdf_list, output, directory)

if __name__ == '__main__':
    main()