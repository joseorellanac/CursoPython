##listas

my_list = list()
my_other_list = []

print (type(my_list))
print (type(my_other_list))

print (len(my_list))


my_list = [35,40,12]
print (len(my_list))
print(my_list)

#my_list.append(34)
#print(my_list)


my_other_list = [35,1.77,"Jose", True]
print(my_other_list)

#my_other_list = [45]

print(my_other_list)

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])


print(my_other_list.count("Jose")) # cuenta el numero de ocurrencias en la lista

#desempacketar los elementos de la lista
age,altura, nombre, t = my_other_list
print(age)

##No recomendable
age,altura, nombre, t = my_other_list[0],my_other_list[1],my_other_list[2], my_other_list[3]
print(age)


#concatenar listas
print(my_list+my_other_list)

my_list.append(34) #agrega un elemento al final de la lista
print(my_list)


my_list.insert(1,"pepe") #agrega un elemento en el indice indicado
print(my_list)


my_list.remove("pepe") #eliminar el primer elemento indicado encontrado en la lista
print(my_list)


my_list.pop() #aelimina el ultimo elemento por defecto
print(my_list)

my_list.pop(2) #aelimina el elemento indicado por el indice
print(my_list)

del my_list[0] #elimina elemento por indice
print(my_list)

my_list.clear() #limpia la lista completa
print(my_list)

###otras funciones
#copy() copia una lista
# reverse() revierte los valores
#sort() ordena la lista