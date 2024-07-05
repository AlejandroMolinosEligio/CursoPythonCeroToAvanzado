# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

#################################
###       CALCULAR EDAD      ####
#################################

print("[+] CON ESTE PROGRAMA SEREMOS CAPACES DE CALCULAR LA EDAD DE LAS PERSONAS EN UN AÑO CONCRETO")

opcion = input("[+] ¿Quieres calcular la edad de alguna persona?[s/n]: ")

match opcion:

    case "s":
        print("[+] Has escogido calcular la edad de una persona!")
        nacimiento = input("[+] Introduce el año de nacimiento de la persona: ")
        fecha = input("[+] Introduce el año en el que quieres saber que edad tenía: ")

        print("[+] Esta persona en el año", fecha, "tenía", int(fecha)-int(nacimiento)," años!")

    case "n":
        print("[+] Has escogido que no quieres calcular la edad, el script terminará.")

    case _:
        print("[+] La opoción escogida no es válida, por favor ejecuta otra vez el script y selecciona una opción correcta.")
