from Carga import Carga
class Packing(Carga):
    
    def __init__(self,contenido:str,peso_por_caja:float,cantidad:int,peso_estructura:float):
        super().__init__(contenido)
        self.peso_por_caja = peso_por_caja
        self.cantidad = cantidad
        self.peso_estructura = peso_estructura

    def peso(self)->float:
        return self.peso_por_caja * self.cantidad + self.peso_estructura

    def __str__(self)->str:
        return f"{self.contenido}, {self.peso():.2f}, {self.cantidad}"