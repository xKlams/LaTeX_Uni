from pypdf import PdfMerger
import sys

pdfs = [f"./PDF_Lezioni/0{i}_Lezione.pdf" for i in range(int(sys.argv[1]),10)]
for i in range(10,int(sys.argv[2]) + 1):
    pdfs.append(f"./PDF_Lezioni/{i}_Lezione.pdf")
merger = PdfMerger()

for pdf in pdfs:
    try:
        merger.append(pdf)
    except:
        print(pdf," Not found!")

merger.write("./PDF_Lezioni/PDF_completo.pdf")
merger.close()