from Correctivo import Correctivo
from Mantenimiento import Mantenimiento
class Maquina():
    def __init__(self,nombre:str):
        self.nombre = nombre
        self.mantenimientos:list[Mantenimiento] =[]

    def add_mantenimiento(self,mantenimiento:Mantenimiento):
        self.mantenimientos.append(mantenimiento)
    
    def suma_gastos(self)->float:
        suma = 0
        for m in self.mantenimientos:
            suma += m.gasto_total()
        return suma

    def cantidad_mantenimientos_caros(self)->int:
        cont_caros = 0
        for m in self.mantenimientos:
            if m.gasto_total() > 10000:
                cont_caros+=1
        return cont_caros

    def rotura_mas_larga(self) -> Correctivo:
        if self.mantenimientos == []:return None
        
        mas_larga = 0
        man : Correctivo | None = None
        for m in self.mantenimientos:
            if isinstance(m,Correctivo) and m.horas_parada > mas_larga:
                mas_larga = m.horas_parada
                man = m
        return man

    def __str__(self):
        mants = ""
        for m in self.mantenimientos:
            mants = mants + str(m)
        return f"{self.nombre}, {mants}"
