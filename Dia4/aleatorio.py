from random import *
#si pones import y la libreria que quieras vas de 1 en 1
#si pones * importas todas las librerias de un golpe (randin, uniform...)

ra = randint(0,10)
print(ra)
ran = uniform(1,5)
print(round(ran,1))#el ,1 es para un decimal, si no pones nada se coloca el numero a entero
colores = ['azul','rojo','amarillo']
ra = choice(colores)
#choice parece para los strings
print(ra)
numeros = list(range(5,50,5))
#shuffle es com o barajar
shuffle(numeros)
print(numeros)
aleatorio = random()
print(aleatorio)
#------------------------- listas con nuevos metodos
palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)
print (lista)
#esto tambien puede ser asi

palabra2 = 'sifon'

lista2 = [letra2 for letra2 in palabra2]

print(lista2)
# a las listas de numeros se las puede operar de esta manera en caso de necesitar
listaNum = [n/2 for n in range(0,21,2)]
print(listaNum)
# tambien se puede alterar con if para n o meter todos los daots
listaNum2 = [n for n in range(0,21,2) if n*2>10 ]
print(listaNum2)
#con else la estructura cambia
listaNum2 = [n if n*2 > 10 else 'no' for n in range(0,21,2)]
print(listaNum2)

pies = [10,20,30,40,50]
metros = [n/3.81 for n in pies]
print(metros)
# ejemplo matchs, es swicht pero con alguna funcion mas
serie = "N-02"

if serie== "N-01":
    print("Samsungo")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")

match serie:
    case "N-01":
     print("Samsungo")
    case "N-02":
        print("Samsungo")
    case "N-03":
        print("Samsungo")

cliente ={'nombre':'Federico','edad':45,'ocupacion':'instructor'}
pelicula = {'titulo':'matrix','ficha_tecnica':{'protagonista':'keanu reeves','director':'lana y nlilly wachowski',}}
elementos = [cliente,pelicula,'libro']
for e in elementos:
    match e:
        case {'nombre':nombre,'edad':edad,'ocupacion':ocupacion}:
            print("es un cliente")
            print(nombre,edad,ocupacion)
        case {'titulo':titulo,'ficha_tecnica':{'protagonista':protagonista,'director':director}}:
            print("es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("nose que es esto")