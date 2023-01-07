import numpy as np

X = np.random.randint(4, 6, size=(10,3))
print(X)

arr, uniq_cnt = np.unique(X, axis=0, return_counts=True)
uniq_arr = arr[uniq_cnt==1]

print(arr)
print(uniq_cnt)
print(uniq_arr)

