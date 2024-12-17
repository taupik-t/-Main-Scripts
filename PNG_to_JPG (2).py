from PIL import Image

# Open the PNG image
png_image = Image.open('KTP-ME.png')

# Convert the image to RGB (required for JPEG)
jpg_image = png_image.convert('RGB')

# Save the image as JPEG
jpg_image.save('path_to_save_image.jpg')
