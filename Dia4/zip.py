nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudad = ['lima','madrid','mexico']
combinados = list(zip(nombres,edades,ciudad))
# para imprimir el zip hay que ponerle en lista como arriba
#~si hay mas elementos en una lista que en otra, se imprimiran el numero de
# elementos de la lista mas baja, si hay 3 y 4, 3 por ejemplo
print(combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edades} edad y vive en {ciudad}")
# ejercicio almazenar los numeros en zip resuelto para ejemplo
espanol = "uno","dos","tres","cuatro","cinco"
portu = "um","dois","três","quatro","cinco"
ing = "one","two","three","four","five"
numeros = list(zip(espanol,portu,ing))
print (numeros)