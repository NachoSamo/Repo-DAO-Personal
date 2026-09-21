import random

numeros_one = set()
numeros_two = set()

for i in range(10):
    num_one = random.randint(1, 20)
    numeros_one.add(num_one)
    num_two = random.randint(1,20)
    numeros_two.add(num_two)

numeros_unidos = numeros_one.union(numeros_two)
print(f"Numeros unidos: {numeros_unidos}")
print(f"Cantidad de numeros unidos: {len(numeros_unidos)}")
numeros_interseccion = numeros_one.intersection(numeros_two)
print(f"Numeros en interseccion: {numeros_interseccion}")
print(f"Cantidad de numeros en interseccion: {len(numeros_interseccion)}")
numeros_diferencia = numeros_one.difference(numeros_two)
print(f"Numeros en diferencia: {numeros_diferencia}")
print(f"Cantidad de numeros en diferencia: {len(numeros_diferencia)}")
numeros_diferencia_simetrica = numeros_one.symmetric_difference(numeros_two)
print(f"Numeros en diferencia simetrica: {numeros_diferencia_simetrica}")
print(f"Cantidad de numeros en diferencia simetrica: {len(numeros_diferencia_simetrica)}")