import os
import zipfile
from gdown import download_folder
import librosa
import soundfile as sf

#TODO:
# for each file:
    # check sampling
        # resample !!!!!


def convert_files(drive_link: str, zip_name: str):
    """
    Function downolads, unzips, resamples, normalizes and converts to .wav database from google drive 

    Args:
        drive_link (str): Link to google drive folder
        zip_name (str): Name of zip file form google drive folder
    """
    dataFolder = download_from_drive_unzip(drive_link, zip_name)
    for file in os.listdir(dataFolder):
        normalize_convert_to_wav(f"{dataFolder}\\{file}")
        os.remove(f"{dataFolder}\\{file}")
    pass


def download_from_drive_unzip(drive_link: str, zip_name: str) -> str:
    """
    Fucntion downolads a zip file from google drive, creats work folder "DataBase" and extracts files from zip file there

    Args:
        drive_link (str): Link to google drive folder, viewer premission must be turned on
        zip_name (str): Name of zip file that is downloaded from drive

    Returns:
        str: path to "DataBase" folder
    """
    dataFolder = os.getcwd() + "/DataBase"
    if not os.path.exists(dataFolder):
        os.mkdir(dataFolder)
        download_folder(drive_link, quiet=True, use_cookies=False, remaining_ok=True, output=dataFolder)
        with zipfile.ZipFile(dataFolder + zip_name) as zip_file:
            zip_file.extractall(dataFolder)
        os.remove(f"{dataFolder}\\{zip_name}")
    return dataFolder


def resample_convert(file: str):
    """
    Function resamples given audio file, normalizes it and converts to .wav 

    Args:
        file (str): audio file
    """
    # TODO
    # check sample rate
        # resample


def normalize_convert_to_wav(file: str, source_folder: str, destination_folder: str):
    """
    Function normalizes audio file and exports it to .flac format

    Args:
        file: audio file name
        source_folder: parent folder for the file
        destination_folder: new location for the file
    """
    try:
        audio, sr = librosa.load(os.path.join(source_folder, file))  
        normalized_audio = librosa.util.normalize(audio)

        os.makedirs(destination_folder, exist_ok=True)
        sf.write(os.path.join(destination_folder, f"{file[:-4]}.flac"), normalized_audio, sr, format="flac")

        print(f"File {file[:-4]} saved into {destination_folder}")
    except:
        print(f"\033[91mFile {file[:-4]} skipped\033[37m")
    
    
def load_file_to_array(path: str):
    """
    Function loads values of audio file

    Args:
        path (str): A path to file 

    Returns:
        signal (np.array): Values of signal
        fs (int): Signal sample rate
    """
    return sf.read(path)


def main():
    source_folder = "D:\Music\Birds sounds"
    destination_folder = "D:\Music\Birds sounds - normalized database"
    os.makedirs(destination_folder, exist_ok=True)

    for folder in os.listdir(source_folder):
        folder_path = os.path.join(source_folder, folder)

        if os.path.isdir(folder_path):
            _ = [normalize_convert_to_wav(f, folder_path, os.path.join(destination_folder, folder)) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            
        


if __name__ == '__main__':
    main()