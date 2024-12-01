class Colibri:
    # Constructor
    def __init__(self, especie, color, edat, velocitat_vol, habitat):
        # Atributos
        self.especie = especie
        self.color = color
        self.edat = edat  
        self.velocitat_vol = velocitat_vol
        self.habitat = habitat

    # Getters i Setters:

    # Getter para la especie
    def get_especie(self):
        return self.especie
    
    # Setter para la especie
    def set_especie(self, especie):
        self.especie = especie
    
    # Getter para el color
    def get_color(self):
        return self.color
    
    # Setter para el color
    def set_color(self, color):
        self.color = color
    
    # Getter para la edad
    def get_edat(self):
        return self.edat
    
    # Setter para la edad
    def set_edat(self, edat):
        self.edat = edat
    
    # Getter para la velocidad de vuelo
    def get_velocitat_vol(self):
        return self.velocitat_vol
    
    # Setter para la velocidad de vuelo
    def set_velocitat_vol(self, velocitat_vol):
        self.velocitat_vol = velocitat_vol
    
    # Getter para el hábitat
    def get_habitat(self):
        return self.habitat
    
    # Setter para el hábitat
    def set_habitat(self, habitat):
        self.habitat = habitat