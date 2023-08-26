import os
import shutil

# Specify the directory where the files are located
source_directory = 'C:/Users/agalo/Downloads/bedrock-samples-main/resource_pack/ui/BedrockPack/animations'
output_directory = 'C:/Users/agalo/Desktop/renamed/animations'  # Main output directory

# Create the main output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Function to recursively traverse and rename files
def rename_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.startswith("animation."):
                source_path = os.path.join(root, filename)
                relative_path = os.path.relpath(source_path, source_directory)
                new_filename = filename.replace("animation.", "")
                output_subdirectory = os.path.join(output_directory, os.path.dirname(relative_path))
                
                # Create subdirectories under the main output directory
                os.makedirs(output_subdirectory, exist_ok=True)
                
                # Copy the original file to the subdirectory as a backup
                shutil.copy2(source_path, os.path.join(output_subdirectory, filename))
                
                # Rename the file in the source directory
                os.rename(source_path, os.path.join(root, new_filename))
                print(f"Renamed: {source_path} -> {os.path.join(root, new_filename)}")

# Call the function to start the renaming process
rename_files_in_directory(source_directory)
