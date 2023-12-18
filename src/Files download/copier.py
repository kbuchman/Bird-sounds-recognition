import os
import shutil

def copy_first_n_files(source_folder, destination_folder, n=20):
    os.makedirs(destination_folder, exist_ok=True)

    for folder in os.listdir(source_folder):
        folder_path = os.path.join(source_folder, folder)

        if os.path.isdir(folder_path):
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

            counter = 0
            for file_name in files:
                if counter >= n:
                    break

                source_file_path = os.path.join(folder_path, file_name)
                destination_file_path = os.path.join(destination_folder, folder, file_name)

                os.makedirs(os.path.join(destination_folder, folder), exist_ok=True)
                shutil.copy(source_file_path, destination_file_path)
                print(f"Copied: {source_file_path} to {destination_file_path}")

                counter += 1


def main():
    source_folder = "D:\Music\Birds sounds"
    destination_folder = "D:\Music\Birds sounds - small"

    copy_first_n_files(source_folder, destination_folder, n=20)


if __name__ == '__main__':
    main()
