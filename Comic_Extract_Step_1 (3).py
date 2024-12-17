import os
import glob

# Define the path to the directory
directory_path = r'C:\Users\taupi\Downloads\MY FILE\Scripts\Comic'

# Use glob to find all .cbz files in the specified directory
cbz_files = glob.glob(os.path.join(directory_path, '*.cbz'))

# Loop through each .cbz file and rename it to .zip
for cbz_file in cbz_files:
    # Create the new file name by replacing the .cbz extension with .zip
    zip_file = cbz_file[:-4] + '.zip'
    
    # Rename the file
    os.rename(cbz_file, zip_file)
    print(f'Renamed: {cbz_file} to {zip_file}')

print('All files have been renamed.')
