from pypdf import PdfWriter,PdfReader
pdf = PdfWriter()

def merget_pdf(file_path):
    for file in file_path:
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            pdf.add_page(page)

    with open("merged_pdf.pdf", "wb") as f:
        pdf.write(f)


