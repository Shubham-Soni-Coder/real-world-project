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
        
        # document checker
        if ext_file in file_categories[dic_keys[0]]:     
            if not os.path.exists(dic_keys[0]):
                os.makedirs(dic_keys[0])
            shutil.move(file,dic_keys[0])
        # image checker
        if ext_file in file_categories[dic_keys[1]]:
            if not os.path.exists(dic_keys[1]):
                os.makedirs(dic_keys[1])
            shutil.move(file,dic_keys[1])
        # video checker
        if ext_file in file_categories[dic_keys[2]]:
            if not os.path.exists(dic_keys[2]):
                os.makedirs(dic_keys[2])
            shutil.move(file,dic_keys[2])
        # music checker
        if ext_file in file_categories[dic_keys[3]]:
            if not os.path.exists(dic_keys[3]):
                os.makedirs(dic_keys[3])
            shutil.move(file,dic_keys[3])
        # programming checker 
        if ext_file in file_categories[dic_keys[4]]:
            if not os.path.exists(dic_keys[4]):
                os.makedirs(dic_keys[4])
            shutil.move(file,dic_keys[4])
        # archive checker
        if ext_file in file_categories[dic_keys[5]]:
            if not os.path.exists(dic_keys[5]):
                os.makedirs(dic_keys[5])
            shutil.move(file,dic_keys[5])
        # executable checker
        if ext_file in file_categories[dic_keys[6]]:
            if not os.path.exists(dic_keys[6]):
                os.makedirs(dic_keys[6])
            shutil.move(file,dic_keys[6])
        # database checker
        if ext_file in file_categories[dic_keys[7]]:
            if not os.path.exists(dic_keys[7]):
                os.makedirs(dic_keys[7])
            shutil.move(file,dic_keys[7])
        # disk image checker
        if ext_file in file_categories[dic_keys[8]]:
            if not os.path.exists(dic_keys[8]):
                os.makedirs(dic_keys[8])
            shutil.move(file,dic_keys[8])
        # font checker
        if ext_file in file_categories[dic_keys[9]]:         
            if not os.path.exists(dic_keys[9]):
                os.makedirs(dic_keys[9])
            shutil.move(file,dic_keys[9])
        # torrent checker
        if ext_file in file_categories[dic_keys[10]]:
            if not os.path.exists(dic_keys[10]):
                os.makedirs(dic_keys[10])
            shutil.move(file,dic_keys[10])

    return("Files organized successfully!")

if __name__ == "__main__":
    file_organizer(path)
    print("Files organized successfully!")