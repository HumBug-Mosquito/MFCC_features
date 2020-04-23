import glob
import numpy as np

label_csv_path = "../data_svm/label.csv"
audio_folder_path = "../data_svm/audio/"
label_out_path = "../data_svm/label/label.txt"

lines = []
with open(label_csv_path,"r") as txt:
    line = txt.readline()
    while(line):
        lines.append(line.replace("\n",""))
        line = txt.readline()

yes = []

for line in lines:
    split = line.split(",")
    audio_id = int(split[1])
    try:
        start = int(float(split[2]) * 10) // 1
        end = int(float(split[3]) * 10) // 1
        yes.append((audio_id,start,end))
        # print(audio_id, start, end)
    except ValueError:
        print(line)

pattern = glob.glob(audio_folder_path+"*.wav")

out = []
for file in pattern:
    file.replace("\\","/")
    audio_id = int(file[-12:-7])
    sub_id = int(file[-6:-4])
    # print(file, audio_id, sub_id)
    out_label_num = np.zeros(600)
    yes_rel = [x for x in yes if x[0] == audio_id]
    # print(len(yes_rel))
    start = sub_id * 600
    end = start + 600
    for i in range(0, len(yes_rel)):
        for j in range(yes_rel[i][1], min(end, yes_rel[i][2])):
            j_mod = j % 600
            out_label_num[j_mod] = 1
    out_label_string = ''.join([str(int(num))+" " for num in out_label_num])
    out.append(out_label_string)

with open(label_out_path, "w") as txt:
    for line in out:
        txt.write("%s\n"%line)
