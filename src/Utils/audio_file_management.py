import soundfile as sf

def cut_audio(input_file_path: str, output_file_path: str, start_time: float, end_time: float):
    audio_data, sample_rate = sf.read(input_file_path)

    start_sample = int(start_time * sample_rate)
    end_sample = int(end_time * sample_rate)

    end_sample = min(end_sample, len(audio_data))

    cut_data = audio_data[start_sample : end_sample]

    sf.write(output_file_path, cut_data, sample_rate)

    print(f"Audio cut from {start_time} seconds to {end_time} seconds and saved to {output_file_path}")
