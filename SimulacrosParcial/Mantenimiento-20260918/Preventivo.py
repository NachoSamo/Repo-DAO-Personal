from Mantenimiento import Mantenimiento

class Preventivo(Mantenimiento):
    
    def __init__(self,operario:str,fecha:str,importe_repuestos:float,
                    importe_insumos:float,
                    resultado:int):
        super().__init__(operario,fecha,importe_repuestos)
        if not isinstance(resultado, int) or isinstance(resultado, bool):
            raise TypeError("El resultado debe ser un entero (1, 2 o 3)")
        if resultado not in (1, 2, 3):
            raise ValueError("El resultado debe ser 1, 2 o 3")
        self.importe_insumos = importe_insumos
        self.resultado = resultado

    def gasto_total(self)->float:
        return self.importe_repuestos + self.importe_insumos

    def __str__(self)-> str:
        cadena = f"Operario: {self.operario}, fecha: {self.fecha}, impRepuestos: {self.importe_repuestos}, {self.importe_insumos}, {self.resultado}, total: {self.gasto_total()}"
        return cadena