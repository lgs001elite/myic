from PIL import Image

# Specify the path to your JPG image
input_jpg_path = 'riotee_scenario.jpg'

# Specify the path for the output PNG image
output_png_path = './riotee_scenario.pdf'

# # Open the JPG image
# with Image.open(input_jpg_path) as img:
#     # Convert and save as PNG
#     img.save(output_png_path)

# print("Image successfully converted to PNG format!")


image = Image.open(input_jpg_path)

# Convert the image to RGB (necessary for PDF conversion)
if image.mode in ('RGBA', 'LA'):
    image = image.convert('RGB')

# Save the image as a PDF
image.save(output_png_path, 'PDF', resolution=100.0)

print("Image successfully converted to PDF format!")