import os

# Replace with your actual folder path
folder_path = "dataset-paper2/2019/OctNov-2019-22/images"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
        old_path = os.path.join(folder_path, filename)
        new_name = f"OctNov-2019-22_{filename}"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")
