class Cotxe:
    # Constructor
    def __init__(self, marca, modelo, matricula):
        #Atributs
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula

    # Getters i Setters:
    # Getters
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_matricula(self):
        return self.matricula

    # Setters
    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_matricula(self, matricula):
        self.matricula = matricula