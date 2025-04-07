from fpdf import FPDF
import random

def make_pdf(filename,num_page=1):
    pdf = FPDF()
    for _ in range(num_page):
        pdf.add_page()
        pdf.set_font("Arial", size=12)      

        for _ in range(30):  # 30 lines per page
            random_text = " ".join(random.choices([
                "hello", "world", "python", "code", "project",
                "chatgpt", "merge", "pdf", "data", "file",
                "test", "random", "generate", "tool", "simple"
            ], k=8))
            pdf.cell(200, 10, txt=random_text, ln=True)
    pdf.output(filename)


file_path = []
for i in range(1,5):
    file_path.append(f"pdf_file_{i}.pdf")
    make_pdf(file_path[i-1], num_page=3)

file_path


