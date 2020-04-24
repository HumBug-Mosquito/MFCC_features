from utils.weak_votes import weak_votes as step1
from utils.build_label import build_label as step2
from utils.audio_to_csv import audio_to_csv as step3
from utils.audiocsv_to_datacsv import audiocsv_to_datacsv as step4
from utils.data_to_test_train import data_to_test_train as step5

verbose = True
print("Beginning data conversion")
# step1(verbose= verbose)
# print("Step 1 complete.")
step2(verbose= verbose)
print("Step 2 complete.")
# step3(verbose= verbose)
# print("Step 3 complete.")
# step4(verbose= verbose)
# print("Step 4 complete.")
# step5(verbose= verbose)
# print("Step 5 complete.")
