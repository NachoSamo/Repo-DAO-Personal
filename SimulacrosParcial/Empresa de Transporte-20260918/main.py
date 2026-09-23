from Packing import Packing
from Caja import Caja
from Bidon import Bidon
from Carga import Carga
from Camion import Camion

def cargar_bidones()->list[Bidon]:
    ls: list[Bidon] = []
    archivo = open("data/bidones.csv")
    archivo.readline()
    for linea in archivo:
        datos = linea.split(",")
        contenido = datos[0]
        capacidad = float(datos[1])
        densidad = float(datos[2])
        bidonx = Bidon(contenido,capacidad,densidad)
        ls.append(bidonx)
    return ls

def cargar_cajas()->list[Caja]:
    ls: list[Caja] = []
    archivo = open("data/cajas.csv")
    archivo.readline()
    for linea in archivo:
        datos = linea.split(",")
        contenido = datos[0]
        peso = float(datos[1])
        cajax= Caja(contenido,peso)
        ls.append(cajax)
    return ls

def cargar_packings()->list[Packing]:
    ls: list[Packing] = []
    archivo = open("data/packing.csv")
    archivo.readline()
    for linea in archivo:
        datos = linea.split(",")
        contenido= datos[0]
        peso_por_caja= float(datos[1])
        cantidad = int(datos[2])
        peso_estructura = float(datos[3])
        packingx= Packing(contenido,peso_por_caja,cantidad,peso_estructura)
        ls.append(packingx)
    return ls


def cargar_todas_las_cargas()->list[Carga]:
    ls:list[Carga] = []
    cajas = cargar_cajas()
    packings = cargar_packings()
    bidones = cargar_bidones()

    for c in cajas:
        ls.append(c)

    for p in packings:
        ls.append(p)
    
    for b in bidones:
        ls.append(b)

    return ls


def crear_camiones()->list[Camion]:
    ls: list[Camion] = []
    for i in range(0,3):
        q = i+100
        ls.append(Camion(f"AAA{i}",q))
    return ls

def distribuir_cargas(camiones:list[Camion], cargas:list[Carga]):
    for carga in cargas:
        for camion in camiones:
            try:
                camion.subir_carga(carga)
                break
            except ValueError:
                continue



def main():
    bidones = cargar_bidones()


if "__main__" == "__name__":
    main()