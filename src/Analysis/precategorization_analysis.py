import numpy as np
import time
from librosa import load
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# TODO:
# Add missing descriptions

# win_len and win_hop defined in ms
def framing(signal: list, fs: int, win_len: int, win_hop: int):
    frame_length = int((win_len * fs) / 1000)
    frame_step = int((win_hop * fs) / 1000)
    signal_length = len(signal)
    frames_overlap = frame_length - frame_step
    num_frames = int(np.abs(signal_length - frames_overlap) // np.abs(frame_length - frames_overlap))
    frame_list = []
    for i in range(num_frames):
        start = i * frame_step
        frame_list.append(signal[start : start + frame_length])
    return frame_list

def signal_energy(frame_list: list):
    energy = []
    for frame in frame_list:
        power = np.sum([i * i for i in frame]) / len(frame)
        energy.append(power * frame.size)
    return energy

def extract_std_signal_energy(path: str, win_len: int, win_hop: int):
    print(f"Extracting std energy from {path}...")

    try:
        signal, fs = load(path)
        frame_list = framing(signal, fs, win_len, win_hop)
        energy = signal_energy(frame_list)
        print(f"\033[32msucceded\033[37m")
        return np.std(energy)
    except:
        print(f"\033[31mfailed\033[37m")
        return 0


def main():
    signal, fs = load("D:\Music\Birds sounds\Bernikla kanadyjska\CanadaGoose3April2009DwingelderveldHolland2.mp3")
    win_lens = range(256, 4096, 256)
    win_hops = [i * .1 for i in range(1, 10)]
    
    x = []
    y = []
    val = []

    for win_len in win_lens:
        for win_hop in win_hops:
            start_time = time.time()

            frame_list = framing(signal, fs, win_len, round(win_hop * win_len))
            energy = signal_energy(frame_list)
            std = np.std(energy)

            end_time = time.time()

            x.append(win_len)
            y.append(win_hop * .1)
            val.append(end_time - start_time)

    data = {'Win_hop': x, 'Win_lenght': y, 'Std': val}
    df = pd.DataFrame(data)
    result = df.pivot(index='Win_hop', columns='Win_lenght', values='Std')

    sns.heatmap(result, annot=True, fmt="g", cmap='viridis')
    plt.title('Script speed')
    plt.xlabel('Win hop')
    plt.ylabel('Win lenght')
    plt.show()
    

if __name__ == "__main__":
    main()