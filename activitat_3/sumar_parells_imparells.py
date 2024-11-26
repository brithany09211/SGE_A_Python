#Copiar exercici anterior i modificar-lo per a que mostri la suma dels números parells i la suma dels números imparells.

num = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]

parells = 0
imparells = 0

for i in num:
    if i % 2 == 0:
        parells += i
    else:
        imparells += i

print(f"La suma dels parells és: {parells}")
print(f"La suma dels imparells és: {imparells}")