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

    #constructor
    def __init__(self, color, marca, modelo, motor, maxPotencia, velocidad, puestos):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.maxPotencia = maxPotencia
        self.velocidad = velocidad
        self.puestos = puestos

    #metodos
    def setColor(self, color):
        self.color = color
        
    def getColor(self):
        return self.color

    def setMarca(self, marca):
        self.marca = marca
        
    def getMarca(self):
        return self.marca
    
    def setModelo(self, modelo):
        self.modelo = modelo
        
    def getModelo(self):
        return self.modelo
    
    def setMotor(self, motor):
        self.motor = motor
        
    def getMotor(self):
        return self.motor

    def acelerar(self):
        self.velocidad += 1
        
    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
    soy_publico = "Hola, soy un atributo publico"
    __soy_privado = "Hola, soy un atributo privado"

    def getInfo(self):
        info = "----Información del carro"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Motor: " + self.getMotor()
        return info
    
#fin clase