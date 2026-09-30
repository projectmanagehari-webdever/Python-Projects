# 📅 US to European Date Format Converter

A Python automation project that works with files and folders, finds dates in files, and converts dates from **US format (`MM-DD-YYYY`) to European format (`DD-MM-YYYY`)**.

The project demonstrates practical Python concepts such as file handling, date manipulation, folder management, and modular programming.

## 📌 Project Overview

![Project Explanation](/Images/explain_image.png)

The project automates repetitive date-formatting tasks by working with files, locating dates, converting their format, and organizing the resulting files.

## ✨ Features

- 📁 Create folders programmatically.
- 📄 Create files using Python.
- 🔍 Find dates inside files.
- 🔄 Convert dates from US format to European format.
- 🗂️ Collect and organize files in a dedicated folder.
- 🧩 Separate functionality into individual Python scripts.

## 🛠️ Technologies Used

- **Python 3**
- File and directory handling
- Date and string manipulation
- Python standard library
- Git and GitHub

## 📂 Project Structure

```text
Project 1 Dates changing/
│
├── File collection/
│   └── Stores files created or processed by the project
│
├── create_files.py
├── create_folder.py
├── find_date.py
├── main.py
├── swap_the_date.py
├── explain_image.png
├── README.md
└── .gitignore
```

## 📄 File Descriptions

| File / Folder       | Purpose                                                   |
| ------------------- | --------------------------------------------------------- |
| `main.py`           | Main entry point for running the project.                 |
| `create_folder.py`  | Creates the folders required by the project.              |
| `create_files.py`   | Creates files for the date-processing workflow.           |
| `find_date.py`      | Searches files for dates that need processing.            |
| `swap_the_date.py`  | Handles changing dates from US format to European format. |
| `File collection/`  | Stores files created or processed by the project.         |
| `explain_image.png` | Visual overview of the project workflow.                  |

## 🔄 Example: Date Conversion

**Before — US format (`MM-DD-YYYY`)**

```text
01-31-2025
```

**After — European format (`DD-MM-YYYY`)**

```text
31-01-2025
```

The conversion changes the order of the month and day while keeping the year unchanged.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd "Project 1 Dates changing"
```

### 3. Run the program

```bash
python main.py
```

Make sure Python 3 is installed on your system.

## 📚 What I Learned

- Working with files and directories in Python.
- Creating and organizing files programmatically.
- Searching for dates in file contents.
- Manipulating date strings and changing date formats.
- Structuring a project using multiple Python modules.
- Using Git and GitHub for version control.

## 🔮 Future Improvements

- Add error handling for invalid or unexpected date formats.
- Add automated tests for date conversion.
- Improve logging and user feedback.
- Support additional date formats.
- Improve the command-line interface.

## 👨‍💻 Author

**Harikrishna**

This project is part of my journey toward becoming a better Python developer through practical, hands-on projects.
