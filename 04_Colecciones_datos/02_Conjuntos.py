# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

#############################
###       CONJUNTOS      ####
#############################

# Conjunto vacío
conjunto_vacio = set()

# Conjunto con elementos
conjunto = {1, 2, 3, 4, 5}

# Conjunto con elementos duplicados (los duplicados se eliminan automáticamente)
conjunto_con_duplicados = {1, 2, 2, 3, 4, 4, 5}
print("[+]", conjunto_con_duplicados)  # Output: {1, 2, 3, 4, 5}

# Crear un conjunto a partir de una lista
conjunto_desde_lista = set([1, 2, 3, 4, 5, 5, 6])
print("[+]", conjunto_desde_lista)  # Output: {1, 2, 3, 4, 5, 6}

# AÑADIR Y ELIMINAR 

conjunto = {1, 2, 3}

# Añadir un elemento
conjunto.add(4)
print("[+]", conjunto)  # Output: {1, 2, 3, 4}

# Eliminar un elemento (sin error si el elemento no existe)
conjunto.discard(2)
print("[+]", conjunto)  # Output: {1, 3, 4}

# Eliminar un elemento (con error si el elemento no existe)
conjunto.remove(3)
print("[+]", conjunto)  # Output: {1, 4}

# Eliminar y retornar un elemento arbitrario
elemento = conjunto.pop()
print("[+]", elemento)
print("[+]", conjunto)

# OPERACIONES 

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# Unión (todos los elementos de ambos conjuntos)
union = conjunto1 | conjunto2
print("[+]", union)  # Output: {1, 2, 3, 4, 5}

# Intersección (elementos comunes a ambos conjuntos)
interseccion = conjunto1 & conjunto2
print("[+]", interseccion)  # Output: {3}

# Diferencia (elementos en conjunto1 pero no en conjunto2)
diferencia = conjunto1 - conjunto2
print("[+]", diferencia)  # Output: {1, 2}

# Diferencia simétrica (elementos en conjunto1 o conjunto2, pero no en ambos)
diferencia_simetrica = conjunto1 ^ conjunto2
print("[+]", diferencia_simetrica)  # Output: {1, 2, 4, 5}

# COMPROBACIONES

conjunto = {1, 2, 3, 4, 5}

# Comprobar si un elemento está en el conjunto
print("[+]", 3 in conjunto)  # Output: True
print("[+]", 6 in conjunto)  # Output: False

# MÉTODOS ADICIONALES

conjunto = {1, 2, 3}

# Longitud del conjunto
print("[+]", len(conjunto))  # Output: 3

# Limpiar todos los elementos del conjunto
conjunto.clear()
print("[+]", conjunto)  # Output: set()