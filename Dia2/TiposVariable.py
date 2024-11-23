#diccionarios (dic) tienen una clave (color) y otra de valor (rojo){}
#tuples parecids a las listas pero el orden no se puede modificar()
#sets {esta es como las listas pero con elementos que no se repiten}
nombre = "Adrian"
print(nombre)
MiNumero = 5+5.8
#si pones type () y la variable te dice que tipo es
print(MiNumero)
print(type(MiNumero))
edad = input("Dime tu edad: ")
edad = int(edad)
print(type(edad))
num1 = "7.5"
num2 = "10"
print(float(num1) + float(num2))
#formateo de cadenas, usando format print(" Mi auto es {} y de matricula{}.format(color_auto,matricula)")
#print(f"Mi auto es {color_auto} y de matricula {matricula}")
x = 21
y = 3
print(f"Mis numeros son {x} y {y}")
#o (se pueden poner en elorden que quieras, x,y o y,x
print("Mis numeros son {} y {}".format(x,y))
print(f"{x} dividido por {y} es igual a {x//y}")
print(f"{x} dividido por {y} es igual a {x/y}")
print(f"{x} modulo {y} es igual a {x%y}") #es modulo
print(f"{x} elevado a {y} es igual a {x**y}") #elevado
print(f"{x} raiz cuadrada es igual a {x**0.5}")
print(round(90/7))
valor = round(96.3333333333333333333,2)
print(valor)
num1 = round(13/2,0)
print(num1)