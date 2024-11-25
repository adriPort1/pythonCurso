mi_set = set([1,2,3,4,5,6])
#tambien se puede escribir asi -> {1,2,3,4,5,6}
#los elementos son unicos e inmutables (no se pueden agregar listas ni diccionarios)
print(mi_set)
otro_set = {1,2,3,4,5,6,1,1,2,2}
print(otro_set)
otro2_set = {1,2,3,(1,2,3),4,5}
print(otro2_set)
#tupples si admite porque es inmutable
print(len(otro2_set))
print(2 in otro2_set)
s1 = {1,2,3}
s2={3,4,5}
s3 = s1.union(s2)
print(s3)
s1.add(4)
s1.remove(3)
s1.discard(6) #igual que remove pero cuando un elemento no esta simplemente pasa, no casca error
print(s1)
s1.pop()
sorteo = s1.pop() #elimina de forma aleatoria
print(sorteo)
#booleanos ----------------------------- (ya les conozco pero bueno)
