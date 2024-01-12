from response_model import Response
import json
import os


folder_path = "src\Resources\Labels"
responses = []
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        responses.extend(Response.from_list(data))

print(responses)