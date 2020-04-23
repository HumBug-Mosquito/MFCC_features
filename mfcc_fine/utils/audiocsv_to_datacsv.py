import librosa
import librosa.display
import pandas as pd
import numpy as np
import time
import glob

def audiocsv_to_datacsv(audio_root = "outputs/audio_csv/",
                        label_file = 'inputs/label.csv',
                        out_file = "outputs/label_out.csv",
                        winSize = 0.1,
                        numBins = 13,
                        verbose = False
                        ):
    # audio_root = "mozz/audio_csv/"
    # data_root = "mozz/data_csv/"
    # label_file = "mozz/label.csv"
    # out_file = "mozz/label_mfcc_by_audio.csv"

    # winSize = 0.1
    # numBins = 13

    lines = []
    with open(label_file,"r") as txt:
        line = txt.readline()
        while(line):
            lines.append(line.replace("\n",""))
            line = txt.readline()

    yes = []

    for line in lines:
        split = line.split(",")
        audio_id = int(split[1])
        try:
            start = int(np.floor(float(split[2]) * 10))
            end = int(np.ceil(float(split[3]) * 10))
            yes.append((audio_id,start,end))
            # print(audio_id, start, end)
        except ValueError:
            if verbose: print(line)

    pattern = audio_root + "*.csv"
    files = glob.glob(pattern)
    res = []
    count = 0
    start_time = time.time()
    for file in files:
        audio_num = int(file.replace("\\", "/").split("/")[-1][:-4])
        count += 1
        # start_time_read = time.time()
        data = pd.read_csv(file, sep=",",header=None).to_numpy(dtype = float, copy=True)
        data = data.squeeze()
        audio_id = int(file[len(pattern)-5:-4])
        # print(file, audio_id)
        # print("Time taken to read", time.time() - start_time_read)
        # start_time_mfcc = time.time()
        sr = int(data[0])
        hop_length = int(sr * winSize)
        data = data[1:]
        # print("SR", sr, "Length", data.__len__()/sr, "Hop_length", hop_length)
        mfcc = librosa.feature.mfcc(data, sr = sr, fmax = sr/2, n_mfcc=numBins, hop_length = hop_length, n_fft = hop_length*4)
        mfcc = np.swapaxes(mfcc, 0, 1)
        # print(mfcc.shape)
        # print("Time to MFCC", time.time() - start_time_mfcc)
        # print(df)
        out_len = mfcc.shape[0]
        yes_rel = [x for x in yes if x[0] == audio_id]
        out_label_num = np.zeros(out_len)
        for i in range(0, len(yes_rel)):
            for j in range(yes_rel[i][1], min(out_len, yes_rel[i][2])):
                out_label_num[j] = 1
        # print(out_label_num)
        # print (mfcc.shape, out_label_num.shape)
        # file_num =
        audio_prefix = np.ones((out_len,1))*audio_num
        out = np.hstack((audio_prefix,mfcc, out_label_num.reshape((out_len, 1))))
        if count==1:
            # print("RESET")
            res = np.copy(out)
        else:
            # if verbose: print(res.shape, out.shape)
            res = np.concatenate((res, out), axis=0)

        # print(res.shape)
        progress = count / files.__len__() * 100
        time_so_far = time.time() - start_time
        time_remain = time_so_far * (100 - progress) / progress
        if verbose: print(str(np.round(progress, decimals = 1))+"%", str(int(np.round(time_remain, decimals = 0))) + "s", audio_id)

    np.savetxt(out_file, res, delimiter=",", header="audio,1,2,3,4,5,6,7,8,9,10,11,12,13,lbl", comments="")

if __name__ == '__main__':
    audiocsv_to_datacsv(audio_root = "../inputs/audio_csv/",
                        label_file = '../inputs/label.csv',
                        out_file = "../inputs/label_out.csv")