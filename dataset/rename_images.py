import os

# Path to your directory containing images
directory_path = r"D:\fyp\AI-based-Adaptive-LMS\dataset\2023\MayJun-2023-11\images"

# Prefix to add before each image name (replacing slashes with underscores)
prefix = "May-June_11_2023_Q"

# Loop through all files in the directory
for filename in os.listdir(directory_path):
    # Check if the file is an image (you can customize the extensions as needed)
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
        # Create the new filename with the prefix
        new_filename = prefix + filename

        # Get the full path for old and new filenames
        old_filepath = os.path.join(directory_path, filename)
        new_filepath = os.path.join(directory_path, new_filename)

        # Rename the file
        os.rename(old_filepath, new_filepath)

print("Renaming completed!")
