# Step 3: Renaming the files
import shutil
import os
from find_date import american_date_regex

def find_date(filename):
    """Find the date in the string and return it as string."""
    mo = american_date_regex.search(filename)
    date_found = mo.group()
    return date_found

def get_new_file_name(date_found, file):
    """Gets the string date and returns the european format of the date as string. """
    # Getting day month and year separately
    date_found_ls = date_found.split('-')
    # Replacing list element [11, 20, 2022] -> [20, 11, 2022]
    temp = date_found_ls[0]
    date_found_ls[0] = date_found_ls[1]
    date_found_ls[1] = temp
    # European Style Date
    new_date = "-".join(date_found_ls)  # [11, 12, 2022] -> 11-12-2022
    newFileName = american_date_regex.sub(new_date, file)

    return newFileName


def rename_files(folder_name):
    # Now we will walk through our folder and find the dates in the filenames os.walk returns all files as list of strings please note string
    for foldername, subfolders, files in os.walk(folder_name):
        for file in files:
            # Get the date from the filename
            date_found = find_date(file)
            # Convert date to another format and get new file name
            new_file_name = get_new_file_name(date_found, file)
            # Renaming the Files.
            shutil.move(f"{folder_name}/{file}", f"{folder_name}/{new_file_name}")

