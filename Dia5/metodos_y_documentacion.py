dic = {'clave1 ':100,'clave2':500}

a = dic.popitem()
print(a)
print(dic)
c= ',:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#'.lstrip(',:_#%')
print(c)
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")
print(frutas)
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
marcas_aisladas = marcas_smartphones.isdisjoint(marcas_tv)
print(marcas_smartphones)
print(marcas_tv)
print(marcas_aisladas)

#---------------------
palabra = "Python".upper()[::-1]
print(palabra)
#ejemplo 2 de palabra invertida
palabra2 = "Python".upper()
palabra2Invertida=''.join(reversed(palabra2))
print(palabra2Invertida)