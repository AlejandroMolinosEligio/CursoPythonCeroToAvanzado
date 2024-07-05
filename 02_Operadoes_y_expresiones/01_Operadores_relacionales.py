# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

###########################################
###       OPERADORES RELACIONALES      ####
###########################################

x=2; y=3
print("[+] Operadores Relacionales")
print("[+] x==y =", x==y) # False
print("[+] x!=y =", x!=y) # True
print("[+] x>y  =", x>y)  # False
print("[+] x<y  =", x<y)  # True
print("[+] x>=y =", x>=y) # False
print("[+] x<=y =", x<=y) # True

###############################
###       OPERADOR ==      ####
###############################

print(4==4)          # True
print(4==5)          # False
print(4==4.0)        # True
print(0==False)      # True
print("asd"=="asd")  # True
print("asd"=="asdf") # False
print(2=="2")        # False
print([1, 2, 3] == [1, 2, 3]) # True

###############################
###       OPERADOR !=      ####
###############################

print(4!=4)          # False
print(4!=5)          # True
print(4!=4.0)        # False
print(0!=False)      # False
print("asd"!="asd")  # False
print("asd"!="asdf") # True
print(2!="2")        # True
print([1, 2, 3] != [1, 2, 3]) # False

##############################
###       OPERADOR >      ####
##############################

print(5>3) # True
print(5>5) # False

##############################
###       OPERADOR <      ####
##############################

print(5<3) # True
print(5<5) # False

###############################
###       OPERADOR >=      ####
###############################

print(3>=3)           # True
print([3,4] >= [3,5]) # False

###############################
###       OPERADOR <=      ####
###############################

print(3<=2.99999999999999999)

################################
###       CURIOSIDADES      ####
################################

print(True==1)     # True
print(True>0.999)  # True
print([1, 2] > [10, 10]) # False

print("abc" < "abd") # True
print("A"<"a")       # True
print(ord('A')) # 65
print(ord('a')) # 97