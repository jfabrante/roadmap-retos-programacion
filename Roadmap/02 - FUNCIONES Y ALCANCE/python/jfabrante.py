"""
Funciones dedinidas por el usuario
"""

# Simple

def greet():
    print("Hola, Python")

greet()

# Con retorno

def return_greet():
    return "Hola, Python!"

greet = return_greet()
print(greet)
print(return_greet())

# Con un argumento

def arg_greet(name):
    print(f"Hola, {name}")

arg_greet("Fran")

# Con argumentos

def args_greet(greet, name):
    print(f"{greet}, {name}")

args_greet("Hi", "Fran")
args_greet(name = "Fran", greet = "Hi")

def default_arg_greet(name = "Python"):
    print(f"Hola, {name}")

default_arg_greet("Fran")
default_arg_greet()

# Con argumentos y return

def return_args_greet(greet, name):
    return f"{greet}, {name}"

print(return_args_greet("Hola", "Fran"))

# Con retorno de varios valores

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un número variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola", {name})

variable_arg_greet("Python", "Fran", "Padilla", "comunidad")

# Con un número variable de argumentos con palabra clave

def variable_key_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_key_greet(
    languaje = "Python",
    name = "Fran",
    alias = "Padilla",
    age = 36
)

"""
Funciones dentro de funciones para
"""

def outer_function():
    def inner_function():
        print("Función interna: Hola, Python !")
    inner_function()

outer_function()

"""
Funciones del lenguaje (built-in)
"""
print(len("Fran"))
print(type(36))
print("Fran".upper())

"""
Variables ocales y globales
"""

global_var = "Python"

print(global_var)

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}")

print(global_var)
# print(local_var) No se puede acceder desde fuera de la función

"""
Extra
"""

def print_numbers(text1, text2)-> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text1 + text2)
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)
        else:
            print(number)
            count += 1
    return count

print(print_numbers("Fizz", "Buzz"))