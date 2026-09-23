from abc import abstractmethod
from abc import ABC
class Envio(ABC):
    def __init__(self,codigo:int,ciudad:str,peso:float,costo_base:float):
        self.codigo = codigo
        self.ciudad = ciudad
        self.peso = peso
        self.costo_base = costo_base

    @abstractmethod
    def importe_final(self):
        pass

class EnvioComun(Envio):
    def __init__(self,codigo:int,ciudad:str,peso:float,costo_base:float):
        super().__init__(codigo,ciudad,peso,costo_base)
    
    def importe_final(self):
        return self.costo_base

class EnvioExpress(Envio):
    def __init__(self,codigo:int,ciudad:str,peso:float,costo_base:float):
        super().__init__(codigo,ciudad,peso,costo_base)

    def importe_final(self):
        return self.costo_base * 1.3