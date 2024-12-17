import os

folder_path = r"C:\Users\taupi\Scripts\Download\Manga\"


def delete_index_html(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")


def check_and_delete_index_html(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower() == "index.html":
                file_path = os.path.join(root, file)
                delete_index_html(file_path)


if __name__ == "__main__":
    check_and_delete_index_html(folder_path)
