#comisiones del 13% ventas totales
#preguntar nombre y cuanto han vendido ese mes

Nombre = input("Dime como te llamas: ")
Comision = float(input("¿Cuanto has vendido este mes?: "))
print("Hola "+ Nombre +" tu comisión es de " + str(Comision*0.13) + " €")
#solucion profe es con otra variable y usando la f para imprimir las variables
# print(f"Hola {Nombre}, tus comisiones de este mes osn de ${comision}")
#la variable intermedia es comision, y pide las ventas con variable numVentas