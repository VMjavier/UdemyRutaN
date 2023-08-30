"""
#Variables globales
nombre1 = "Gato"
entero1 = 10
float1 = 2.8
bool = True 

#detectar tipado
comprobar = isinstance(nombre1,str)
if comprobar:
    print("Es una variable es de tipo string")
else:
    print("No es una variable es de tipo string")

if not isinstance(nombre1,float):
    print("la varible no el de tipo Float")
else:
    print("La varibale es de tipo float")
"""

#Reto progresión geométrica
n = int(input("Ingrese el número de granos iniales"))
Total = 0
for i in range(1,64):
    Total += n**i

print(f"El total de granos es : {Total}.")
print("#Un kilogramo de trigo trae apróx 20.000 granos de trigo")
print(f"El total de kilos de trigo es : {Total/20000}.")
print("#Un bulto de trigo trae apróx 20 kilogramos de trigo")
print(f"El total de bultos de trigo es : {Total/400000}.")

#git init
#git commit -m "first commit"
#git remote add origin https://github.....
#git add .
#git push -f origin main