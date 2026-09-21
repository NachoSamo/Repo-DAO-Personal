from inmueble import Inmueble

class Casa(Inmueble):

    def __init__(self,codigo,propietario,superficie,importe_base,dormitorios,pileta):
        super().__init__(codigo,propietario,superficie,importe_base)
        self.dormitorios = dormitorios
        self.pileta = pileta

    def alquiler(self):
        importe_por_hab = self.dormitorios * 30000
        importe_por_pileta =  self.pileta * 100000
        total_alquiler = importe_por_hab + importe_por_pileta + self.importe_base
        return total_alquiler

