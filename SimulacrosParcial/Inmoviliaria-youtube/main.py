from inmobiliaria import Inmobiliaria
from casa import Casa
from departamento import Departamento

def main():
    inm1 = Inmobiliaria()
    archivo = open("inmuebles.csv")
    for linea in archivo:
        datos = linea.split(",")
        tipo = int(datos[0])
        codigo = int(datos[1])
        propietario = datos[2]
        importe_base = int(datos[3])
        superficie = int(datos[4])

        if tipo == 1:
            dormitorios = int(datos[5])
            pileta = int(datos[6]) == 1
            casa = Casa(codigo,propietario,superficie,importe_base,dormitorios,pileta)
            inm1.agregar(casa)
        else:
            expensas = int(datos[5])
            piso = int(datos[6])
            depto = Departamento(codigo,propietario,superficie,importe_base,expensas,piso)
            inm1.agregar(depto)
    archivo.close()

    print("1) Informe el total a recaudar en concepto de alquileres si todos los inmuebles se encuentran alquilados")
    print(f"Suma alquileres: ${inm1.suma_alquileres()}")

    print("2) Informe la cantidad de casas de más de 150 metros cuadrados, más de 2 dormitorios y que posean pileta.")
    print(f"Cantidad casas premium: {inm1.cantidad_casas_premium()}")

    print("3) Informe el nombre del propietario del departamento con el alquiler cuyo importe definitivo sea el más bajo.")
    print(f"Propietario con alquiler más bajo: {inm1.propietario_alquiler_mas_bajo()}")


if __name__ == "__main__":
    main()