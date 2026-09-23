from asyncio import sleep
from Carga import Carga

class Caja(Carga):

    def __init__(self,contenido:str,peso:float):
        super().__init__(contenido)
        self._peso = peso

    def peso(self)->float:
        return self._peso

    def __str__(self):
        return f"{self.contenido}, {self.peso():.2f}"