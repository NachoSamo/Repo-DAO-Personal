from solucion import EnvioExpress
from solucion import EnvioComun
from solucion import Envio

def total_a_recaudar(envios:list[Envio])->float:
    a_recaudar = 0
    for e in envios:
        a_recaudar += e.importe_final()

    return a_recaudar


def cargar_envios(ruta:str)->list[Envio]:
    archivo = open( ruta, encoding="utf-8")
    archivo.readline()

    ls: list[Envio] = []

    for linea in archivo:
        datos = linea.split(",")
        tipo = int(datos[0])
        codigo = int(datos[1])
        ciudad = datos[2]
        peso = float(datos[3])
        costo_base = float(datos[4])

        if tipo == 1:
            comun = EnvioComun(codigo,ciudad,peso,costo_base)
            ls.append(comun)
        elif tipo == 2:
            exp  = EnvioExpress(codigo,ciudad,peso,costo_base)
            ls.append(exp)
        else:
            raise ValueError("No es un tipo envio valido")
    return ls

def con_peso_admitido(envios:list[Envio])->list[Envio]:
    ls:list[Envio] = []
    for e in envios:
        if e.peso > 10:
            ls.append(e)

    return ls

def diff_ciudades(envios:list[Envio])->list[str]:
    ciudades:list[str] = []
    for e in envios:
        ciudad = e.ciudad
        if ciudad not in ciudades:
            ciudades.append(ciudad)

    return ciudades

def main():
    envios = cargar_envios("datos/envios.csv")
    print(f"Se registraron {len(envios)} envios desde 'datos/envios.csv' ")
    recaudado = total_a_recaudar(envios)
    print(f"Se recaudarán: ${recaudado}")
    print(f"Cantidad con peso mayor a 10kg: {len(con_peso_admitido(envios))} envios")

    ciudades = diff_ciudades(envios)
    print("Las ciudades son:")
    for c in ciudades:
        print(c)
    

if __name__ == "__main__":
    main()
