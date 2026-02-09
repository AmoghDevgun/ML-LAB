import numpy as np

og_arr = np.arange(1, 13)
print("original array shape:", og_arr.shape)
print(og_arr)

reshaped_arr = og_arr.reshape(3, 4)
print("\nreshaped array shape:", reshaped_arr.shape)
print(reshaped_arr)

