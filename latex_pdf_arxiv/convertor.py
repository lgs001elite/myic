import pdflatex

with open('main_arxiv.tex', 'rb') as f:
    pdfl = pdflatex.PDFLaTeX.from_binarystring(f.read(), 'my_file')
pdf, log, cp = pdfl.create_pdf()