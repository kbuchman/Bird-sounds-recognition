'''
A class that allows to download audio files from the API
'''

import requests
import wget
import os
from response_model import Response
import pandas as pd


class Downloader():
    def __init__(self, base_url: str, endpoint: str) -> None:
        self.base_url = base_url
        self.endpoint = endpoint

    def download_json(self, gen: str, sp: str):
        final_url = f"{self.base_url}{self.endpoint}query={gen}+{sp}+grp:birds"
        response = requests.get(final_url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to download data. Recived status code is" + 
                            f" {response.status_code}")
        
    def download_audio_from_response(self, response: Response, path: str = None):
        for recording in response.recordings:
            try:
                wget.download(recording.file, f'{path}{recording.file_name}')
            except:
                continue


def main():
    base_url = "https://xeno-canto.org"
    endpoint = "/api/2/recordings?"
    birds_df = pd.read_csv("src/Resources/birds_list.csv", header=None)
    path = "D:/Music/Birds sounds"
    
    downloader = Downloader(base_url, endpoint)
    for row in birds_df.itertuples():
        final_path = path + f"/{row[1]}/"
        if not os.path.exists(final_path):
            os.mkdir(final_path)
        else:
            continue

        try:
            response = Response.from_dict(downloader.download_json(row[2], row[3]))
            downloader.download_audio_from_response(response, path=final_path)
        except:
            continue


if __name__ == '__main__':
    main()

