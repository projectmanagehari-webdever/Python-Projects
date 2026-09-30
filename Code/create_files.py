# Step 1: Create Folders and files
# B. Creating 100 files in the folder (Before running this code check if files already exists
import random

def create_files(folder_name):
    """This function creates files in format f1_mm-dd-yyyy.txt in the folder defined in main.py"""
    # To count number of files created.
    # count : int = 0

    for i in range(1, 10):
        try:
            month = random.randint(1, 12)
            day = random.randint(1,30)
            year = random.randint(2000, 2026)

            date = f"{month}-{day}-{year}"

            with open(f"{folder_name}/f{i}_{date}.txt", 'w') as fileobject:
                fileobject.write(f"File {i} created with date {date}")
                fileobject.close()
                # count += 1

        except FileExistsError:
            print("File already exists let us continue.....")

    # print(count,"files created.")