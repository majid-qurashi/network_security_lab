# Majid Qurashi - 220365

from Crypto.Cipher import ARC4

key = b'secretkey'

cipher = ARC4.new(key)

text = input("Enter text: ").encode()

encrypted = cipher.encrypt(text)

print("Encrypted:", encrypted.hex())
