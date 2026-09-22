from paciente import Paciente
from atencion import AtencionMedica, AtencionFarmacia
from hospital import Hospital
def aBooleano(texto:str)->bool:
    return str(texto).strip().lower() == "true"

def cargarPacientes() -> dict[int, Paciente]:
    archivo = open("data/pacientes.csv",encoding="utf-8")
    archivo.readline()
    p: dict[int, Paciente] = {}
    for linea in archivo:
        datos = linea.strip().split(",")
        codigo = int(datos[0])
        nombre = datos[1]
        sintoma = int(datos[2])
        habitual = aBooleano(datos[3])
        p[codigo]= Paciente(nombre,sintoma,habitual)

    archivo.close()
    return p

def cargarAtencionesMedicas(pacientes:dict[int, Paciente])->list[AtencionMedica]:
    archivo = open("data/atenciones_medicas.csv", encoding="utf-8")
    archivo.readline()
    medicas:list[AtencionMedica]=[]
    for linea in archivo:
        datos = linea.split(",")
        codigo = int(datos[0])
        tipo_cobro = int(datos[1])
        importe_consulta = float(datos[2])

        paciente = pacientes[codigo]
        atencion = AtencionMedica(codigo,tipo_cobro,paciente,importe_consulta)
        medicas.append(atencion)

    archivo.close()
    return medicas

def cargarAtencionesFarmacia()->list[AtencionFarmacia]:
    archivo = open("data/atenciones_farmacia.csv", encoding="utf-8")
    archivo.readline()
    f:list[AtencionFarmacia] = []
    for linea in archivo:
        datos = linea.split(",")
        codigo = int(datos[0])
        tipo_cobro = int(datos[1])
        importe_total = float(datos[2]) 
        cupon_descuento = float(datos[3])
        f.append(AtencionFarmacia(codigo,tipo_cobro,importe_total,cupon_descuento))
    archivo.close()
    return f

def cargarHospital()->Hospital:
    hospi = Hospital("SalvadorHospital")
    pacientes = cargarPacientes()
    atenciones_medicas = cargarAtencionesMedicas(pacientes)
    atenciones_farmacia = cargarAtencionesFarmacia()
    for am in atenciones_medicas:
        hospi.addAtencion(am)
    
    for af in atenciones_farmacia:
        hospi.addAtencion(af)
    return hospi

def main():
    dict_pacientes = cargarPacientes()
    lista_atenciones_medicas = cargarAtencionesMedicas(dict_pacientes)
    lista_atenciones_farmacia = cargarAtencionesFarmacia()



if __name__ == "__main__":
    main()
