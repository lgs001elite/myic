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


def adjust_pdf_content3(input_pdf, output_pdf, width, height):
    # Open the input PDF
    document = fitz.open(input_pdf)

    # Define the new page size (16:9 aspect ratio)
    new_page_size = (width, height)

    for page_num in range(document.page_count):
        page = document.load_page(page_num)

        # Get the original page size
        original_rect = page.rect

        # Define the margin (in points, 1 inch = 72 points)
        margin = 36  # 0.5 inch margin

        # Calculate the new rectangle with margins
        new_width = new_page_size[0] - 2 * margin
        new_height = new_page_size[1] - 2 * margin

        # Ensure new width and height are positive
        if new_width <= 0 or new_height <= 0:
            raise ValueError("Margins are too large for the given page size")

        new_rect = fitz.Rect(margin, margin, new_page_size[0] - margin, new_page_size[1] - margin)

        # Define a transformation matrix to fit the content within the new rectangle
        scale_x = new_width / original_rect.width
        scale_y = new_height / original_rect.height
        transform = fitz.Matrix(scale_x, scale_y).pretranslate(-original_rect.x0, -original_rect.y0)

        # Apply the transformation to the page
        page.apply_matrix(transform)

        # Set the crop box to the new rectangle
        page.set_cropbox(new_rect)

    # Save the adjusted PDF to a new file
    document.save(output_pdf)






# Example usage
input_pdf = "figures_nsdi_zoomed_in.pdf"
output_pdf = "figures_fitting.pdf"
resize_pdf_to_content2(input_pdf, output_pdf)
