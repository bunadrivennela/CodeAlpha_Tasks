
import os
import shutil

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist!")
        return

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".aac"],
        "Python_Files": [".py"],
        "ZIP_Files": [".zip", ".rar", ".7z"]
    }

    organized_count = 0

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(file_name)[1].lower()
        destination_folder = "Others"

        for folder_name, extensions in file_types.items():
            if extension in extensions:
                destination_folder = folder_name
                break

        target_folder = os.path.join(folder_path, destination_folder)
        os.makedirs(target_folder, exist_ok=True)

        destination_path = os.path.join(target_folder, file_name)

        # Avoid overwriting files with the same name
        if os.path.exists(destination_path):
            print("Skipped duplicate:", file_name)
            continue

        shutil.move(file_path, destination_path)
        print("Moved:", file_name, "->", destination_folder)
        organized_count += 1

    print("\nFile organization completed!")
    print("Total files organized:", organized_count)


folder_path = input("Enter the folder path to organize: ").strip().strip('"')
organize_files(folder_path)
