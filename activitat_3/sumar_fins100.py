#Sumar números fins a arribar a 100 amb while. Caldrà sumar els números que estan inclosos entre 0 i 100. El programa deixarà d’executar-se quan s’arribi al número 100.

suma = 0
num = 0

while num <= 100:
    suma += num
    num += 1

print(f"La suma ha arribat a 100. El resultat final és: {suma}")