# Majid Qurashi - 220365

p = 23
g = 5

a = 6
b = 15

A = pow(g, a, p)
B = pow(g, b, p)

key1 = pow(B, a, p)
key2 = pow(A, b, p)

print("Shared Key at A:", key1)
print("Shared Key at B:", key2)
