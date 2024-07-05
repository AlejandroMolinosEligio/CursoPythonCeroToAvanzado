# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

########################
###       Numpy     ####
########################

# INSTALACION:
'''
    python -m pip install numpy
'''

import numpy as np

### 1. Crear un arreglo (array)

#### a. Arreglo unidimensional

# Crear un arreglo unidimensional
arr = np.array([1, 2, 3, 4, 5])
print("[+]",arr)

#### b. Arreglo bidimensional

# Crear un arreglo bidimensional
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("[+]",arr)

### 2. Operaciones aritméticas

#### a. Suma de arreglos

# Crear dos arreglos
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Sumar los arreglos
sum_arr = arr1 + arr2
print("[+]",sum_arr)

#### b. Producto escalar

# Crear dos arreglos
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Producto escalar
dot_product = np.dot(arr1, arr2)
print("[+]",dot_product)

### 3. Funciones estadísticas

#### a. Media

# Crear un arreglo
arr = np.array([1, 2, 3, 4, 5])

# Calcular la media
mean_val = np.mean(arr)
print("[+]",mean_val)

#### b. Desviación estándar

# Crear un arreglo
arr = np.array([1, 2, 3, 4, 5])

# Calcular la desviación estándar
std_dev = np.std(arr)
print("[+]",std_dev)

### 4. Indexación y segmentación (slicing)

#### a. Indexación

# Crear un arreglo
arr = np.array([1, 2, 3, 4, 5])

# Acceder al tercer elemento (índice 2)
print("[+]",arr[2])

#### b. Segmentación

# Crear un arreglo
arr = np.array([1, 2, 3, 4, 5])

# Obtener una sección del arreglo (del segundo al cuarto elemento)
print("[+]",arr[1:4])

### 5. Crear arreglos con valores inicializados

#### a. Arreglo de ceros

# Crear un arreglo de ceros
zeros_arr = np.zeros((3, 3))
print("[+]",zeros_arr)

#### b. Arreglo de unos

# Crear un arreglo de unos
ones_arr = np.ones((2, 4))
print("[+]",ones_arr)

#### c. Arreglo con un rango de valores

# Crear un arreglo con un rango de valores
range_arr = np.arange(0, 10, 2)
print("[+]",range_arr)

#### d. Arreglo con valores equidistantes

# Crear un arreglo con 5 valores equidistantes entre 0 y 1
linspace_arr = np.linspace(0, 1, 5)
print("[+]",linspace_arr)

### 6. Operaciones con matrices

#### a. Matriz identidad

# Crear una matriz identidad de 3x3
identity_matrix = np.eye(3)
print("[+]",identity_matrix)

#### b. Transpuesta de una matriz

# Crear una matriz
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Obtener la transpuesta de la matriz
transposed_matrix = np.transpose(matrix)
print("[+]",transposed_matrix)

### 7. Funciones universales (ufunc)

#### a. Aplicar una función universal

# Crear un arreglo
arr = np.array([1, 2, 3, 4, 5])

# Aplicar la función seno a cada elemento
sin_arr = np.sin(arr)
print("[+]",sin_arr)