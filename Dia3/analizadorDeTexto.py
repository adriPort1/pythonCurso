#5 funciones: 1 - cuantas veces aparece cada letra (3 letras)
#2 - cuantas palabras hay en total
#3 - primera y ultima letra
#4 - el texto enorden inverso
#5 - y si aparece la palabra python en el texto
from queue import PriorityQueue
from tokenize import String

texto = input("Escribe un texto: ").upper()
print("Escribe ahora tres letras a tu elección: ")
letra1 = input("1: ").upper()
letra2 = input("2: ").upper()
letra3 = input("3: ").upper()
print("Las letras pedidas aparecen: ")
print(letra1.lower()+": "+ str(texto.count(letra1))+ " veces ")
print(letra2.lower()+": "+ str(texto.count(letra2))+ " veces ")
print(letra3.lower()+": "+ str(texto.count(letra3))+ " veces ")
lista = texto.split()
print("Hay "+str(len(lista))+ " palabras, la primera letra es "+texto[0].lower()+" y la ultima es "+texto[-1].lower())
lista.reverse()
print(lista)
print(lista.__contains__("PYTHON"))
#solucion de el ---------------------------------------------------------------------------------------------------
texto2 = input("Ingresa un texto a eleccion: ")
letras =[]
texto2 = texto2.lower()
letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())
print("\n")
print("Cantidad de letras")
cantidad_letras1 = texto.count((letras[0]))
cantidad_letras2 = texto.count((letras[1]))
cantidad_letras3 = texto.count((letras[2]))
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")
print("\n")
print("Cantidad de palabras")
palabras2 = texto2.split()
print(f"Hemps encontrado {len(palabras2)} palabras en tu texto")
print("letras de inicio y fin")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es {letra_inicio} y la letra final es {letra_final}")
print("texto al reves")
palabras2.reverse()
texto_invertido = " ".join(palabras2)
print(f"Tu texto al reves es: '{texto_invertido}'")
print("buscando python")
busca_python = "python" in texto2
dic = {True:"si", False:"NO"}
print(f"La palabra 'Python {dic} aparece en el texto" )
