lista = ['a','b','c']
for i in lista:
    numero_letra = lista.index(i)+1
    print(f"Letra {numero_letra}: {i}")
lista2 = ['Pablo','Laura','Fede','Luis','Julia']
#----------------------------------------------------
for i in lista2:
    if i.startswith('L'):
        print(i)
    else:
        print('Nombre que no comienza con L')
#---------------------------------------------------
numeros = [1,2,3,4,5]
mi_valor = 0
for i in numeros:
    mi_valor = mi_valor+i
print(mi_valor)
#-----------------------------------------------------
for a,b in [[1,4],[3,4],[5,6]]:
    print(a)
    print(b)
#--------------------------------------------------------
dic = {'clavel':'a', 'clave2':'b', 'clave3':'c'}
for i in dic.items():
    print(i)
# con items ves todo sin metodo es solo clave1 ... y con v. valores se ve las letras
#-----------------------------------------------------------------------------------
monedas = 5
while monedas>0:
    print(f"Tengo {monedas} moneda/s")
    monedas=monedas-1
#------------------------------------------------------------------------------------
respuesta = 's'
while respuesta== 's':
    respuesta = input("¿Quieres seguir? (s/n): ").lower()
else:
    print("Gracias")
#ahora ejemplos con pass, continuar y break
#pass funciona como un espacio reservado, para poder ejecutar sin que entre al loop, guardando el
#espacio de me moria
#while letra =="s":
#   pass
#nombre = input("Tu nombre: ")
#while i in nombre:
#   if i == 'r':
#        break #si pones continue sigue en el loop saltando el if en este caso
#    print(i)
num = 50
while num >=0:
    if num % 5 == 0:
        print(num)
    num = num -1
