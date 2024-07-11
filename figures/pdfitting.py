import fitz  # PyMuPDF


def resize_pdf_to_content(input_pdf, output_pdf):
    # Open the existing PDF
    doc = fitz.open(input_pdf)

    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        rect = page.rect

        # Get the text bounding boxes
        text_rects = page.get_text("bbox")
        print(f"Page {page_num + 1} bounding boxes: {text_rects}")

        if not text_rects:
            continue

        # Proceed only if text_rects is a list of tuples
        if isinstance(text_rects, list) and all(isinstance(box, tuple) for box in text_rects):
            # Flatten the bounding boxes (combine all into one overall bounding box)
            x0 = min(box[0] for box in text_rects)
            y0 = min(box[1] for box in text_rects)
            x1 = max(box[2] for box in text_rects)
            y1 = max(box[3] for box in text_rects)

            # Calculate the new size based on the bounding box
            new_rect = fitz.Rect(x0, y0, x1, y1)

            # Set the new page size
            page.set_cropbox(new_rect)
            page.set_media_box(new_rect)

    # Save the modified PDF to a new file
    doc.save(output_pdf)

import fitz  # PyMuPDF

def resize_pdf_to_content2(input_pdf, output_pdf):
    # Open the existing PDF
    doc = fitz.open(input_pdf)

    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        rect = page.rect

        # Get the text bounding boxes
        text_rects = page.get_text("bbox")

        if not text_rects:
            continue

        # Proceed only if text_rects is a list of tuples
        if isinstance(text_rects, list) and all(isinstance(box, tuple) and len(box) == 4 for box in text_rects):
            # Flatten the bounding boxes (combine all into one overall bounding box)
            x0 = min(box[0] for box in text_rects)
            y0 = min(box[1] for box in text_rects)
            x1 = max(box[2] for box in text_rects)
            y1 = max(box[3] for box in text_rects)

            # Calculate the new size based on the bounding box
            new_rect = fitz.Rect(x0, y0, x1, y1)

            # Set the new page size
            page.set_cropbox(new_rect)
            page.set_media_box(new_rect)

    # Save the modified PDF to a new file
    doc.save(output_pdf)



# Example usage
input_pdf = "figures_nsdi_zoomed_in.pdf"
output_pdf = "figures_fitting.pdf"
resize_pdf_to_content2(input_pdf, output_pdf)
