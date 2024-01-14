from response_model import Response
import sys
import os
import json

utils_path = os.path.join(os.path.abspath(__file__) + r"/../../")
sys.path.append(utils_path)
from Utils.model_helpers import cross_validation
from Utils.audio_file_management import cut_audio
sys.path.remove(utils_path)


def get_labels():
    folder_path = "src\Resources\Labels"
    responses = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)

            responses.extend(Response.from_list(data))

    return responses

def create_train_database(responses):
    file_names = [response.file_upload[9:] for response in responses]
    cross_validation_indexes = cross_validation(file_names, 5)[0]

    audio_files_folder = "D:\Music\Birds sounds - test database"
    destination_folder_path = "D:\Music\Birds sounds - train database"

    for idx in cross_validation_indexes[0]:
        audio_file_path = os.path.join(audio_files_folder, file_names[idx])
        i = 0

        for result in responses[idx].annotations[0].result:
            audio_type = "_main" if result.value.labels[0] == "main bird's sound" else "_other"
            name = f"f{idx}_{i}" + audio_type + ".flac"
            destination_path = os.path.join(destination_folder_path, name)

            try:
                cut_audio(audio_file_path, destination_path, result.value.start, result.value.end)
            except:
                print(f"\033[91mExtracting labels from file {file_names[idx]} failed\033[37m")

            i += 1

