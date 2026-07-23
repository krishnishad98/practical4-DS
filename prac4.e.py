import numpy as np

arr = np.array([12, 45, 23, 45, 19])
print("Array:", arr)

max_val = arr.max()
filtered = arr[arr == max_val]
print("Maximum Value(s):", filtered)
