#Prueba de paquetes propios
from mipaquete import aritmetica
from mipaquete import trigonometrica
#alternativa "from mipaquete import aritmetica, trigonometrica"

print(aritmetica.calc(3,8,"resta"))
print(trigonometrica.coseno(270))