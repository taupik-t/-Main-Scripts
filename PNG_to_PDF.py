import os
from PIL import Image

# Path to the folder containing the images
image_folder = r"Just Twilight/Chapter 45"
# Output PDF file path
pdf_path = r"Just Twilight/Chapter 45/Chapter 45.pdf"

# Get all image files in the folder
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('jpg', 'jpeg', 'png', 'webp'))]
image_files.sort()  # Sort files to maintain order

# Convert images to PDF
images = []
for file in image_files:
    img_path = os.path.join(image_folder, file)
    img = Image.open(img_path).convert("RGB")
    images.append(img)

# Save all images as a single PDF file, each image as a new page
if images:
    images[0].save(pdf_path, save_all=True, append_images=images[1:])
    print(f"PDF created successfully at: {pdf_path}")
else:
    print("No images found in the specified folder.")
