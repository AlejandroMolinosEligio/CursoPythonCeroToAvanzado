# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

################################
###       DICCIONARIOS      ####
################################

# Diccionario vacío
diccionario_vacio = {}

# Diccionario con elementos
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

print("[+]", diccionario)

# ACCEDER A ELEMENTOS

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a un valor usando la clave
print("[+]", diccionario["nombre"])  # Output: Juan
print("[+]", diccionario["edad"])    # Output: 30

# Usar el método get() para acceder a un valor
print("[+]", diccionario.get("ciudad"))  # Output: Madrid
# Si la clave no existe, get() devuelve None o un valor por defecto si se proporciona
print("[+]", diccionario.get("pais", "No especificado"))  # Output: No especificado

# MODIFICAR ELEMENTOS

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Modificar un valor existente
diccionario["edad"] = 31
print("[+]", diccionario)  # Output: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid'}

# Añadir un nuevo par clave-valor
diccionario["pais"] = "España"
print("[+]", diccionario)  # Output: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'pais': 'España'}

# ELIMINAR ELEMENTOS

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Eliminar un par clave-valor usando del
del diccionario["ciudad"]
print("[+]", diccionario)  # Output: {'nombre': 'Juan', 'edad': 30}

# Eliminar un par clave-valor usando pop()
edad = diccionario.pop("edad")
print("[+]", diccionario)  # Output: {'nombre': 'Juan'}
print("[+]", edad)         # Output: 30

# Eliminar todos los elementos usando clear()
diccionario.clear()
print("[+]", diccionario)  # Output: {}

# ITERAR

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Iterar sobre las claves
for clave in diccionario:
    print("[+]", clave)

# Iterar sobre los valores
for valor in diccionario.values():
    print("[+]", valor)

# Iterar sobre los pares clave-valor
for clave, valor in diccionario.items():
    print("[+]", f"{clave}: {valor}")

# MÉTODOS ADICIONARLES

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Obtener todas las claves
claves = diccionario.keys()
print("[+]", claves)  # Output: dict_keys(['nombre', 'edad', 'ciudad'])

# Obtener todos los valores
valores = diccionario.values()
print("[+]", valores)  # Output: dict_values(['Juan', 30, 'Madrid'])

# Obtener todos los pares clave-valor
items = diccionario.items()
print("[+]", items)  # Output: dict_items([('nombre', 'Juan'), ('edad', 30), ('ciudad', 'Madrid')])

