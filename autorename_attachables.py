import os
import re
import shutil

def get_unique_filename(path):
    base, ext = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = f"{base}_dupe{counter}{ext}"
        counter += 1
    return path

def rename_and_backup_files_recursive(root_directory, output_directory):
    pattern = r"^(.*?)(\.gmdl_\w*)?\.attachable\.json$"
    
    for root, _, files in os.walk(root_directory):
        for filename in files:
            match = re.match(pattern, filename)
            if match:
                base_filename = match.group(1)
                new_filename = base_filename + ".json"
                
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)
                
                if old_path == new_path:
                    continue
                
                if os.path.exists(new_path):
                    new_path = get_unique_filename(new_path)
                
                rel_path = os.path.relpath(root, root_directory)
                backup_folder = os.path.join(output_directory, rel_path, os.path.basename(root))  # Main folder in backup
                if not os.path.exists(backup_folder):
                    os.makedirs(backup_folder)
                
                backup_path = os.path.join(backup_folder, filename)
                
                shutil.copy2(old_path, backup_path)  # Create a backup
                os.rename(old_path, new_path)  # Rename the file
                
                print(f"Renamed: {filename} -> {new_filename}")
                print(f"Backup created at: {backup_path}")


if __name__ == "__main__":
    target_directory = "C:/Users/agalo/Downloads/bedrock-samples-main/resource_pack/ui/BedrockPack/attachables"  # Replace with your directory path
    output_directory = "C:/Users/agalo/Desktop/renamed/test"  # Replace with your output directory path
    
    for root, _, _ in os.walk(target_directory):
        rel_path = os.path.relpath(root, target_directory)
        os.makedirs(os.path.join(output_directory, rel_path), exist_ok=True)
    
    rename_and_backup_files_recursive(target_directory, output_directory)
