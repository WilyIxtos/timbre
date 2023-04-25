tabla_multiplicar=int(input("ingrese la cantidad a multiplicarse:")) 
tabla_multiplicar=int(input("ingrese la cantidad a iniciar:")) 
tabla_multiplicar=int(input("ingrese la cantidad a terminar:")) 
inicio=0
fin=10
for i in range(inicio,fin + 1):
     print(tabla_multiplicar,"*", i, "=",tabla_multiplicar*i)
