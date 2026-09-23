from Carga import Carga
class Bidon(Carga):
    
    def __init__(self,contenido:str,capacidad:float,densidad:float):
        super().__init__(contenido)
        self.capacidad = capacidad
        self.densidad = densidad

    def peso(self)->float:
        return self.densidad * self.capacidad

    def __str__(self):
        return f"{self.capacidad}, {self.contenido}, {self.densidad}, {self.peso():.2f}"
    
