from abc import ABC,abstractmethod
class Carga(ABC):

    def __init__(self,contenido:str):
        self.contenido = contenido

    @abstractmethod
    def peso():
        pass

    def __str__():
        pass