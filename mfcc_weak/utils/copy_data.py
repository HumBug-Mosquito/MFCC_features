import pyfastcopy
import shutil

audio_csv_path = "../data_svm/audio.csv"
label_csv_path = "../data_svm/label.csv"
PSQL_local_root = "C:/Humbug/Data/PSQL/"
dest_root = "../data_svm/audio_full/"

with open(audio_csv_path,"r") as txt:
    line = txt.readline()
    while(line):
        split = line.replace("\n","").split(",")
        id = split[0]
        path = split[1]
        fullpath = PSQL_local_root + path[3:]
        destpath = dest_root + str(id) + ".wav"
        print(fullpath,destpath)
        shutil.copy2(fullpath,destpath)
        line = txt.readline()




