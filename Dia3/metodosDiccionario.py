#diccionario (dic) ---
diccionario = {'c1':'valor1','c2':'valor2'} #la clave es c y valor donde pone valor
print(diccionario)
resultado = diccionario ['c1']
print(resultado)
cliente = {'nombre':'juan','apellido':'perez','peso':88,'talla':1.75}
consulta = (cliente['apellido'])
print(consulta)
dic ={'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c3']['s2'])
dic2 = {'c1':[1,2,3],'c2':[4,5,6]}
print(dic2['c2'][1])#en el ejemplo lo pide en mayus, se pone .upper, el lo hace con strings
dic3 ={1:'a',2:'b'}
print(dic3)
dic3[3]='c'
print(dic3)
dic3[2] = 'B'
print(dic3)
print(dic3.keys())
print(dic3.values())
print(dic3.items())
#Tupples -----------------------------------------
#son como listas inmutables (y son mas eficientes porque ocupan menos
mi_tupple = (1,2,3,4)
mi_tupple2= (1,2,(10,20),3)
#admiten varios valores
t = (1,2,3)
x,y,z=t
print(x,y,z)
t2= 1,2,3,1
print(t2.count(1))
print(t2.index(3))