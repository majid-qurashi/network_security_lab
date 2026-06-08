# Majid Qurashi - 220365

def rail_fence_encrypt(text):
    even = text[::2]
    odd = text[1::2]
    return even + odd

text = input("Enter text: ")
print("Encrypted Text:", rail_fence_encrypt(text))
