# import os
# import glob

# # Define the path to the main directory
# main_directory = r'C:\Users\taupi\Downloads\MY FILE\Scripts\Comic'

# # Get a list of all folders inside the main directory
# folders = [f.path for f in os.scandir(main_directory) if f.is_dir()]

# # Loop through each folder
# for folder in folders:
#     # Use glob to find all .bin files in the current folder
#     bin_files = glob.glob(os.path.join(folder, '*.bin'))
    
#     # Loop through each .bin file and rename it to .jpg
#     for bin_file in bin_files:
#         # Create the new file name by replacing the .bin extension with .jpg
#         jpg_file = bin_file[:-4] + '.jpg'
        
#         # Rename the file
#         os.rename(bin_file, jpg_file)
#         print(f'Renamed: {bin_file} to {jpg_file}')

# print('All .bin files have been renamed to .jpg.')

import os
import zipfile
import shutil

# Define the path to the main directory
main_directory = r'C:\Users\taupi\Downloads\MY FILE\Scripts\Comic'

# Get a list of all folders inside the main directory
folders = [f.path for f in os.scandir(main_directory) if f.is_dir()]

# Loop through each folder
for folder in folders:
    # Get the folder name
    folder_name = os.path.basename(folder)
    
    # Define the path for the .zip file
    zip_path = os.path.join(main_directory, f'{folder_name}.zip')
    
    # Create a .zip file with the name of the folder
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Loop through all files in the folder
        for root, dirs, files in os.walk(folder):
            for file in files:
                # Get the full path of the file
                file_path = os.path.join(root, file)
                # Add the file to the zip archive
                zipf.write(file_path, os.path.relpath(file_path, folder))
    
    # Define the path for the .cbz file
    cbz_path = zip_path.replace('.zip', '.cbz')
    
    # Rename the .zip file to .cbz
    os.rename(zip_path, cbz_path)
    print(f'Compressed and renamed: {zip_path} to {cbz_path}')

print('All folders have been compressed and renamed.')

