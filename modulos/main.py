"""
#importar un modulo
import mimodulo

sum = mimodulo.suma(2,5)
print(sum)

rest = mimodulo.resta(4,10)
print(rest)
"""

#para importar una sola función de un modulo
from mimodulo import suma

sum = suma(10,500)
print(sum)

#modulo de fecha
import datetime

print(datetime.date.today())

#modulo de matemáticas
import math

num = 2
raiz = math.sqrt(num)
print(f"La raíz cuadrada de {num} es {raiz}")
#redondear a un entero
print(f"La raíz cuadrada de {num} es {math.floor(raiz)}")