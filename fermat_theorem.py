# Majid Qurashi - 220365

a = int(input("Enter a: "))
p = int(input("Enter prime number p: "))

result = pow(a, p - 1, p)

print("a^(p-1) mod p =", result)

if result == 1:
    print("Fermat's theorem verified")
else:
    print("Not verified")
