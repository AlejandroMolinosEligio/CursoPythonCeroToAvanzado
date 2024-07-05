# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

##################################
###       CALCULAR MEDIA      ####
##################################

alumnos_notas = {

    'Pepe': {
        'Lengua': 8.75,
        'Matemáticas': 5,
        'Educación física': 10,
        'Inglés': 7,
        'Historia': 3
    },

    'Alicia': {
        'Lengua': 5,
        'Matemáticas': 10,
        'Educación física': 8,
        'Inglés': 6,
        'Historia': 8
    },

    'Ricardo': {
        'Lengua': 5,
        'Matemáticas': 7,
        'Educación física': 9,
        'Inglés': 10,
        'Historia': 8
    }
}

print("[+] Vamos a calcular la nota media de cada uno de los alumnos")

for alumno in alumnos_notas:
    media = 0

    for asignatura in alumnos_notas[alumno]:
        media += alumnos_notas[alumno][asignatura]
    
    print("\t[+] La nota media de", alumno, "es de", int(media)/5)

print("[+] Ya se han calculado las notas medias de todos los alumnos, fin del script!")
