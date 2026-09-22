from abc import abstractmethod
from abc import ABC
class Mantenimiento(ABC):

    def __init__(self,operario:str,fecha:str,importe_repuestos:float):
        self.operario = operario
        self.fecha = fecha
        self.importe_repuestos = importe_repuestos

    @abstractmethod
    def gasto_total(self) -> float:
        pass    
    