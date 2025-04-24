from operator import truediv


def mi_funcion(nombre):
    '''
    funcion de ejemplo para saber comodefinirlas
    '''
    print("hola "+nombre)
mi_funcion("luis")
def saludar_persona(nombre):
    '''
    funcion para saludar a alguien
    '''
    print("hola "+nombre)
saludar_persona('mr. popo')
def multiplicar(num1,num2):
    return num1*num2
multiplicado= multiplicar(3,5)
print(multiplicado)
palabra = input("dime una palabra: ").upper()
print(palabra)


def chequear_3_cifras(numero):
    return numero in range(100,1000)
resultado= chequear_3_cifras(658)
print(resultado)

def chequear_3_cifras_multiple(lista):
#el aqui usa pass en el else para quqe le de none, yo aqui hubiera usado while y ya
#el enunciado era cuando encontrara 1 que cumpliera

    for n in lista:
        if n in range (100,1000):
            return True
        else:
            pass
    return False
resultado2 = chequear_3_cifras_multiple([55,99,6000])
print(resultado2)

def chequear_3_cifras_ver (lista):
    lista_3_cifras =[]
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras
resultado3 = chequear_3_cifras_ver([555,2,600])
print(resultado3)

def suma_menores(lista):
    suma_num=0
    for n in lista:
        if 0<n<1000:
            suma_num= suma_num+n
    return suma_num

menores = [50,-3,8000,50]
suma = suma_menores(menores)
print(suma)
def cantidad_pares(lista):
    cuenta_num=0
    for n in lista:
        if n%2==0:
            cuenta_num= cuenta_num+1
    return cuenta_num
numeros = [12,50,47,35,60]
pares = cantidad_pares(numeros)
print(pares)