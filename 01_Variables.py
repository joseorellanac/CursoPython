#variables

my_string_variable = "my string variable"
print(my_string_variable)


my_int_variable = 10
print(my_int_variable)


my_bool_variable = True
print(my_bool_variable)

#Print puede recibir varias variables como argumentos
print(my_string_variable, my_int_variable)

#funciones de string
print(len(my_string_variable))

# declarar variables en una sola linea
name, surname , alias, age= "jose", "orellana", "pepit0",35.2
print (name, surname, alias, age)
print (type(name), type(surname), type(alias), type(age))


#input
n = input("ingresar n")
o = input("ingresa 0")
print(n)
print(o)

#¿declarar variable y tipo?
#aunque se asigne otro valor de otro tipo siempre 
#qieda com el ultimo tipo asignado
address: str= "mi direccion"
address = 32
print(address)