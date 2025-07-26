import os
import shutil

# Path to the main folder containing the subfolders
main_folder_path = r''

# Function to move files from subfolders to the main folder
def move_files_to_main_folder(folder_path):
    # Loop through the subfolders and move their contents to the main folder
    for root, dirs, files in os.walk(folder_path):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            print(f"Processing folder: {folder_path}")
            # List and move files to the main folder
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)
                # Move file to the main folder
                shutil.move(file_path, main_folder_path)
            # Once files are moved, delete the (now empty) folder
            os.rmdir(folder_path)
        break  # To ensure we don't go deeper into sub-subfolders

# Call the function
move_files_to_main_folder(main_folder_path)