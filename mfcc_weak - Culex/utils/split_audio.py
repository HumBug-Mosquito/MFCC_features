from pydub import AudioSegment
import glob

size = 60 * 1000
audio_folder_path = "../data_svm/audio_full/"
audio_sink_path = "../data_svm/audio/"

pattern = glob.glob(audio_folder_path+"*.wav")
count = 0
for file in pattern:
    file = file.replace("\\","/")
    id = file[len(audio_folder_path):-4]
    full_audio = AudioSegment.from_wav(file)
    t1 = 0
    audio_len = len(full_audio)
    subcount = 0
    print(id)
    while t1 < audio_len:
        new_path = audio_sink_path + str(count).rjust(4,'0') + "_" + str(id).rjust(5,"0") + "_" + str(subcount).rjust(2,'0') + ".wav"
        if t1 + size > audio_len:
            new_audio = full_audio[t1:]
        else:
            new_audio = full_audio[t1:t1 + size]
        new_audio.export(new_path, format="wav")
        t1 += size
        subcount += 1
        count+=1

# t1 = t1 * 1000 #Works in milliseconds
# t2 = t2 * 1000
# newAudio = AudioSegment.from_wav("oldSong.wav")
# newAudio = newAudio[t1:t2]
# newAudio.export('newSong.wav', format="wav") #Exports to a wav file in the current path.