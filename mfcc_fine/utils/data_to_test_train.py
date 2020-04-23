# from sklearn.model_selection import train_test_split
# import pandas as pd
import numpy as np

def data_to_test_train(input_file = "outputs/label_out.csv",
                       train_out = "outputs/train_out.csv",
                       test_out = "outputs/test_out.csv",
                       test_ratio = 0.2,
                       verbose=False):
    # input_file = "data/label_out.csv"
    # df = pd.read_csv(data_file, sep=",")
    data = np.genfromtxt(input_file, delimiter=',',skip_header=True)
    n = data.shape[0]
    if verbose: print(data.shape)
    # n=10
    if verbose:print(n)
    # test_ratio = 0.2
    test_size = int(n * test_ratio)
    audio_unique, count_unique = np.unique(data[:,0],return_counts=True)
    # audio_train = audio_unique[:int(audio_unique.shape[0]/2)]
    # audio_test = audio_unique[int(audio_unique.shape[0]/2):]
    test_len = 0
    test = []
    test_n = []
    tmp_audio_uniq = np.arange(audio_unique.shape[0])
    while(test_len<test_size):
        n = int(np.random.choice(tmp_audio_uniq, size=1,replace=False))
        test.append(audio_unique[n])
        test_len+=count_unique[n]
        test_n.append(int(n))
        # if verbose: print(test, test_len, np.sum(np.isin(data[:0],test)))
    diff = test_len-test_size
    # print(count_unique[test_n])
    closest = np.argmin(np.abs(count_unique[test_n]-diff))
    # print(closest, test_n[int(closest)], diff, count_unique[test_n[int(closest)]])
    # print(test_len, test_size)
    # print(test, np.sum(count_unique[test_n]))
    # print(audio_unique.shape, audio_unique)

    # np.random.shuffle(data)
    test = data[np.isin(data[:,0], test)]
    train = data[np.isin(data[:,0], test, invert=True)]
    np.savetxt(train_out, train, delimiter=",", header="audio,1,2,3,4,5,6,7,8,9,10,11,12,13,lbl", comments="")
    np.savetxt(test_out, test, delimiter=",", header="audio,1,2,3,4,5,6,7,8,9,10,11,12,13,lbl", comments="")
    if verbose:print(train.shape, test.shape)

if __name__ == '__main__':
    data_to_test_train(label_file = "../outputs/label_out.csv",
                       train_out = "../outputs/train_data.csv",
                       test_out = "../outputs/test_out.csv")