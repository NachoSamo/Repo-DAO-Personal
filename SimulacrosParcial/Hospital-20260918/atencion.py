from abc import ABC, abstractmethod
from paciente import Paciente

class Atencion(ABC):
    FORMAS_COBRO = {1:"efectivo", 2:"tarjeta de credito"}
    def __init__(self,codigo:int,tipoDeCobro:int,):
        self.codigo = codigo
        if tipoDeCobro not in self.FORMAS_COBRO:
            raise ValueError("El tipo de cobro debe ser 1 o 0")
        self.tipoDeCobro = tipoDeCobro

    @property
    def codigo(self)->int:
        return self._codigo

    @codigo.setter
    def codigo(self,value:int)-> None:
        if value <= 0:
            raise ValueError("El codigo debe ser positivo")
        self._codigo = value

    @property
    def tipoDeCobro(self)->int:
        return self._tipoDeCobro
    
    @tipoDeCobro.setter
    def tipoDeCobro(self,value:int)->None:
        if value not in self.FORMAS_COBRO:
            raise ValueError("El tipo de cobro debe ser 1 o 0")
        self._tipoDeCobro = value

    @property
    def descripcion_cobro(self)->str:
        #Parseo el tipo de cobro para mostrar mejor en el toString()
        return self.FORMAS_COBRO[self._tipoDeCobro]

    def __str__(self)->str:
        return (
            f"Atención #{self.codigo} | "
            f"Cobro: {self.descripcion_cobro} | "
            f"Total a cobrar: ${self.importeACobrar():.2f}"
        )

    @abstractmethod
    def importeACobrar(self):
        pass

class AtencionFarmacia(Atencion):
    def __init__(self,codigo:int,tipoDeCobro:int,importeTotal:float,descuento:int):
        super().__init__(codigo ,tipoDeCobro)
        self.importeTotal = importeTotal
        self.descuento = descuento

    @property
    def importeTotal(self)->float:
        return self._importeTotal
    
    @property
    def descuento(self)->int:
        return self._descuento

    @importeTotal.setter
    def importeTotal(self,value:float)->None:
        if value < 0:
            raise ValueError("No puede ser neg")
        self._importeTotal = value

    @descuento.setter
    def descuento(self,value:int)->None:
        if value < 0:
            raise ValueError("No puede ser neg")
        self._descuento = value

    def importeACobrar(self):
        total = self.importeTotal - self.descuento
        if self.tipoDeCobro == 1:
            total *= 0.95
        else:
            total *= 1.3
        return total

    def __str__(self) -> str:
        return f"Atencion Farmacia {self.codigo} - Total a cobrar: ${self.importeACobrar():.2f}"



class AtencionMedica(Atencion):
    def __init__(self, codigo: int, tipoDeCobro: int, paciente: Paciente, importe: float):
        super().__init__(codigo, tipoDeCobro)
        self.paciente = paciente
        self.importe = importe

    @property
    def paciente(self) -> Paciente:
        return self._paciente

    @paciente.setter
    def paciente(self, valor: Paciente) -> None:
        self._paciente = valor

    @property
    def importe(self) -> float:
        return self._importe

    @importe.setter
    def importe(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("El importe no puede ser negativo")
        self._importe = valor

    @property
    def importe_consulta(self) -> float:
        """Alias para compatibilidad con importe."""
        return self._importe

    @importe_consulta.setter
    def importe_consulta(self, valor: float) -> None:
        self.importe = valor

    def esPacienteHabitual(self) -> bool:
        return self.paciente.habitual

    def importeACobrar(self):
        total = self.importe

        if self.esPacienteHabitual() == True:
            total *= 0.75

        if self.tipoDeCobro == 1:
            total *= 0.90
        else:
            total *= 1.20

        return total

    def __str__(self) -> str:
        return f"Atencion Medica {self.codigo} - Total a cobrar: ${self.importeACobrar():.2f}"

