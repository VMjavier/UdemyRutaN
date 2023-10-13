#inicio clase

class Carro:
    #atributos
    color = "negro"
    marca = "ferrari"
    modelo = "purosangue"
    motor = "v12 65"
    maxPotencia = 725
    velocidad = 300
    puestos = 4

    """metodos"""
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
#fin clase


#pruebas
coche = Carro()
print(coche.marca)

print(f"Velocidad actual {coche.velocidad}")
coche.acelerar()
print(f"Velocidad actual {coche.velocidad}")
coche.frenar()
coche.frenar()
print(f"Velocidad actual {coche.velocidad}")

coche2 = Carro()
print(f"Carro 2 color {coche2.getColor()}")
coche2.setColor("verde")
print(f"Carro 2 color {coche2.getColor()}")
