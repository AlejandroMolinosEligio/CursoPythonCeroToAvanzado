# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

##########################
###       LISTAS      ####
##########################

lista_numeros = [0, 1, 2, 3, 4, 5]

lista_frutas = ["Pera", "Manzana", "Piña", "Coco"]

lista_mix = [0 , 1, "Piña", 3, "Manzana"]

print("[+] Lista números:", lista_numeros)
print("[+] Lista frutas:", lista_frutas)
print("[+] Lista mix:", lista_mix)

print("[+] Tamaño de lista de números:", len(lista_numeros))
print("[+] Tamaño de lista de frutas:", len(lista_frutas))
print("[+] Tamaño de lista de mix:", len(lista_mix))


##########################
###      ÍNDICES      ####
##########################


indice = lista_frutas[1] # Manzana
print("[+] La fruta es:", indice)

indice = lista_frutas[2] # Piña
print("[+] La fruta es:", indice)

indice = lista_frutas[-1] # Coco
print("[+] La fruta es:", indice)


print("[+] Slicing frutas:", lista_frutas[1:3])
print("[+] Slicing frutas:", lista_frutas[1:])
print("[+] Slicing frutas:", lista_frutas[:2])

texto = "Hola mundo!"

print("[+] El caracter es:", texto[1])
print("[+] El fragmento es:", texto[3:-1])
print("[+] El fragmento es:", texto[:4])
