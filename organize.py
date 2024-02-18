import os
import shutil

def organize_downloads_folder(downloads_folder):
    # Dictionary to map file extensions to folder names
    folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".csv", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Music": [".mp3", ".wav", ".flac", ".aac"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Executables": [".exe", ".msi"],
        "Programs": [".deb", ".dmg", ".apk", ".appimage", ".rpm"],
        "Others": []  # Default folder for other file types
    }

    # Create folders if they don't exist
    for folder_name in folders:
        folder_path = os.path.join(downloads_folder, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Get list of files in the Downloads folder
    files = [f for f in os.listdir(downloads_folder) if os.path.isfile(os.path.join(downloads_folder, f))]

    # Organize files into respective folders
    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        moved = False
        for folder_name, extensions in folders.items():
            if file_extension in extensions:
                shutil.move(os.path.join(downloads_folder, file), os.path.join(downloads_folder, folder_name, file))
                moved = True
                break
        # If file doesn't match any category, move to 'Others' folder
        if not moved:
            shutil.move(os.path.join(downloads_folder, file), os.path.join(downloads_folder, 'Others', file))

if __name__ == "__main__":
    downloads_folder = os.path.expanduser("~/Downloads")  # Path to the Downloads folder
    downloads_folder = os.path.expanduser("~/Desktop")  # Path to the Downloads folder
    organize_downloads_folder(downloads_folder)
    print("Downloads and Desktop folders organized successfully.")
