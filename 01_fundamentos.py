# ********************* TIPOS DE DATOS *********************
print('String', type('String')) # Tipo 'str'
print(15, type(15)) # Tipo 'int'
print(1.3, type(1.3)) # Tipo 'float'
print(7 + 5j, type(7 + 5j)) # Tipo 'complejo'
print(True, type(True)) # Tipo 'bool'

# ********************* VARIABLES *********************
'''
Para declarar una variable se debe:
- Usar snake_case
- Solo basta con escribir el nombre de la variable seguido de un igual y el valor
    e.g edad = 25
- Es posible usar las palabras reservadas como nombre de variable pero habremos de añadir un guión bajo al inicio
    e.g _if = 'valor'
'''

first_name = 'Eduardo'
last_name = "Morales" # Se puede usar tanto comillas simples como comillas dobles para declarar un str
edad = 25
_if = 'valor para _if'

# Se puede hacer la impresión de variables a la vez en un solo print()
print(first_name, last_name, edad, _if) # Eduardo Morales 25 valor para _if

# ********************* PARSE ENTRE TIPOS DE DATOS *********************
number = 9
number_to_str = str(number) # int a str

str = '1.458'
str_to_float = float(str) # str a float

float = 3.141563
float_to_complex = complex(float) # float a complejo

print(number, type(number))
print(number_to_str, type(number_to_str))

print(str, type(str))
print(str_to_float, type(str_to_float))

print(float, type(float))
print(float_to_complex, type(float_to_complex))