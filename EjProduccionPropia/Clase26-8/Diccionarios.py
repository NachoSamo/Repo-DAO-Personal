clientes = {1:"Juan", 2:"Maria", 3:"Pedro"}

for x in clientes.values():
    print(x)

for x in clientes.keys():
    print(x)

for x in clientes.keys():
    print(clientes[x])

for i in clientes.items():
    print(i)

print(f"-----------------------------------\n")

paises = {
    "AR": "Argentina",
    "BR": "Brasil",
    "COL": "Colombia"
}

donde = input("Donde naciste?: ")
while donde != "":
    if donde in paises:
        print(f"Naciste en: ", paises[donde])

    else:
        print(f"No tengo esa ubicacion en mi base de datos.")
     
    donde = input("Donde naciste?: ")


