from cotxe import Cotxe
from colibri import Colibri

# Instància objecte Cotxe (añadidos los parámetros 'any' y 'num_rodes' en cada instancia)
cotxe1 = Cotxe("Toyota", "Focus", "12345CBA", 2006, 4)
cotxe2 = Cotxe("Ford", "X5", "5678DEF", 2026, 4)
cotxe3 = Cotxe("BMW", "Sèrie 3", "123240BRI", 2012, 4)

# Instància objecte Colibri
colibri1 = Colibri("Colibrí Verd Esmaragda", "Verd intens", "13 anys", "80 km/h", "Bosques tropicales")
colibri2 = Colibri("Colibrí Rosat", "Rosa brillant", "2 anys", "100 km/h", "Selvas")
colibri3 = Colibri("Colibrí Blau", "Blau metàl·lic", "10 anys", "120 km/h", "Muntanyes")

# Mostrar tres getters de Cotxe
print("Marca:", cotxe1.get_marca())
print("Model:", cotxe2.get_model())
print("Matrícula:", cotxe3.get_matricula())

# Mostrar quatre getters de Colibrí
print("Espècie:", colibri1.get_especie())
print("Color:", colibri2.get_color())
print("Edat:", colibri3.get_edat())
print("Velocitat de vol:", colibri1.get_velocitat_vol())

# Modificar dos atributs de Cotxe a través dels setters
cotxe1.set_model("Ferrari")
cotxe2.set_matricula("1111ZZZ")

# Mostrar els atributs modificats de Cotxe a través dels getters
print("Nou model:", cotxe1.get_model())
print("Nova matrícula:", cotxe2.get_matricula())

# Modificar dos atributs de Colibrí a través dels setters
colibri1.set_especie("Colibrí Cora")
colibri2.set_color("Verd brillant")

# Mostrar els atributs modificats de Colibrí a través dels getters
print("Nova espècie:", colibri1.get_especie())
print("Nou color:", colibri2.get_color())