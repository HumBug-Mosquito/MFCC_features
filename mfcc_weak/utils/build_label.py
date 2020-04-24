import numpy as np
import pandas as pd
import time
import os
import shutil

def build_label(input_file = "outputs/audio_info.csv", label_out = "inputs/label.csv", verbose=False):
    # input_file = "audio_info.csv"
    df = pd.read_csv(input_file, header=None)
    val = np.array(df.values)
    parents = np.unique(val[:,1])
    # audio = np.array(pd.read_csv("audio.csv"))[1:]
    count = 0
    # label_out = "inputs/label.csv"
    # print(len(parents))
    pc = val[:,1]*10000+val[:,2]
    out = []
    for parent in parents:
        n = np.max(val[:,2][val[:,1]==parent])
        # print(n)
        for i in range(0, int(n+1)):
            h = parent * 10000 + i
            m = np.where(pc == h)[0]
            if len(m)>0:
                if val[int(m[0]),6] == 1:
                    if i == 0:
                        tup = [int(count), int(parent),int(i), int(i+1)]
                        out.append(tup)
                        count += 1
                    else:
                        j = i + 1
                        h2 = parent * 10000 + j
                        m2 = np.where(pc==h)[0]
                        if len(m2) > 0:
                            if val[int(m2[0]),6] == 0:
                                continue
                        tup = [int(count), int(parent),int(i), int(i+1)]
                        out.append(tup)
                        count += 1
                    if i == n:
                        tup = [int(count), int(parent),int(i+1), int(i+2)]
                        out.append(tup)
                        count += 1
    np.savetxt(label_out, out, delimiter=',', fmt='%f')

if __name__ == '__main__':
    build_label(input_file="../outputs/audio_info.csv", label_out="../inputs/label.csv")
