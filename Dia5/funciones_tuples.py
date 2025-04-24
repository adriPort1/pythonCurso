from random import shuffle
precios_cafe=[('capuchino',1.5),('expreso',1.2),('moka',1.9)]
for elemento in precios_cafe:
    print(elemento)
def cafe_mas_caro(lista_precios):
    precio_mayor=0
    cafe_mas_caro=''
    for cafe,precio in lista_precios:
        if precio>precio_mayor:
            precio_mayor=precio
            cafe_mas_caro=cafe
        else:
            pass
    return(cafe_mas_caro,precio_mayor)
print(cafe_mas_caro(precios_cafe))

#lista inicial
palitos = ['-','--','---','----']

#mezclar palitos
def mezclar(lista):
    shuffle(palitos)
    return lista
print(mezclar(palitos))
#pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento=input("Elige un numero del 1 al 4: ")
    return int(intento)
intento1 = probar_suerte()
print(intento1)
# comprobar intento
def chequear_intento(lista,intento):
    if lista[intento -1]== '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")
    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)
seleccion=probar_suerte()
chequear_intento(palitos_mezclados,seleccion)
