frase = """tres tristes tigres 
comen trigo 
en un trigal"""
print(frase)
#o con \n como ya se vio
print("tristes" in frase)
print("tristes" not in frase)
print(len(frase))
print("pene"*15)
#listas ----------------------------------------------------
lista = ["a","b","c"]
print(type(lista))
lista2 = ["hola",55,6.1]
print(lista2)
print(type(lista2))
print(len(lista2))
print(lista2[0:2])
print(lista+lista2)
lista2.append("mazorca")
print(lista2)
lista2.pop()#asi el ultimo elemento, sino lo que quieras borrar de la lista escibelo
print(lista2)
lista3  =  ["a","f","j","b","k"]
print(lista3)
lista3.sort()
print(lista3)
lista3.reverse()
print(lista3)