# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

##########################
###       TUPLAS      ####
##########################

# Tupla vacía
tupla_vacia = ()

# Tupla con elementos
tupla = (1, 2, 3, 4, 5)

# Tupla con diferentes tipos de datos
tupla_mixta = (1, "Hola", 3.14, True)

# Tupla anidada
tupla_anidada = (1, (2, 3), [4, 5])

print("[+]", tupla)
print("[+]", tupla_mixta)
print("[+]", tupla_anidada)

# ACCEDER A ELEMENTOS

tupla = (10, 20, 30, 40, 50)

# Acceder al primer elemento
print("[+]", tupla[0])  # Output: 10

# Acceder al último elemento
print("[+]", tupla[-1])  # Output: 50

# Acceder a un rango de elementos
print("[+]", tupla[1:3])  # Output: (20, 30)

# OPERACIONES CON TUPLAS

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenación de tuplas
tupla_concatenada = tupla1 + tupla2
print("[+]", tupla_concatenada)  # Output: (1, 2, 3, 4, 5, 6)

# Repetir tupla
tupla_repetida = tupla1 * 3
print("[+]", tupla_repetida)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Longitud de una tupla
print("[+]", len(tupla1))  # Output: 3

# DESEMPAQUETAR TUPLAS

tupla = (10, 20, 30)

# Desempaquetado
a, b, c = tupla
print("[+]", a)  # Output: 10
print("[+]", b)  # Output: 20
print("[+]", c)  # Output: 30
