# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

lista_numeros = [0, 1, 2, 3, 4, 5]

lista_frutas = ["Pera", "Manzana", "Piña", "Coco"]

########################################
###       SENTENCIAS IF y ELSE      ####
########################################

x = 1
y = 2
if x>y:
    print("[+]",x, "es mayor que", y)
else:
    print("[+]",x, "es menor que", y)



x = 1
y = 2
if x>y:
    print("[+]",x, "es mayor que", y)
elif x>y:
    print("[+]",x, "es menor que", y)
else:
    print("[+]",x, "es igual que", y)


# IF CON LISTAS

fruta = "Manzana"
if fruta in lista_frutas:
    print("En la lista hay", fruta)
else:
    print("En la lista no hay", fruta)


numero = 4
if numero in lista_numeros:
    print("En la lista está el número", numero)
else:
    print("En la lista no está el número", numero)

numero = 4
if numero not in lista_numeros: # CONDICIÓN NEGATIVA
    print("En la lista no está el número", numero)
else:
    print("En la lista está el número", numero)