from carro import Carro

coche1 = Carro("Azul","Ferrari","Portofino","V8", 591, 320, 4)
coche2 = Carro("Amarillo","Ferrari","F8 Tributo","V8", 710, 340, 2)
coche3 = Carro("Negro","Ferrari","812 Superfast","V12", 789, 340, 2)

print(coche1.getInfo())
print(coche2.getInfo())
print(coche3.getInfo())

#Detectar tipado
if type(coche3) == Carro:
    print("Es un objeto correto: " + str(type(coche3)))
else:
    print("No es un objeto correcto")

#Visibilidad atributos
print(Carro.soy_publico)
#print(Carro.__soy_privado) no muestra ya que es privado
