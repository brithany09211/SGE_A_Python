class Cotxe:
    # Constructor
    def __init__(self, marca, model, matricula, any, num_rodes):
        self.marca = marca
        self.model = model
        self.matricula = matricula
        self.any = any
        self.num_rodes = num_rodes

    # Getters i Setters:

    # Getter para la marca
    def get_marca(self):
        return self.marca
    
    # Setter para la marca
    def set_marca(self, marca):
        self.marca = marca
    
    # Getter para el modelo
    def get_model(self):
        return self.model 
    
    # Setter para el modelo
    def set_model(self, model):
        self.model = model
    
    # Getter para la matrícula
    def get_matricula(self):
        return self.matricula
    
    # Setter para la matrícula
    def set_matricula(self, matricula):
        self.matricula = matricula
    
    # Getter para el año
    def get_any(self):
        return self.any
    
    # Setter para el año
    def set_any(self, any):
        self.any = any
    
    # Getter para el num_rodes
    def get_num_rodes(self):
        return self.num_rodes
    
    # Setter para el num_rodes
    def set_num_rodes(self, num_rodes):
        self.num_rodes = num_rodes