from utils.audio_to_csv import audio_to_csv as step1
from utils.audiocsv_to_datacsv import audiocsv_to_datacsv as step2
from utils.data_to_test_train import data_to_test_train as step3

verbose = True
print("Beginning data conversion")
# step1(verbose= verbose)
print("Step 1 complete.")
step2(verbose= verbose)
print("Step 2 complete.")
step3(verbose= verbose)
print("Step 3 complete.")
