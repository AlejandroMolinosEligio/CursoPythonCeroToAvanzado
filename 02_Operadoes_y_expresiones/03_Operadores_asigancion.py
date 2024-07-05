# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

############################################
###       OPERADORES DE ASIGNACIÓN      ####
############################################

a=7; b=2
print("[+] Operadores de asignación")
x=a; x+=b;  print("[+] x+=", x)  # 9
x=a; x-=b;  print("[+] x-=", x)  # 5
x=a; x*=b;  print("[+] x*=", x)  # 14
x=a; x/=b;  print("[+] x/=", x)  # 3.5
x=a; x**=b; print("[+] x**=", x) # 49

##############################
###       OPERADOR =      ####
##############################

x=2       # Uso correcto del operador =
print(x)  # 2

###############################
###       OPERADOR +=      ####
###############################

x=5      # Ejemplo de como incrementar
x+=1     # en una unidad x
print(x)

###############################
###       OPERADOR -=      ####
###############################

i = 5
i -= 1
print(i) # 4

###############################
###       OPERADOR *=      ####
###############################

a=10; b=2 # Inicializamos a 10 y 20
a*=b      # Usando dos variables
print(a)  # 20

###############################
###       OPERADOR /=      ####
###############################

x = 10
x/=3
print(x) # 10/3 = 3.333

################################
###       OPERADOR **=      ####
################################

x=5      # Eleva el número al cuadrado
x**=2    # y guarda el resultado en la misma
print(x) # 25