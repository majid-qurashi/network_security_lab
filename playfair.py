# Majid Qurashi - 220365

def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key:
        if char not in used and char.isalpha():
            matrix.append(char)
            used.add(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

key = input("Enter key: ")
matrix = generate_matrix(key)

print("Playfair Matrix:")
for row in matrix:
    print(row)
