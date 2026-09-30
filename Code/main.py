# what we have to do in this project?
# Write a python code to rename thousands of files with american style (MM-DD-YYYY) dates to european style (DD-MM-YYYY) date
# Let us break this down in Steps:
# Step 1: Create folder and inside it multiple files with american style dates.
# Step 2: Finding dates in the file names.
# Step 3: Replacing this dates with european style dates.


from create_folder import create_folder
from create_files import create_files
from swap_the_date import rename_files

# Folder name
folder_to_create = "File collection"
# Creating the folder
create_folder(folder_to_create)
# Creating all the files of the folder
create_files(folder_to_create)
# Then the final step of renaming the files.
rename_files(folder_to_create)





# To delete the whole directory with all files inside it
# (comment above code and change the folder name in rmtree() accordingly)
# import shutil
# shutil.rmtree("File collection")

