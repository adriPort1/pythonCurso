mi_texto = "Esta es una prueba"
resultado = mi_texto.index("n")
print(resultado)
#arriba ejemplo para buscar substrings y abajo para decir que valor ocupa el indice entre corchetes
mi_texto2 = "Esta es una prueba"
resultado2 = mi_texto2[6]
print(resultado2)
#si buscas por letra cuidado, sensible a mayus
mi_texto3 = "Esta es una prueba"
resultado3 = mi_texto3.rindex("a")#este busca pero desde el final
print(resultado3)
#substrings
textos = "ABCDEFGHIJKLMNO"
fragmento = textos[2:5]
print(fragmento)
texto= "ABCDEFGHIJKLMNO"
fragmento2 = texto[2:10:4]
print(fragmento2)
#va saltando segun los numeros del ultimo factor, y si pones ::-1 lo pone al reves y segun el numero va saltando tambien