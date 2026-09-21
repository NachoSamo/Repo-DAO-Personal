operaciones = {
    "+" : lambda x,y: x+y,
    "-" : lambda x,y: x-y,
    "*" : lambda x,y: x*y,
    "/" : lambda x,y: x/y
}

while True:
    operation = input("Ingrese una operacion: ")
    partes = operation.split()
    if len(partes) != 3:
        print("Operacion invalida")
        continue

    if partes[0] not in operaciones:
        print("Operacion invalida")
        continue

    num1 = int(partes[1])
    num2 = int(partes[2])
    print("El resultado es: ", operaciones[partes[0]](num1, num2))
    

