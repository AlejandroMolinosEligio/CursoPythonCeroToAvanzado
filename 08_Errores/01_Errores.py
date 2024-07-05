# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

############################
###       Errores 1     ####
############################

lista_frutas = ["Pera", "Manzana", "Piña", "Coco"]

indice = 0

print(f'[+] Vamos a intentar acceder al índice {indice}')

try:
    print(f'[+] El valor seleccionado es {lista_frutas[indice]}')

except:

    print(f'[+] El índice que se ha escogido no es correcto ya que está fuera de rango')


#############################
###       Errores 2      ####
#############################

try:
    # Intentar realizar una división
    numerador = 10
    denominador = 0
    resultado = numerador / denominador
    print("[+] El resultado es:", resultado)
except ZeroDivisionError:
    # Manejar la excepción de división por cero
    print("[+] Error: No se puede dividir por cero")

    

############################################
###       Errores sin saber motivo      ####
############################################

try:
    # Intentar realizar una división
    numerador = 10
    denominador = 0
    resultado = numerador / denominador
    print("[+] El resultado es:", resultado)
except Exception as e:
    # Manejar la excepción de división por cero
    print(f'[+] El error es {e}')
