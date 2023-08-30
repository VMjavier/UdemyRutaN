# Recordar que # es para comentarios
"""
comentario multilinea
"""


""""
print("hola mundo")
nombre = "Javier"
apellido = "Velasco"
grado = "11-1"
print(f"Mi nombre es {nombre} {apellido} y soy del grado {grado}.")
"""

"parámetros opcinales"
def suma(a1,a2,a3 = None):
    sum=a1+a2
    if a3 != None:
        print(sum+a3)
    else:
        print(sum)

def resta(a,b):
    c=a-b
    print(c)

def calc():
    print("Calculadora")
    print("1. suma \n2. resta \n3. multiplicación")
    #c=input("Ingrese operación")

suma(2,3,5)

