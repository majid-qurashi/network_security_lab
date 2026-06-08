# Majid Qurashi - 220365

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'1234567890123456'

cipher = AES.new(key, AES.MODE_ECB)

text = input("Enter text: ").encode()

encrypted = cipher.encrypt(pad(text, 16))

print("Encrypted:", encrypted.hex())
