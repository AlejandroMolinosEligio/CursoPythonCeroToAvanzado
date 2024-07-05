# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

lista_numeros = [0, 1, 2, 3, 4, 5]

lista_frutas = ["Pera", "Manzana", "Piña", "Coco"]

#############################
###       BUCLE FOR      ####
#############################

print("[+] FOR DE UNA LISTA")
for numero in [1,2,3,4,5,6]:
    print("[+]", numero)

print("[+] FOR DE UNA LISTA DEFINIDA")
for numero in lista_numeros:
    print("[+]", numero)

print("[+] FOR CON RANGE")
for numero in range(0,10,1):
    print("[+]", numero)

###############################
###       BUCLE WHILE      ####
###############################

print("[+] BUCLE WHILE BASE")
x = 1
while x<10:
    print("[+] El valor de x es:", x)
    x+=1

print("[+] BUCLE WHILE EN EL QUE NO ENTRA")
x = 1
while x>10:
    print("[+] El valor de x es:", x)
    x+=1

# print("[+] BUCLE WHILE INFINITO")
# while True:
#     print("[+] Hola mundo!")


###################################
###       BUCLES ANIDADOS      ####
###################################

print("[+] FOR ANIDADO")
for numero in range(10):
    for numero2 in range(5):
        print("[+] El número 1 es:", numero, "y el número 2 es:",numero2)


print("[+] WHILE ANIDADO CON FOR")
x=1
while x<5:
    for numero in range(5):
        print("[+] La x vale:", x, "y el número es:",numero)
    x+=1

##################################
###       RUPTURA BUCLES      ####
##################################

print("[+] BUCLE WHILE RUPTURA")
x = 1
while x<10:
    print("[+] El valor de x es:", x)

    if x == 5:
        break

    x+=1

print("[+] BUCLE WHILE INFINITO CON RUPTURA")
while True:
    print("[+] Hola mundo!")
    break

###################################
###       CONTINUE BUCLES      ####
###################################

print("[+] Impresión cadena Python")
cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        continue
    print("[+]",letra)

print("[+] Impresión de números")
x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print("[+]", x)

#########################
###       MATCH      ####
#########################

condicion = 2
if condicion == 1:
    print("[+] Haz a")
elif condicion == 2:
    print("[+] Haz b")
elif condicion == 3:
    print("[+] Haz c")
else:
    print("[+] Haz d")


match condicion:
    case 1:
        print("[+] Haz a")
    case 2:
        print("[+] Haz b")
    case 3:
        print("[+] Haz c")
    case _:
        print("[+] Haz d")


