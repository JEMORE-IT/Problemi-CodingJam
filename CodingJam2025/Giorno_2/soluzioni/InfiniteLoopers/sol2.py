import numpy as np
import cv2

CONST = 1234567890123456789

img = cv2.imread("../../problema_2/white_rabbit.png", cv2.IMREAD_GRAYSCALE)
img = np.where(img == 255, 0, 1)
arr = np.zeros(img.shape[0], dtype=np.int64)
for idx, line in enumerate(img):
    num = np.array2string(line, separator="")[1:-1]
    arr[idx] = int(num, 2)

mod_arr = []

seq1 = "+"
mod_arr.append(arr[0] + CONST)
for idx, num in enumerate(arr[1:], start=1):
    mod_arr.append(num + CONST)
    distance_pos = np.max(mod_arr) - np.min(mod_arr)

    mod_arr[idx] = num - CONST
    distance_neg = np.max(mod_arr) - np.min(mod_arr)

    if distance_pos < distance_neg:
        mod_arr[idx] = num + CONST
        seq1 += "+"
    else:
        seq1 += "-"

distance1 = np.max(mod_arr) - np.min(mod_arr)

mod_arr = []

seq2 = "-"
mod_arr.append(arr[0] - CONST)
for idx, num in enumerate(arr[1:], start=1):
    mod_arr.append(num + CONST)
    distance_pos = np.max(mod_arr) - np.min(mod_arr)

    mod_arr[idx] = num - CONST
    distance_neg = np.max(mod_arr) - np.min(mod_arr)

    if distance_pos < distance_neg:
        mod_arr[idx] = num + CONST
        seq2 += "+"
    else:
        seq2 += "-"

distance2 = np.max(mod_arr) - np.min(mod_arr)

if distance1 < distance2:
    print(seq1)
else:
    print(seq2)
