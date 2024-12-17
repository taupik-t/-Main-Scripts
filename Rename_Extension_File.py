import os

def rename_extension(directory, initial_ext, target_ext):

    if not os.path.isdir(directory):
        print(f"The path {directory} is not a valid directory.")
        return;

    for file in os.listdir(directory):
        if file.endswith(".bin"):
            new_file = file[:-4] + ".jpg"

            old_name = os.path.join(directory, file)
            new_name = os.path.join(directory, new_file)

            os.rename(old_name, new_name)
            print(f"Renamed: {old_name} --> {new_name}")

    
        
