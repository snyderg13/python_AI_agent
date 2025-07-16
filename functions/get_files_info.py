import os

def get_files_info(working_directory, directory=None):
    full_path = os.path.join(working_directory, directory)
    if not os.path.exists(full_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    abs_path = os.path.abspath(full_path)
    print(f"abs_path = {abs_path}")