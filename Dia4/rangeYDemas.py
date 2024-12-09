for numero in range(5,20,3): #si pones 3, es para saltar cada tanto
    print(numero)
#--- Un ejercicio -----
mi_lista = []
for i in range(2500,2586):
    mi_lista.append(i)
print(mi_lista)

mi_lista2 = []
for i in range(3, 301,3):
    mi_lista2.append(i)
print(mi_lista2)
#--------------------------------------------------
suma_cuadrados = 0
for i in range(1,16):
    suma_cuadrados = suma_cuadrados + i**0.5
print(suma_cuadrados)
#---------- enumerador ----------------------
lista = ['a','b','c','d']
for i in  enumerate(lista):
    print(i)

mis_tuples = list(enumerate(lista))
print(mis_tuples)
#--------------------------- ejercicio enumerate
lista_nombres = [(0,"Marcos"), "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

lista_nombres2 = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres2):
    if (nombre[0]=="M"):
        print(indice)