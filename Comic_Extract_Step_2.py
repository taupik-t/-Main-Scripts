import os
import glob
import zipfile

# Define the path to the directory containing the .zip files
directory_path = r'C:\Users\taupi\Downloads\MY FILE\Scripts\Comic'

# Use glob to find all .zip files in the specified directory
zip_files = glob.glob(os.path.join(directory_path, '*.zip'))

# Loop through each .zip file
for zip_file in zip_files:
    # Get the base name of the zip file (without directory path)
    zip_base_name = os.path.basename(zip_file)
    
    # Create the folder name by removing the .zip extension
    folder_name = zip_base_name[:-4]
    
    # Create the full path for the new folder
    folder_path = os.path.join(directory_path, folder_name)
    
    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    
    # Extract the contents of the zip file into the newly created folder
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(folder_path)
    
    print(f'Extracted: {zip_file} to {folder_path}')

print('All files have been extracted.')
