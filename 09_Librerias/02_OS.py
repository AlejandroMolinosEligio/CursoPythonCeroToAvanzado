# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

#####################
###       OS     ####
#####################

### 1. Importar la biblioteca os

import os

### 2. Obtener el directorio de trabajo actual

# Obtener el directorio de trabajo actual
current_directory = os.getcwd()
print(f"Directorio actual: {current_directory}")

### 3. Listar archivos y directorios

# Listar archivos y directorios en el directorio actual
files_and_dirs = os.listdir('.')
print(f"Archivos y directorios en el directorio actual: {files_and_dirs}")

### 4. Crear un nuevo directorio

# Crear un nuevo directorio
os.mkdir('nuevo_directorio')
print(f"'nuevo_directorio' creado")

### 5. Crear directorios recursivamente

# Crear directorios recursivamente
os.makedirs('dir1/dir2/dir3')
print("'dir1/dir2/dir3' creados")

### 6. Eliminar un archivo

# Crear un archivo de prueba
with open('archivo_a_eliminar.txt', 'w') as f:
    f.write("Este archivo será eliminado")

# Eliminar el archivo
os.remove('archivo_a_eliminar.txt')
print("'archivo_a_eliminar.txt' eliminado")

### 7. Eliminar un directorio vacío

# Eliminar un directorio vacío
os.rmdir('nuevo_directorio')
print("'nuevo_directorio' eliminado")

### 8. Eliminar directorios recursivamente

# Eliminar directorios recursivamente
os.removedirs('dir1/dir2/dir3')
print("'dir1/dir2/dir3' eliminados")

### 9. Renombrar archivos o directorios

# Crear un archivo de prueba
with open('archivo_a_renombrar.txt', 'w') as f:
    f.write("Este archivo será renombrado")

# Renombrar el archivo
os.rename('archivo_a_renombrar.txt', 'archivo_renombrado.txt')
print("'archivo_a_renombrar.txt' renombrado a 'archivo_renombrado.txt'")

### 10. Obtener información sobre un archivo

# Obtener información sobre un archivo
file_info = os.stat('archivo_renombrado.txt')
print(f"Información sobre 'archivo_renombrado.txt': {file_info}")

### 11. Ejecutar un comando del sistema

# Ejecutar un comando del sistema
os.system('echo Hola, mundo!')

### 12. Manejar variables de entorno

#### a. Establecer una variable de entorno

# Establecer una variable de entorno
os.environ['NUEVA_VAR'] = 'valor_de_la_nueva_var'
print(f"NUEVA_VAR: {os.getenv('NUEVA_VAR')}")

### 13. Caminando por el árbol de directorios

# Recorrer el árbol de directorios
for dirpath, dirnames, filenames in os.walk('.'):
    print(f"Directorio actual: {dirpath}")
    print(f"Subdirectorios: {dirnames}")
    print(f"Archivos: {filenames}")

### 14. Manejar permisos de archivos

# Cambiar los permisos de un archivo
with open('archivo_con_permisos.txt', 'w') as f:
    f.write("Archivo con permisos modificados")

os.chmod('archivo_con_permisos.txt', 0o644)
print("'archivo_con_permisos.txt' permisos cambiados a 644")