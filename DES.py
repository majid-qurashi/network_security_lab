# Majid Qurashi - 220365

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

key = b'12345678'

cipher = DES.new(key, DES.MODE_ECB)

text = input("Enter text: ").encode()

encrypted = cipher.encrypt(pad(text, 8))

print("Encrypted:", encrypted.hex())
