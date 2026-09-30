# Step 1: Create Folder and files.
# A. Create Folder
import os

def create_folder(folder_name : str):
    """Pass a string to create a folder of that name."""
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print("Already exists:",folder_name)