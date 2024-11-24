import os

# Define the folder path
folder_path = r"AI-based-Adaptive-LMS\dataset/2020/OctNov-2020-12/images"

# Check if the folder exists
if os.path.exists(folder_path):
    # Iterate through all the files in the folder
    for file_name in os.listdir(folder_path):
        # Check if 'q' is in the file name
        if 'q' in file_name:
            # Create the new file name
            new_file_name = file_name.replace('q', '')
            # Get the full paths
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, new_file_name)
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {file_name} -> {new_file_name}")
else:
    print("Folder does not exist!")
