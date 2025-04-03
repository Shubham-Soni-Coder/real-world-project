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
path = 'E://' 

def file_organizer(path):
    os.chdir(path)

    files = list(os.listdir(path))


    for file in files:
        ext_file = Path(file).suffix.lower()
        destion_folder = "others"
        for category,extension in file_categories.items():
            if ext_file in extension:
                destion_folder = category
                break # stop checking if file found
        # create folder if not exists    
        os.makedirs(destion_folder, exist_ok=True) 

        # move file to the folder
        try:
            shutil.move(file, destion_folder)
        except PermissionError:
            print(f"Permission denied: {file}. Skipping...") 
        except FileNotFoundError:
            print(f"File not found: {file}. Skipping...")       
        except Exception as e:
            print(f"Error moving file {file}: {e}. Skipping...")

    return "Files organized successfully!" 

if __name__ == "__main__":
    file_organizer(path)
    print("Files organized successfully!")