from precategorization_analysis import extract_std_signal_energy
import os
import shutil

def copy_files_based_on_std_energy(source_folder, destination_folder, n=200):
    print(f"\033[35mStart listing files in {source_folder}\033[37m")

    file_paths = []
    for folder in os.listdir(source_folder):
        folder_path = os.path.join(source_folder, folder)

        if os.path.isdir(folder_path):
            files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            file_paths.extend(files)
    
    print(f"Files in {source_folder}: {len(file_paths)}")
    print(f"\033[35mStart extracting std energy from signals...\033[37m")

    files_std_energy = {path: extract_std_signal_energy(path, 50, 25) for path in file_paths}

    print(f"\033[35mStart sorting accquired data...\033[37m")

    files_std_energy = dict(sorted(files_std_energy.items(), key=lambda item: item[1], reverse=True))

    files_to_copy = list(files_std_energy.keys())[: n]

    print(f"\033[35mStart coping selected {n} files into {destination_folder}...\033[37m")

    os.makedirs(destination_folder, exist_ok=True)

    for file in files_to_copy:
        shutil.copy(file, destination_folder)
        print(f"Copied: {file} to {destination_folder}")

    print("\033[35mFinished\033[37m")


def main():
    source_folder = "D:\Music\Birds sounds - normalized database"
    destination_folder = "D:\Music\Birds sounds - test database"

    copy_files_based_on_std_energy(source_folder, destination_folder, n=256)


if __name__ == '__main__':
    main()
