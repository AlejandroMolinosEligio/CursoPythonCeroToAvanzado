# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

#############################
###       FUNCIONES      ####
#############################

def saludar():

    return print("Hola mundo")

def suma():

    return 5 + 5

saludar()
print(f'[+] {suma()}')


##########################################
###       FUNCIONES CON ARGUMENTO     ####
##########################################

def saludar(nombre):

    return print(f'[+] Hola {nombre}!')

saludar("Juan")
saludar("mundo")


def suma(numero1, numero2):

    return numero1 + numero2

print(f'[+] {suma(10, 2)}')
print(f'[+] {suma(20, 6)}')


def saludar(nombre="mundo"):

    return print(f'[+] Hola {nombre}!')

saludar()
saludar("Jose")

###################################
###       BUENAS PRÁCTICAS     ####
###################################


def suma(numero1: int, numero2: int) -> int:

    return numero1 + numero2

print(f'[+] {suma(10, 6)}')

