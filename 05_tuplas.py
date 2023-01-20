### tuplas

my_tuple = ()
my_other_tuple = tuple()

my_tuple = (35,1.22, "Jose", "Orellana")
print(my_tuple) 
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Jose"))## cuenta cuantos elementos posee el valor indicado

print(my_tuple.index("Jose"))## retorna el indice del primer elemento que se indica


## la principal diferencia con una lista es que la tupla en inmutable
#no se pueden cambiar, agregar o eliminar sus elementos

# convert tuple a list

my_tuple = list(my_tuple)
print(type(my_tuple))

del my_tuple # elimina completamente el objeto tupla
