

from Maquina import Maquina
from Mantenimiento import Mantenimiento
from Correctivo import Correctivo
from Preventivo import Preventivo

def crear_mantenimiento(fila: list[str]) -> Mantenimiento:
    tipo_mantenimiento = int(fila[0])
    fecha = fila[1]
    operario = fila[2]
    importe_repuestos = float(fila[3])
    if tipo_mantenimiento == 1:
            resultado_mantenimiento = int(fila[4])
            importe_insumos = float(fila[5])
            return Preventivo(operario,fecha,importe_repuestos,importe_insumos,resultado_mantenimiento)
    elif tipo_mantenimiento == 2:
        horas_parada = int(fila[4]) 
        importe_tecnico = float(fila[5])
        return Correctivo(operario,fecha,importe_repuestos,horas_parada,importe_tecnico)
    else:
        raise ValueError(f"Tipo de mantenimiento inválido: {tipo_mantenimiento}")

def cargar_mantenimientos():
    mantenimientos:list[Mantenimiento] = []
    archivo = open("data/mantenimientos.csv",encoding="utf-8")

    for linea in archivo:
        dato = linea.split(",")
        tipo_mantenimiento = int(dato[0])
        fecha = dato[1]
        operario = dato[2]
        importe_repuestos = float(dato[3])
        if tipo_mantenimiento == 1:
            resultado_mantenimiento = int(dato[4])
            importe_insumos = float(dato[5])
            mantenimientos.append(Preventivo(operario,fecha,importe_repuestos,importe_insumos,resultado_mantenimiento))
        elif tipo_mantenimiento == 2:
            horas_parada = int(dato[4]) 
            importe_tecnico = float(dato[5])
            mantenimientos.append(Correctivo(operario,fecha,importe_repuestos,horas_parada,importe_tecnico))
        else:
            raise ValueError(f"Tipo de mantenimiento inválido: {tipo_mantenimiento}")

    archivo.close()
    return mantenimientos

def cargar_maquina():
    maquina = Maquina("Maquina Manufacturera")
    for m in cargar_mantenimientos():
        maquina.add_mantenimiento(m)

    return maquina


def main():
    mantenimientos = cargar_mantenimientos()


if "__main__" == "__name__":
    main()