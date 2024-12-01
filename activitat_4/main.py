from cotxe import Cotxe
from colibri import Colibri

# Instància objecte Cotxe
cotxe1 = Cotxe("Toyota", "Focus", "12345CBA")
cotxe2 = Cotxe("Ford", "X5", "5678DEF")
cotxe3 = Cotxe("BMW", "Serie 3", "123240BRI")

# Instància objecte Colibri
colibri1 = Colibri("Colibrí Verd Esmaragda", "Verd intens", "13 anys")
colibri2 = Colibri("Colibrí Rosat", "Rosa brillant", "2 anys")
colibri3 = Colibri("Colibrí Blau", "Blau metàl·lic", "10 anys")

# Mostrar tres getters de Cotxe
print("Marca:", cotxe1.get_marca())
print("Modelo:", cotxe2.get_modelo())
print("Matrícula:", cotxe3.get_matricula())

# Mostrar quatre getters de Colibrí
print("Espècie:", colibri1.get_especie())
print("Color:", colibri2.get_color())
print("Edat colibri 2:", colibri2.get_edat())
print("Edat colibri 3:", colibri3.get_edat())

# Modificar dos atributs de Cotxe a través dels setters
cotxe1.set_modelo("Ferrari")
cotxe2.set_matricula("1111ZZZ")

# Mostrar els atributs modificats a través dels getters
print("Nuevo modelo:", cotxe1.get_modelo())
print("Nueva matrícula:", cotxe2.get_matricula())

# Modificar dos atributs de Colibrí a través dels setters
colibri1.set_especie("Colibrí Cora")
colibri2.set_color("Verd brillant")

# Mostrar els atributs modificats a través dels getters
print("Nueva especie:", colibri1.get_especie())
print("Nuevo color:", colibri2.get_color())