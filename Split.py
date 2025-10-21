import os
import shutil

# === CONFIG ===
image_folders = ["C:\\Users\\anavn\\Downloads\\SVRDD_YOLO\\Xicheng\\images", "C:\\Users\\anavn\\Downloads\\SVRDD_YOLO\\Haidian\\images", "C:\\Users\\anavn\\Downloads\\SVRDD_YOLO\\Fengtai\\images", "C:\\Users\\anavn\\Downloads\\SVRDD_YOLO\\Dongcheng\\images", "C:\\Users\\anavn\\Downloads\\SVRDD_YOLO\\Chaoyang\\images"]  # change if needed
label_folders = ["C:\\Users\\anavn\\Downloads\\SVRDD_YOLO\\Xicheng\\labels","C:\\Users\\anavn\\Downloads\\SVRDD_YOLO\\Haidian\\labels", "C:\\Users\\anavn\\Downloads\\SVRDD_YOLO\\Fengtai\\labels", "C:\\Users\\anavn\\Downloads\\SVRDD_YOLO\\Dongcheng\\labels", "C:\\Users\\anavn\\Downloads\\SVRDD_YOLO\\Chaoyang\\labels"]
split_files = {
    'train': "C:\\Users\\anavn\\Downloads\\SVRDD_YOLO\\train.txt",
    'val': "C:\\Users\\anavn\\Downloads\\SVRDD_YOLO\\val.txt",
    'test': "C:\\Users\\anavn\\Downloads\\SVRDD_YOLO\\test.txt"
}



# === UTILITY: Find matching file in multiple folders ===
def find_file(filename, folder_list):
    for folder in folder_list:
        path = os.path.join(folder, filename)
        if os.path.exists(path):
            return path
    return None

# === MAKE OUTPUT FOLDERS ===
for split in split_files:
    os.makedirs(f"/images/{split}", exist_ok=True)
    os.makedirs(f"/labels/{split}", exist_ok=True)

# === PROCESS EACH SPLIT ===
for split, txt_file in split_files.items():
    with open(txt_file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    for line in lines:
        # Normalize path separators and extract filename
        img_filename = os.path.basename(line.replace('\\', '/'))
        label_filename = os.path.splitext(img_filename)[0] + ".txt"

        # Find files
        img_path = find_file(img_filename, image_folders)
        label_path = find_file(label_filename, label_folders)

        if img_path and label_path:
            shutil.copy(img_path, f"/images/{split}/{img_filename}")
            shutil.copy(label_path, f"/labels/{split}/{label_filename}")
        else:
            print(f"[WARNING] Missing: {img_filename} or {label_filename}")

