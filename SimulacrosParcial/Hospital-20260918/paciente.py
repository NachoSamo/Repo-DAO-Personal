from numpy import str_
from multiprocessing.sharedctypes import Value
class Paciente():
    SINTOMAS = {1:"corazon",2:"pulmon",3:"otras"}
    def __init__(self, nombre:str,sintoma:int, habitual=False):
        self.nombre = nombre
        self.habitual = habitual
        if sintoma not in self.SINTOMAS:
            raise ValueError("No es un sintoma valido (es del 1 al 3)")
        self.sintoma = sintoma

    
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self,valor:str)-> None:
        self._nombre = valor
    
    @property
    def sintoma(self) -> int:
        return self._sintoma
    
    @sintoma.setter
    def sintoma(self,valor:int)-> None:
        if valor not in self.SINTOMAS:
            raise ValueError("No es un sintoma valido (es del 1 al 3)")
        self._sintoma = valor

    @property
    def habitual(self)-> bool:
        return self._habitual

    @habitual.setter
    def habitual(self,valor:bool) -> None:
        self._habitual = valor

    @property
    def parserSintoma(self)->str:
        return self.SINTOMAS[self.sintoma]

    def __str__(self)-> str:
        return f"{self.nombre},{self.parserSintoma},{self.habitual}"





    