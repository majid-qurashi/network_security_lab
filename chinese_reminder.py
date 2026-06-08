# Majid Qurashi - 220365

from sympy.ntheory.modular import crt

mod = [3, 5, 7]
rem = [2, 3, 2]

result = crt(mod, rem)

print("Solution:", result[0])
