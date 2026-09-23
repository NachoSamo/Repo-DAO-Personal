from Carga import Carga
class Camion():
    DISPONIBLE = "disponible"
    REPARACION = "reparacion"
    VIAJE = "viaje"
    
    def __init__(self,patente:str,carga_maxima:float):
        self.patente = patente
        self.carga_maxima = carga_maxima
        self.estado = Camion.DISPONIBLE
        self.cargas:list[Carga] = []

    def cantidad_cargas(self)-> int:
        return len(self.cargas)

    def subir_carga(self,carga:Carga):
        if not isinstance(carga,Carga):
            raise TypeError

        if self.peso_cargas() + carga.peso() > self.carga_maxima: 
            raise ValueError
        
        self.cargas.append(carga)

    def bajar_carga(self,carga:Carga):
        if not isinstance(carga,Carga):
            raise ValueError
        if self.estado == Camion.REPARACION or self.estado == Camion.VIAJE:
            raise ValueError("Estado invalido para bajar carga")

        if carga not in self.cargas:
            raise ValueError("No existe esa carga")

        for c in self.cargas:
            if c == carga:
                    self.cargas.remove(c)

    def a_reparacion(self):
        if self.estado != Camion.REPARACION:
            self.estado = Camion.REPARACION

    def peso_cargas(self)->float:
        peso = 0
        for c in self.cargas:
            peso += c.peso()
        return peso

    def sale_reparado(self):
        self.estado = Camion.DISPONIBLE

    def en_viaje(self):
        self.estado = Camion.VIAJE

    def de_regreso(self):
        self.estado = Camion.DISPONIBLE

    def listo_para_salir(self)->bool:
        flag = False
        carga_admitida = self.carga_maxima * 0.75
        if self.estado == Camion.DISPONIBLE and self.peso_cargas() >= carga_admitida:
            flag = True
        return flag 

    def cargas_en_orden(self):
        cadena = ""
        for c in self.cargas:
            cadena += c.__str__()
        return cadena

    def __str__(self):
        return f"{self.patente}, {self.estado}"

