from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_pdf(filename, lines):
    c = canvas.Canvas(filename, pagesize=letter)

    # Calculate the total height needed for the lines
    height = len(lines) * 12 + 1 * inch
    max_line_width = max(c.stringWidth(line, "Helvetica", 12) for line in lines)
    width = max_line_width + 1 * inch

    # Set the page size to fit the content exactly
    c.setPageSize((width, height))

    # Draw each line on the canvas
    for i, line in enumerate(lines):
        c.drawString(0.5 * inch, height - (i + 1) * 12 - 0.5 * inch, line)

    # Save the PDF
    c.save()

# Example usage
lines = [
    "This is the first line of text.",
    "This is the second line of text, which is a bit longer.",
    "This is the third line."
]
create_pdf("dynamic_page_size_multiline.pdf", lines)
