### strings ###

my_string = "mi string"
my_other_string = 'mi other string'

print(len(my_other_string))

print(my_string+" "+my_other_string)

my_new_line_string = "este es un string\ncon salto de linea"
print (my_new_line_string)

#\n salto de linea
#\t con tabulacion

my_scape_string = "\teste es un string \n escapado"
print (my_scape_string)


#formateo
name, surname , age= "jose", 'orellana', 40

print("mi nombre es {} , apellido {}  y edad {}".format(name,surname, age))
print("mi nombre es %s , apellido %s  y edad %d"%(name,surname, age))
print(f"mi nombre es {name} , apellido {surname}  y edad {age}")

#desempaquetado de caracteres
language = "python"
a,b ,c,d,e,f= language
print(a)
print(b)

#division
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[:3]
print(language_slice)

language_slice = language[-2]
print(language_slice)


#reverse 
reversed_language = language[::-1]
print(reversed_language)


#funciones
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.upper().isupper())

print(language.startswith("p"))

