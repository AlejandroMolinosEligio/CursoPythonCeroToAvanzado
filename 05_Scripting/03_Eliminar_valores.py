# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

####################################
###       ELIMINAR VALORES      ####
####################################

lista_compra = ["Tomate", "Patatas fritas", "Manzanas", "Huevos", "Harina", "Chocolate", "Zumo de piña"]

print("[+] VAMOS A IR ELIMINANDO ELEMENTOS DE LA CESTA DE LA COMPRA")

while True:

    print("[+] La lista de la compra actual es", lista_compra)

    eliminar = input("[+] Escribe que quieres quitar de la lista de la compra[exit para salir]: ")

    match eliminar:

        case "Tomate":
            lista_compra.remove(eliminar)
            print("[+] Se ha eliminado", eliminar, "de la lista de la compra\n")

        case "Patatas fritas":
            lista_compra.remove(eliminar)
            print("[+] Se ha eliminado", eliminar, "de la lista de la compra\n")

        case "Manzanas":
            lista_compra.remove(eliminar)
            print("[+] Se ha eliminado", eliminar, "de la lista de la compra\n")

        case "Huevos":  
            lista_compra.remove(eliminar)
            print("[+] Se ha eliminado", eliminar, "de la lista de la compra\n")

        case "Harina":
            lista_compra.remove(eliminar)
            print("[+] Se ha eliminado", eliminar, "de la lista de la compra\n")

        case "Chocolate":
            lista_compra.remove(eliminar)
            print("[+] Se ha eliminado", eliminar, "de la lista de la compra\n")

        case "Zumo de piña":
            lista_compra.remove(eliminar)
            print("[+] Se ha eliminado", eliminar, "de la lista de la compra\n")

        case "exit":
            print("[+] Has seleccionado salir, el script terminará")
            break

        case _:
            print("[+] La opción escogida no es válida, escoge uno de los elementos de la lista.\n")