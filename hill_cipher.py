# Majid Qurashi - 220365

import numpy as np

key = np.array([[3, 3],
                [2, 5]])

text = input("Enter 2-letter plaintext: ").upper()

P = [ord(text[0]) - 65, ord(text[1]) - 65]
C = np.dot(key, P) % 26

cipher = "".join(chr(int(x) + 65) for x in C)

print("Cipher Text:", cipher)
