# Majid Qurashi - 220365

p = 3
q = 11

n = p * q
e = 3
phi = (p - 1) * (q - 1)
d = 7

msg = int(input("Enter message: "))

cipher = pow(msg, e, n)
plain = pow(cipher, d, n)

print("Encrypted:", cipher)
print("Decrypted:", plain)
