'''
A function that downloads, unzips, resamples converts to .wav and loads audio files as np.arrays for further usage
'''
import os
import zipfile
from gdown import download_folder
from pydub import AudioSegment, effects
import mutagen

#TODO:
# for each file:
    # check sampling
        # resample !!!!!
    # check length (what for? dunno, maybe useful)
    # save as converted file or load converted file as np.array


def load_files(drive_link: str, zip_name: str):
    dataFolder = download_from_drive_unzip(drive_link, zip_name)
    for file in os.listdir(dataFolder):
        convert_resample(f"{dataFolder}\\{file}")
    pass


def download_from_drive_unzip(drive_link: str, zip_name: str) -> str:
    dataFolder = os.getcwd() + "/DataBase"
    if not os.path.exists(dataFolder):
        os.mkdir(dataFolder)
        download_folder(drive_link, quiet=True, use_cookies=False, remaining_ok=True, output=dataFolder)
        with zipfile.ZipFile(dataFolder + zip_name) as zip_file:
            zip_file.extractall(dataFolder)
        os.remove(f"{dataFolder}\\{zip_name}")
    return dataFolder


def convert_resample(file: str):
    #TODO
        # ffmpeg does not work on my files, works on previous files from TM
    # check sample rate
        # resample
    audio_info = mutagen.File(file).info
    if not audio_info.sample_rate == 16000:
        print(audio_info.sample_rate)
    normalize_convert_to_wav(file)


def normalize_convert_to_wav(file: str):
    rawsound = AudioSegment.from_file(file, file[-3:])  
    normalizedsound = effects.normalize(rawsound)  
    normalizedsound.export(f"{file[:-4]}norm.wav", format="wav")
