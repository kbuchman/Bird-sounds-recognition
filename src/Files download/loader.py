'''
A function that downloads, unzips, resamples converts to .wav and loads audio files as np.arrays for further usage
'''
import os
import zipfile
from gdown import download_folder

#TODO:
# for each file:
    # check extension
        # convert to .wav
    # check sampling
        # resample
    # check length (what for? dunno, maybe useful)
    # normalize 
    # save as converted file or load converted file as np.array


def load_files():
    pass


def download_from_drive(drive_link: str, zip_name: str):
    dataFolder = os.getcwd() + "/DataBase"
    if not os.path.exists(dataFolder):
        os.mkdir(dataFolder)
        download_folder(drive_link, quiet=True, use_cookies=False, remaining_ok=True, output=dataFolder)
        with zipfile.ZipFile(dataFolder + zip_name) as zip_file:
            zip_file.extractall(dataFolder)
    pass


def unzip_to_workfolder():
    pass


def convert_resample():
    #TODO
    # check extension
    # check saple rate
    pass


def normalize():
    pass
