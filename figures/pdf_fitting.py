from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_pdf(filename, content):
    # Create a canvas object
    c = canvas.Canvas(filename, pagesize=letter)

    # Get the width and height of the content
    width, height = c.stringWidth(content, "Helvetica", 12), 12

    # Set the page size to fit the content exactly
    c.setPageSize((width + 1 * inch, height + 1 * inch))

    # Draw the content on the canvas
    c.drawString(0.5 * inch, 0.5 * inch, content)

    # Save the PDF
    c.save()

# Example usage
content = "This is a test string to fit exactly into the page size."
create_pdf("dynamic_page_size.pdf", content)
