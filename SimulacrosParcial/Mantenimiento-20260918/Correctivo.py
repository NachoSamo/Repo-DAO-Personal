from Mantenimiento import Mantenimiento
class Correctivo(Mantenimiento):
    def __init__(self,operario:str,fecha:str,importe_repuestos:float,
                    horas_parada:int,
                    importe_tecnico:float):
        super().__init__(operario,fecha,importe_repuestos)
        self.horas_parada = horas_parada
        self.importe_tecnico = importe_tecnico

    def gasto_total(self)->float:
        return self.importe_repuestos + self.importe_tecnico

    def __str__(self)-> str:
        cadena = f"Operario: {self.operario}, fecha: {self.fecha} total: {self.gasto_total():2f}"
        return cadena