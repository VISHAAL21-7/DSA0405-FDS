from scipy import stats
import numpy as np

data = [10, 20, 30, 40, 50]
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data))
