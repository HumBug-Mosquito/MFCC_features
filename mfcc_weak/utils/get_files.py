import numpy as np
import pandas as pd
import time
import os
import shutil

input_file = "audio_info.csv"
df = pd.read_csv(input_file, header=None)
val = np.array(df.values)
parents = np.unique(val[:,1])
audio = np.array(pd.read_csv("audio.csv"))[1:]
for parent in parents:
    # print(parent)
    path = audio[np.argmax(audio[:,0]==parent), 1]
    dl_path = "../Data/PSQL/Data" + path
    # print(dl_path)
    new_path = "inputs/audio/" + str(int(parent)) + ".wav"
    shutil.copy(dl_path, new_path)
