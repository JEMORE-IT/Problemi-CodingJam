import string
from tqdm import tqdm
from itertools import product


def decipher(data, key):
    idx = 0
    msg = ""
    for b in data:
        msg += chr(b ^ ord(key[idx]))
        idx = (idx + 1) % len(key)
    return msg


with open("../../problema_3/cipher.bin", "rb") as f:
    data = f.read()

d = string.printable

for key in tqdm(list(product(d, repeat=3))):
    key = "".join(key)
    msg = decipher(data, key)
    if "Matrix" in msg:
        break

print(msg)
print("KEY:", key)
