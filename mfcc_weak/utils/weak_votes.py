import numpy as np
import pandas as pd
import time

def weak_votes(scheme = 0, in_file = 'outputs/all_coarse.csv', out_file = 'outputs/audio_info.csv', verbose = False):
    # scheme = 0 # 0 is ns -> 0.5, 1 is ns drop
    df = pd.read_csv(in_file, header=None)
    val = np.array(df.values)
    head = val[0]
    # print(head[26])
    val = val[1:]
    # print(val)
    audio_id_list = val[:,1].astype(int)
    audio_ids = np.unique(audio_id_list, return_counts= False)
    audio_info = np.zeros((audio_ids.shape[0], 7)) #id, parent, clip, yes, no, maybe, overall
    paths_list = val[:,]
    start = time.time()
    for i in range(0, audio_ids.__len__()):
        id = audio_ids[i]
        indexes = np.where(audio_id_list == id)[0]
        index = indexes[0]
        # print(index, indexes)
        parent = val[index, 18]
        name = val[index, 26]
        clip_start = name.find("clip") + 5
        clip_end = name.find(".wav", clip_start)
        clip = int(name[clip_start:clip_end])
        # print(parent, clip)
        yes = np.sum(val[indexes,15] == 'mosquito')
        no = np.sum(val[indexes,15] == 'background')
        maybe = np.sum(val[indexes,15] == 'not_sure')
        if yes + no + maybe == 0:
            print("0 error", id, val[index, 15])
            overall = 0
        else:
            if scheme == 0:
                overall = ((yes + 0.5*maybe)/(yes+no+maybe)>=0.5) * 1
            elif scheme == 1:
                overall = (yes/(yes+no)>=0.5) * 1
            else:
                overall = 0
        # print(name)
        # print(id, parent, clip, yes, no, maybe, overall)
        audio_info[i] = [id, parent, clip, yes, no, maybe, overall]
        n = i+1
        if i%1000 == 0 and verbose:
            print(np.around(n / len(audio_ids) * 100,2), np.around(time.time()-start,0),  np.around(((time.time()-start) / n * len(audio_ids)),0))

    np.savetxt(out_file, audio_info, delimiter = ',', fmt='%f')

if __name__ == '__main__':
    weak_votes(in_file = '../outputs/all_coarse.csv', out_file = '../outputs/audio_info.csv')