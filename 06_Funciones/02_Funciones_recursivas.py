# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

########################################
###       FUNCIONES RECRUSIVAS      ####
########################################

def funcion_fibonacci(n):

    a = 0
    b = 1

    if n == 0:
        return a

    if n == 1:
        return b

    for _ in range(n):

        c = a+b
        a = b
        b = c

    return b

print(f'[+] El resultado es {funcion_fibonacci(4)}')


def funcion_fibonacci_recursiva(n):

    a = 0
    b = 1

    if n == 0:
        return a

    elif n == 1:
        return b
    
    else:
        return funcion_fibonacci_recursiva(n-2) + funcion_fibonacci_recursiva(n-1)

print(f'[+] El resultado es {funcion_fibonacci(4)}')