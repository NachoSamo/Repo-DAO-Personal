from atencion import AtencionMedica
from ast import List
from atencion import Atencion

class Hospital():
    def __init__(self,razonSocial:str):
        self.razonSocial = razonSocial
        self._atencionesRealizadas: list[Atencion] = []

    def addAtencion(self,Atencion):
        self._atencionesRealizadas.append(Atencion)

    @property
    def razonSocial(self)-> str:
        return self._razonSocial
    
    @razonSocial.setter
    def razonSocial(self,valor:str)->None:
        self._razonSocial = valor

    @property
    def atencionesRealizadas(self)->List:
        return list(self._atencionesRealizadas)
    
    def __str__(self) -> str:
        atenciones_str = ", ".join(str(a) for a in self.atencionesRealizadas)
        return f"Hospital: {self.razonSocial}, Atenciones: [{atenciones_str}]"

    
    def importe_total_atencion_consulta(self)->float:
        importe_total = 0.0
        for atencion in self.atencionesRealizadas:
            if isinstance(atencion, AtencionMedica):
                importe_total += atencion.importe
        return importe_total

    def importe_promedio_atenciones(self,Minimo:float,Maximo:float)->float:
        contador = 0
        suma = 0.0

        for atencion in self.atencionesRealizadas:
            if isinstance(atencion, AtencionMedica):
                importe = atencion.importeACobrar()
                if Minimo <= importe <= Maximo:
                    suma+=importe
                    contador+=1
        if contador == 0:
            return 0.0
        return suma/contador
         

    def codigo_primera_atencion_habitual(self)->int:
        for atencion in self.atencionesRealizadas:
            if isinstance(atencion, AtencionMedica) and atencion.esPacienteHabitual():
                return atencion.codigo
        return 0


    def atencionesMedicas(self)->list[AtencionMedica]:
        l:list[AtencionMedica]=[]
        for a in self.atencionesRealizadas:
            if isinstance(a,AtencionMedica):
                l.append(a)
        return l

