from departamento import Departamento
from casa import Casa
class Inmobiliaria():
    def __init__(self):
        self.inmuebles = []

    def agregar(self,inmueble):
        self.inmuebles.append(inmueble)

    def suma_alquileres(self):
        total = 0
        for inmueble in self.inmuebles:
            total += inmueble.alquiler()
        return total 

    def cantidad_casas_premium(self):
        cont_premiun = 0
        for inmueble in self.inmuebles:
            if isinstance(inmueble,Casa) and inmueble.dormitorios > 2 and inmueble.superficie > 150 and inmueble.pileta == 1:
                cont_premiun += 1
        return cont_premiun

    def propietario_alquiler_mas_bajo(self):
        importe_mas_bajo = float('inf')
        propietario = None
        for inmueble in self.inmuebles:
            if isinstance(inmueble,Departamento):
                alquiler = inmueble.alquiler()
                if alquiler < importe_mas_bajo:
                    importe_mas_bajo = alquiler
                    propietario = inmueble.propietario
        return propietario
