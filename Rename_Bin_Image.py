import os

def rename_bin_to_jpg(directory):
    # Check if the provided path is a directory
    if not os.path.isdir(directory):
        print(f"The provided path {directory} is not a valid directory.")
        return
    
    # Loop through all the files in the directory
    for filename in os.listdir(directory):
        # Check if the file has a .bin extension
        if filename.endswith('.bin'):
            # Create the new filename by replacing the .bin extension with .jpg
            new_filename = filename[:-4] + '.jpg'
            # Get the full path for the old and new filenames
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {old_file} -> {new_file}")

# Specify the directory to scan for .bin files
# directory_path = r"E:\Code\Scripts\New folder\New folder"
# directory_path = r"E:\Code\Scripts\Chapter 106"

# Call the function to rename .bin files to .jpg
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 76")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 77")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 78")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 79")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 80")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 81")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 82")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 83")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 84")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 85")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 86")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 87")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 88")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 89")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 90")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 91")
rename_bin_to_jpg(r"C:\Users\taupi\Downloads\Code\Script\Comic\Chapter 92 End")