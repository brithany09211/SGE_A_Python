#Imprimir els números parells i els imparells continguts en la següent llista. Utilitzar for: num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

num = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]

print("Parells:")
for i in num:
    if i % 2 == 0:
        print(f"{i}")

print("Imparells:")
for i in num:
    if i % 2 != 0:
        print(f"{i}")