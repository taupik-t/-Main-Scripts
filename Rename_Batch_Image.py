import os

def rename_images(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
                file_path = os.path.join(root, file)
                base_name, ext = os.path.splitext(file)

                # Check if the file name is a single digit
                if len(base_name) == 1 and base_name.isdigit():
                    new_name = f"0{base_name}{ext}"
                    new_path = os.path.join(root, new_name)

                    # Rename the file
                    os.rename(file_path, new_path)
                    print(f"Renamed: {file} -> {new_name}")

# Specify the folder path
folder_path = r"D:\\Code\\Scripts\\Download\\Komik\\_Manhua\\The Demon King Who Lost His Job\\Chapter 1"

# Call the function to rename images
rename_images(folder_path)
