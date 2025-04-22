from random import *
# pedida de nombre
nombre = input("Dime como te llamas: ")
print("Hola "+nombre+ " he pensado un numero del 1 al 100, adivinas cual es? tienes 8 intentos!")
#creacion de numero random
num = randint(1,100)
#variable para contar nombres, la variable interruptor e inicializacion de numero
contadorErrores = 0
interruptor = False
numero = 0
# loop con interruptor en falso, cuando se da que aciertan o el contador llega a 8, devuelve verdadero y finaliza
while interruptor == False:
    numero = int(input("Dime un numero: "))
# condicion para que se cumplan los numeros en menor y mayor
    if numero > 100 or numero <1:
        print("Ese numero no esta permitido, tienes un fallo más")
# pista cuando el numero que se introduce es mas bajo
    elif numero < num:
        print("No es ese numero, es más alto")
# pista cuando el numero que se introduce es mas alto
    elif numero > num:
        print("no es ese numero, es más bajo")
# cuando el numero se acierta
    else:
        print("Ese es el numero! tuviste "+str(contadorErrores)+" errores!")
        interruptor=True
    contadorErrores = contadorErrores+1
# cuando no se acertó en 8 inentos, pasa por aqui para acabar
    if contadorErrores == 8:
        print("Fallaste! más suerte otra vez, tuviste "+ str(contadorErrores) +" errores!")
        interruptor=True