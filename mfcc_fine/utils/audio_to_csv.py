import librosa
import librosa.display
import os
import numpy as np
import time
import glob

def audio_to_csv(pattern = "inputs/audio/*.wav", out_root = "outputs/audio_csv/", verbose=False):
    files = glob.glob(pattern)
    count = 0
    start_time = time.time()
    for file in files:
        count += 1
        audio_path = os.path.abspath(file)
        x , sr = librosa.load(audio_path, sr=None)
        x_sr = np.copy(x)
        x_sr = np.insert(x_sr, 0, sr)
        save_name = out_root + file[len(pattern)-5:-3] + "csv"
        progress = count / files.__len__() * 100
        time_so_far = time.time() - start_time
        time_remain = time_so_far * (100 - progress) / progress
        np.savetxt(save_name, x_sr, delimiter = ",")
        if verbose:print(str(np.round(progress, decimals = 1))+"%", str(int(np.round(time_remain, decimals = 0))) + "s", save_name)

if __name__ == '__main__':
    audio_to_csv(pattern = "../inputs/audio/*.wav", out_root="../outputs/audio_csv/")