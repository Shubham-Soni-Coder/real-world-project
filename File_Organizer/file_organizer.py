import os 
import shutil
from pathlib import Path

file_categories = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".rtf", ".odt", ".pptx", ".ppt", ".xlsx", ".xls", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm"],
    "Music": [".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a"],
    "Programming": [".py", ".java", ".cpp", ".c", ".js", ".html", ".css", ".php", ".rb", ".swift", ".cs", ".go"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".bat", ".sh", ".apk", ".app"],
    "Databases": [".sql", ".sqlite", ".db", ".mdb"],
    "Disk Images": [".iso", ".img", ".dmg"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Torrents": [".torrent"],
    "Others": []  # For uncategorized files
}
dic_keys = list(file_categories.keys())

def main(path,log_widget=None):
    Path(path).iterdir() # check if path exists
    errors = [] # save all errors

    files = list(os.listdir(path))


    if not files:
        if log_widget:
            log_widget.insert("end", "No files found in the selected directory.\n", "error")
        return
    for file in files:
        ext_file = Path(file).suffix.lower()
        destination_folder = "Others"  # Default to "Others" if no category matches
        for category,extension in file_categories.items():
            if ext_file in extension:
                destination_folder = category
                break # stop checking if file found
        # create folder if not exists    
        os.makedirs(destination_folder, exist_ok=True) 

        # move file to the folder
        try:
            shutil.move(file, destination_folder)
            if log_widget:
                log_widget.insert("end", f"Moved {file} to {destination_folder}\n" , "success")
        except PermissionError:
            errors.append(f"Permission denied: {file}. Skipping...") 
        except FileNotFoundError:
            errors.append(f"File not found: {file}. Skipping...")       
        except Exception as e:
            errors.append(f"Error moving file {file}: {e}. Skipping...")

    # Display errors in log_widget instead of pop-ups
    if log_widget and errors:
        log_widget.insert("end", "\n".join(errors) + "\n", "error")

    return len(errors)  # Return error count

if __name__ == "__main__":
    path = 'E://'
    main(path)
    print("Files organized successfully!")