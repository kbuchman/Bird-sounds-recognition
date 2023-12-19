import numpy as np
import scipy as sc
def framing(signal, fs, win_len, win_hop):
    frame_length = win_len * fs
    frame_step = win_hop * fs 
    signal_length = len(signal)
    frames_overlap = frame_length - frame_step
    num_frames = np.abs(signal_length - frames_overlap) // np.abs(frame_length - frames_overlap)
    frame_list = []
    for i in range(num_frames):
        start = i * (frame_length - frame_step)
        frame_list.append(signal[start : start + frame_length])
    return frame_list

def signal_energy(frame_list):
    energy = []
    for frame in frame_list:
        power = sc.sum(frame * frame, 1) / frame.size
        energy.append(power * frame.size)
    return energy

def main():
    signal = []
    fs = 0
    win_len = 0
    win_hop = 0
    frame_list = []
    energy = []
    frame_list = framing(signal, fs, win_len, win_hop)
    energy = signal_energy(frame_list)
    std = np.stdev(energy)
    mean = np.mean(energy)
    return mean * std

if __name__ == "__main__":
    main()