class Colibri:
    # Constructor
    def __init__(self, especie, color, edat):
        #Atributs
        self.especie = especie
        self.color = color
        self.edat = edat

    # Getters i Setters:
    # Getters
    def get_especie(self):
        return self.especie

    def get_color(self):
        return self.color

    def get_edat(self):
        return self.edat

    # Setters
    def set_especie(self, especie):
        self.especie = especie

    def set_color(self, color):
        self.color = color