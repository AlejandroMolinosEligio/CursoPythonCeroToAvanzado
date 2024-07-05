# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

###################################
###       Creacion clases      ####
###################################

class Perro:
    pass  # pass no hace nada


pastor_aleman = Perro()
perro_agua = Perro()
bodegero = Perro()

print("[+]",type(pastor_aleman))
print("[+]",type(perro_agua))
print("[+]",type(bodegero))



##################################
###       Añadir métodos      ####
##################################


class Perro:
    def ladrar(self):
        print("[+] guau, guau")


perro_agua = Perro()

perro_agua.ladrar()


####################################
###       Añadir atributos      ####
####################################


class Perro:
    def sacar_a_pasear(self):
        self.en_casa = False
        print("[+] Has sacado el perro a pasear")

    def volver_a_casa(self):
        self.en_casa = True
        print("[+] Has vuelto a casa")


perro_agua = Perro()

perro_agua.sacar_a_pasear()

print(f'[+] ¿El perro está en casa? {perro_agua.en_casa}')

perro_agua.volver_a_casa()

print(f'[+] ¿El perro está en casa? {perro_agua.en_casa}')


##################################
###       Inicialización      ####
##################################

class Perro:
    def __init__(self, name: str):
        self.name = name

pastor_aleman = Perro('Rex')

print(f'[+] El perro se llama {pastor_aleman.name}')


###############################
###       Propiedades      ####
###############################

class Perro:
    def __init__(self, name: str):
        self.hidden_name = name

    @property
    def name(self) -> str:
        print('[*] Obteniendo nombre')
        return self.hidden_name
    
    @name.setter
    def name(self, name: str) -> None:
        print('[*] Estableciendo nombre')
        self.hidden_name = name

perro_agua = Perro('Luna')

print(f'[+] El perro se llama {perro_agua.name}')

perro_agua.name = 'Lana'

print(f'[+] El perro se llama {perro_agua.name}')


######################################
###       Valores calculados      ####
######################################

class Perro:
    def __init__(self, name: str, edad: int):
        self.name = name
        self.edad = edad

    @property
    def edad_humana(self) -> int:

        return 7 * self.edad
    

perro_agua = Perro('Luna',2)

print(f'[+] El perro se llama {perro_agua.name} y tiene {perro_agua.edad_humana} en años humanos')


###################################
###       Atributos clase      ####
###################################

class Perro:

    adiestrado = True

    def __init__(self, name: str, edad: int):
        self.name = name
        self.edad = edad


perro_agua = Perro('Luna',2)
pastor_aleman = Perro('Rex',1)

print(f'[+] ¿El perro {perro_agua.name} está adiestrado? {perro_agua.adiestrado}')
print(f'[+] ¿El perro {pastor_aleman.name} está adiestrado? {pastor_aleman.adiestrado}')

pastor_aleman.adiestrado = False

print(f'[+] ¿El perro {perro_agua.name} está adiestrado? {perro_agua.adiestrado}')
print(f'[+] ¿El perro {pastor_aleman.name} está adiestrado? {pastor_aleman.adiestrado}')

Perro.adiestrado = False

print(f'[+] ¿El perro {perro_agua.name} está adiestrado? {perro_agua.adiestrado}')
print(f'[+] ¿El perro {pastor_aleman.name} está adiestrado? {pastor_aleman.adiestrado}')


#################################
###       Métodos clase      ####
#################################

class Perro:

    count = 0

    def __init__(self):
        Perro.count += 1

    @classmethod
    def total_perros(cls) -> None:
        print(f'[+] Hay un total de {cls.count} perros!')

perro_agua = Perro()
pastor_aleman = Perro()
bodegero = Perro()

Perro.total_perros()