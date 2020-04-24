import numpy as np
import pandas as pd
df = pd.read_csv('remove.csv', header=None)
val = np.array(df.values)
out = ""
for i in val:
    out += str(i[0]) + ", "
out_file = open("remove_list.csv", "w")
out_file.write(out)
out_file.close()