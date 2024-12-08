import os

# Path to your directory containing images
directory_path = r"D:\fyp\AI-based-Adaptive-LMS\dataset\2023\OctNov-2023-12\images"

# Text to remove from the middle of filenames
text_to_remove = "Oct-Nov_12_2023_Q"

# Loop through all files in the directory
for filename in os.listdir(directory_path):
    # Check if the text to remove is in the filename and is an image
    if text_to_remove in filename and filename.lower().endswith(
        (".jpg", ".jpeg", ".png", ".gif", ".bmp")
    ):
        # Remove the specified text from the filename
        original_filename = filename.replace(text_to_remove, "")

        # Get the full path for old and new filenames
        old_filepath = os.path.join(directory_path, filename)
        new_filepath = os.path.join(directory_path, original_filename)

        # Rename the file
        os.rename(old_filepath, new_filepath)

print("Text removal completed!")
