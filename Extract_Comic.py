import os
import re
import zipfile
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfMerger

def convert_cbz_to_zip(cbz_file):
    """Rename .cbz file to .zip"""
    zip_file = cbz_file.replace('.cbz', '.zip')
    try:
        os.rename(cbz_file, zip_file)
        print(f"Converted {cbz_file} to {zip_file}")
        return zip_file
    except Exception as e:
        print(f"Failed to convert {cbz_file} to .zip: {e}")
        return None

def extract_zip(zip_file, extract_to):
    """Extract .zip file to the specified directory"""
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Extracted {zip_file} to {extract_to}")
    except Exception as e:
        print(f"Failed to extract {zip_file}: {e}")

def rename_folders_with_chapter(folder_path):
    """Rename folders containing 'Chapter [Number]' to just 'Chapter [Number]'"""
    chapter_pattern = re.compile(r'Chapter \d+')
    renamed_folders = []

    for folder_name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, folder_name)
        
        if os.path.isdir(full_path):
            match = chapter_pattern.search(folder_name)
            if match:
                new_folder_name = match.group(0)
                new_full_path = os.path.join(folder_path, new_folder_name)
                
                if not os.path.exists(new_full_path):
                    try:
                        os.rename(full_path, new_full_path)
                        print(f"Renamed folder '{folder_name}' to '{new_folder_name}'")
                        renamed_folders.append(new_full_path)
                    except Exception as e:
                        print(f"Failed to rename folder '{folder_name}': {e}")

    return renamed_folders

def process_images_in_folder(folder_path):
    """Find .webp images and combine them into a single PDF"""
    image_extension = '.webp'
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extension)]
    
    if image_files:
        image_files.sort()  # Sort by name
        pdf_path = os.path.join(folder_path, 'combined_images.pdf')

        try:
            c = canvas.Canvas(pdf_path, pagesize=letter)

            for image_file in image_files:
                image_path = os.path.join(folder_path, image_file)
                with Image.open(image_path) as img:
                    img_width, img_height = img.size
                    c.setPageSize((img_width, img_height))
                    
                    c.drawImage(image_path, 0, 0, img_width, img_height)
                    c.showPage()

            c.save()
            print(f"Created PDF with images in {folder_path}")
        except Exception as e:
            print(f"Failed to create PDF in {folder_path}: {e}")
    else:
        print(f"No images found in {folder_path}")

def combine_pdfs_from_folders(base_folder):
    """Combine PDFs from each folder into a single PDF"""
    folders = [os.path.join(base_folder, f) for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))]
    folders.sort()  # Sort folders by name

    for folder in folders:
        pdf_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith('.pdf')]
        
        if pdf_files:
            pdf_files.sort()  # Sort PDF files by name
            combined_pdf_path = os.path.join(folder, 'combined_pdfs.pdf')

            try:
                merger = PdfMerger()
                for pdf in pdf_files:
                    merger.append(pdf)
                merger.write(combined_pdf_path)
                merger.close()
                print(f"Combined PDFs in {folder} into {combined_pdf_path}")
            except Exception as e:
                print(f"Failed to combine PDFs in {folder}: {e}")

def process_comics_folder(folder_path):
    """Process all .cbz files in the given folder"""
    print("Starting to process .cbz files...")

    cbz_files = [f for f in os.listdir(folder_path) if f.endswith('.cbz')]
    if not cbz_files:
        print("No .cbz files found. Skipping conversion and extraction.")
        return

    for filename in cbz_files:
        cbz_file = os.path.join(folder_path, filename)
        
        # Convert .cbz to .zip
        zip_file = convert_cbz_to_zip(cbz_file)
        if not zip_file:
            continue
        
        # Create a folder for extraction
        folder_name = os.path.splitext(filename)[0]
        extract_to = os.path.join(folder_path, folder_name)
        try:
            os.makedirs(extract_to, exist_ok=True)
            print(f"Created directory {extract_to} for extraction")
        except Exception as e:
            print(f"Failed to create directory {extract_to}: {e}")
            continue
        
        # Extract .zip file
        extract_zip(zip_file, extract_to)
        
        # Optional: Remove the .zip file after extraction
        try:
            os.remove(zip_file)
            print(f"Removed temporary file {zip_file}")
        except Exception as e:
            print(f"Failed to remove temporary file {zip_file}: {e}")
        
    # Rename folders containing 'Chapter [Number]'
    renamed_folders = rename_folders_with_chapter(folder_path)
    if renamed_folders:
        for folder in renamed_folders:
            process_images_in_folder(folder)
    
    # Combine PDFs in each folder
    combine_pdfs_from_folders(folder_path)
    
    print("Finished processing all .cbz files and renaming folders.")

if __name__ == "__main__":
    comics_folder = 'Comics'  # Path to the folder containing .cbz files
    process_comics_folder(comics_folder)
