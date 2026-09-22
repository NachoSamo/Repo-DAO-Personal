from inmueble import Inmueble

class Departamento(Inmueble):
    def __init__(self,codigo,propietario,superficie,importe_base,expensas,piso):
        super().__init__(codigo,propietario,superficie,importe_base)
        self.expensas = expensas
        self.piso = piso

    def alquiler(self):
        total = self.importe_base + self.expensas
        if self.piso < 3:
            total += 20000
        return total

    