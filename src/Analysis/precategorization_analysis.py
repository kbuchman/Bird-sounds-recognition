import numpy as np
import time
from librosa import load
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def framing(signal, fs, win_len, win_hop):
    frame_length = win_len
    frame_step = win_hop
    signal_length = len(signal)
    frames_overlap = frame_length - frame_step
    num_frames = np.abs(signal_length - frames_overlap) // np.abs(frame_length - frames_overlap)
    frame_list = []
    for i in range(num_frames):
        start = i * frame_step
        frame_list.append(signal[start : start + frame_length])
    return frame_list

def signal_energy(frame_list):
    energy = []
    for frame in frame_list:
        power = np.sum([i * i for i in frame]) / len(frame)
        energy.append(power * frame.size)
    return energy


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