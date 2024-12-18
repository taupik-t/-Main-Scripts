import os

source_directory = "C:\\Users\\taupi\\Videos\\New folder"

def rename_folders_first(directory):
    for folder_name in os.listdir(directory):
        old_path = os.path.join(directory, folder_name)
        if os.path.isdir(old_path):
            new_name = folder_name.replace("-", " ").title()
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {folder_name} -> {new_name}")

if __name__ == "__main__":
    rename_folders_first(source_directory)

def rename_folders(directory):
    for folder_name in os.listdir(directory):
        old_path = os.path.join(directory, folder_name)
        if os.path.isdir(old_path):
            # Check if the folder name contains the word "Chapter"
            if "Chapter" in folder_name:
                # Extract the chapter number from the folder name
                chapter_number = folder_name.split("Chapter")[-1].strip()
                # Create the new name with "Chapter" and the chapter number
                new_name = f"Chapter {chapter_number}"
                new_path = os.path.join(directory, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed: {folder_name} -> {new_name}")

if __name__ == "__main__":
    rename_folders(source_directory)
