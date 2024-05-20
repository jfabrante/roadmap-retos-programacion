# Listas

my_list: list = ["Fran", "Topuria", "Canelo"]
print(my_list)
my_list.append("Castor") # Inserción
my_list.append("Tyson")
print(my_list)
my_list.remove("Fran") # Eliminación
print(my_list)
print(my_list[2]) # Acceso
print(my_list)
my_list[1] = "Cuervillo" # Actualización
print(my_list)
my_list.sort() # Ordenación
print(my_list)
print(type(my_list))

# Tuplas
my_tuple: tuple = ("Fran", "Padilla", "jfabrante")
print(my_tuple)
print(my_tuple[1])
my_tuple = tuple(sorted(my_tuple)) # Ordenación
print(type(my_tuple))

# Sets
my_set = {"Fran", "Padilla", "jfabrante", 44}
print(my_set)
my_set.add("mantrestel@gmail.com")
print(my_set)
# my_set = set(sorted(my_set)) # No se puede ordenar
print(my_set)
print(type(my_set))

# Diccionario
my_dict: dict = {"name":"Fran", "surname":"Padilla", "alias":"jfabrante","age":44}
my_dict["email"] = "mantrestel@gmail.com" # Inserción
print(my_dict)
print(my_dict["name"]) # Acceso
print(my_dict)
my_dict["age"] = "37" # Actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # Ordenación
print(my_dict)
print(type(my_dict))

"""
Extra
"""

def my_agenda():

    agenda = {}

    while True:
        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f"El contacto {name} es {agenda[name]}")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                phone = input("Introduce el teléfono del contacto: ")
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                    agenda[name] = phone
                else:
                    print("Debes introducir un número con igual o menos de 11 dígitos.")
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    phone = input("Introduce el teléfono del contacto: ")
                    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                        agenda[name] = phone
                    else:
                        print("Debes introducir un número igual o menor de 11 dígitos.")
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")

    

my_agenda()