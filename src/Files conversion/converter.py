import os
import zipfile
from gdown import download_folder
from pydub import AudioSegment, effects
import soundfile as sf

#TODO:
# for each file:
    # check sampling
        # resample !!!!!


def convert_files_in_folder(folder_path: str):
    for folder in os.listdir(folder_path):
        for file in os.listdir(f"{folder_path}\\{folder}"):
            normalize_convert_to_wav(f"{folder_path}\\{folder}\\{file}")
            os.remove(f"{folder_path}\\{folder}\\{file}")


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
    #TODO
        # ffmpeg does not work on my files, works on previous files from TM
    # check sample rate
        # resample


def normalize_convert_to_wav(file: str):
    """
    Function normalizes audio file and exports it to .wav format

    Args:
        file (str): audio file
    """
    rawsound = AudioSegment.from_file(file, file[-4:])  
    normalizedsound = effects.normalize(rawsound)  
    normalizedsound.export(f"{file[:-5]}converted.wav", format="wav")
    
    
def load_file_to_array(path: str):
    """
    Fucntion loads values of audio file

    Args:
        path (str): A path to file 

    Returns:
        signal (np.array): Values of signal
        fs (int): Signal sample rate
        path (str): Path to loaded file
    """
    signal, fs = sf.read(path)
    return signal, fs, path