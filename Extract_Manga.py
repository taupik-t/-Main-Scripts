import os
import zipfile

source_directory = ("D:\\Code\\Scripts\\Download\\Komik\\_Manhua\\The Demon King Who Lost His Job")


def extract_zip(directory):
    items = os.listdir(directory)
    sorted_zip_files = sorted(item for item in items if item.endswith(".zip"))

    print("Sorted ZIP files:")
    for zip_file in sorted_zip_files:
        zip_file_path = os.path.join(directory, zip_file)

        # Extract the filename without extension
        file_name = os.path.splitext(zip_file)[0]

        # Create a directory using the extracted filename
        folder_path = os.path.join(directory, file_name)
        os.makedirs(folder_path, exist_ok=True)

        # Extract the contents of the ZIP file into the created folder
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(folder_path)

        print(f"Created folder '{file_name}' and extracted contents from '{zip_file}'")


def rename_folders_first(directory):
    for folder_name in os.listdir(directory):
        old_path = os.path.join(directory, folder_name)
        if os.path.isdir(old_path):
            new_name = folder_name.replace("-", " ").title()
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {folder_name} -> {new_name}")


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
    # Specify the source directory to monitor
    extract_zip(source_directory)
    rename_folders_first(source_directory)
    rename_folders(source_directory)
