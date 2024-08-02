import os
import random
import subprocess

folder_path = '/path/to/your/folder'

def pick_random_txt_file(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    if not files:
        print("No .txt files found in the specified folder.")
        return None
    selected_file = random.choice(files)
    return selected_file

def run_cat_on_file(file_path):
    try:
        result = subprocess.run(['cat', file_path], check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def main():
    selected_file = pick_random_txt_file(folder_path)
    if selected_file:
        file_path = os.path.join(folder_path, selected_file)
        print(f"Running 'cat' on: {file_path}")
        run_cat_on_file(file_path)

if __name__ == "__main__":
    main()
