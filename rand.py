import sys;
import numpy as np;
import pandas as pd;

np.set_printoptions(threshold=sys.maxsize)
# replace the range, sample size with your custom numbers 
arr = np.array(np.random.choice(range(10000), 10000, replace=False)) 
print(arr)
DF = pd.DataFrame(arr)
DF.to_csv("temp.csv")



