import os
import shutil

# Specify the path to the Downloads folder
downloads_path = os.path.expanduser("~/Downloads")

# Create a dictionary to map extensions to target folders
extension_to_folder = {
    ".txt": "TextFiles",
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".zip": "Archives",
    ".dmg": "Installers",
    ".pkg": "Installers",
    ".doc": "Documents",
    ".docx": "Documents",
    ".xls": "Excels",
    ".xlsx": "Excels",
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".java": "JavaCodes",
    ".py": "PythonCodes",
    ".html": "HtmlCodes",
    ".css": "HtmlCodes",
    ".js": "HtmlCodes",
    ".mov": "Movies",
    ".heic": "Movies",
}

# Iterate over files in the Downloads folder
for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)
    if os.path.isfile(file_path):  # Process only files, not directories

        # Get the file extension
        _, extension = os.path.splitext(filename)

        # Check if the extension is mapped in the dictionary
        if extension.lower() in extension_to_folder:

            # Get the target folder name for the extension
            target_folder = extension_to_folder[extension.lower()]

            # Create the target folder if it doesn't exist
            target_folder_path = os.path.join(downloads_path, target_folder)
            os.makedirs(target_folder_path, exist_ok=True)

            # Move the file to the target folder
            new_file_path = os.path.join(target_folder_path, filename)
            shutil.move(file_path, new_file_path)

            print(f"Moved '{filename}' to '{target_folder}' folder.")
