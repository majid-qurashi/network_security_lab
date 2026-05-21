#2 XOR cipher

def xor_encrypt(text, key):
    encrypted = ""

    for char in text:
        encrypted += chr(ord(char) ^ key)

    return encrypted


message = input("Enter message: ")
key = int(input("Enter numeric key: "))

encrypted = xor_encrypt(message, key)
decrypted = xor_encrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
