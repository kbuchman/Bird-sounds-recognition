import os
import librosa

def calculate_average_length(audio_files):
    total_length = sum([librosa.get_duration(y=audio) for audio in audio_files.values()])
    average_length = total_length / len(audio_files)
    return average_length

def analyze_audio_folder(folder_path):
    audio_files = {}
    contains_main = 0
    contains_other = 0

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.lower().endswith(".flac"):
            audio, _ = librosa.load(file_path, sr=None)
            audio_files[filename] = audio

            if "_main" in filename.lower():
                contains_main += 1
            elif "_other" in filename.lower():
                contains_other += 1

    average_length = calculate_average_length(audio_files)

    print(f"Number of audio files: {len(audio_files)}")
    print(f"Average length of audio files: {average_length} seconds")
    print(f"Number of files containing main bird's sound: {contains_main}")
    print(f"Number of files containing other birds' sound: {contains_other}")

if __name__ == "__main__":
    folder_path = "D:\Music\Birds sounds - train database"
    analyze_audio_folder(folder_path)
