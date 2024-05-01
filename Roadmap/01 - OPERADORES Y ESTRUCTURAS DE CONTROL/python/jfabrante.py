"""
Operadores
"""

# operadores aritméticos

sum = 10 + 3
print(sum)


print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"División: 10 / 3 = {10 / 3}")
print(f"Módulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"División entera: 10 // 3 = {10 // 3}")

# Operadores de comparación

print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores lógicos

print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 13 or 5 - 2 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de asignación

my_number = 11 # asignación
print(my_number)
my_number += 1 # Suma y asiganación
print(my_number)
my_number -= 1 # resta y asiganción  
print(my_number)
my_number *= 2 # multiplicación y asignación
print(my_number)
my_number /= 2 #división y asignación
print(my_number)
my_number %= 2 # módulo y asignación
print(my_number)
my_number **= 5 # exponente y asignación
print(my_number)
my_number //= 1 # dividión entera y asiganación
print(my_number)

# Operadores de identidad

my_new_number = my_number
print(f"my_new_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia

print(f"'u' in 'mouredev' = {'u' in 'mouredev'}")
print(f"'b' not in 'mouredev' = {'b' not in 'mouredev'}")

# Operadores de bit

a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010 (2 en bits)
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")

"""
Estructuras de control
"""

# Condicionales

my_string = "Padilla"

if my_string == "Francisco":
    print("my_string es 'Francisco'")
elif my_string == "Padilla":
    print("my_string es 'Padilla'")
else:
    print("my_string no es 'Francisco' ni 'Padilla'")

# Iterativas

for i in range(11):
    print(i)

i = 0

while i <= 19:
    print(i)
    i += 1

# Manejo de excepciones

try:
    print(10 / 1)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")



