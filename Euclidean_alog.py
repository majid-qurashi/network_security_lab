# Majid Qurashi - 220365

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD =", gcd(a, b))
