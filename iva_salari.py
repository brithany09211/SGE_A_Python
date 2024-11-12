# Crear una variable amb el salari
salari = 50000

# Calcular l'IVA segons el salari
if salari < 15000:
    iva = 0  
elif salari < 30000:
    iva = 10  
elif salari < 60000:
    iva = 21  
else:
    iva = 0  # Opcional, si quieres manejar salarios mayores de 60,000

# Calcular l'IVA
iva_calculat = salari * iva / 100

# Calcular el salari amb IVA
salari_amb_iva = salari + iva_calculat

# Mostrar el resultat
print(f"Càlcul de l'IVA: {salari} * {iva}/100 = {iva_calculat}")
print(f"Salari amb IVA: {salari_amb_iva}")