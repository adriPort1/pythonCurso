#esta leccion empezo con comparadores (que ya se, ==, != <=... etc
# el y es and, o es or y hay not que es como decir qu eno se cumpla que y lo que siga
#if, elif, else ahora se notara la tabulacion
if 5==2:
    print("es correcto")
else:
    print("No es correcto")
mascota = "perro"
if mascota=="gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("tienes un perro")
else:
    print("No se que animal tienes")
edad = 16
nota = 9
if edad <18:
    print("Eres menor de edad")
    if nota >=7:
        print("aprobado")
    else:
        print("No aprobado")
else:
    print("eres adulto")

num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
        print(f"{num1} es mayor que {num2}")
elif num2 > num1:
        print(f"{num2} es mayor que {num1}")
elif num1 == num2:
        print(f"{num1} y {num2} son iguales")