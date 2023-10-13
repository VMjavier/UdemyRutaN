class Pokemon:
    nombre = "Charizard"
    tipo = "fuego"
    ataque = 84
    defensa = 78
    salud = 78
    habilidadPrincipal = "Mar de llamas"
    movimiento1 = "Lanzallamas"
    movimiento2 = "Garra dragón"
    naturaleza = "Firme"

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo = tipo

    def getAtaque(self):
        return self.ataque
    
    def setAtaque(self, ataque):
        self.ataque = ataque

    def getDefensa(self):
        return self.defensa
    
    def setDefensa(self, defensa):
        self.defensa = defensa

    def getSalud(self):
        return self.salud
    
    def setSalud(self, salud):
        self.salud = salud

    def atacar(self):
        return "Estoy atacando"
    
    def defender(self):
        return "Estoy defendiendo"


class Region(Pokemon):
    color = "Rojo"
    tamaño = "Grande"

    def __init__(self):
        self.ataqueEspecial = 109
        self.defesaEspecial = 85

    def getAtaqueEspecial(self):
        return self.ataqueEspecial
        
    def getDefensaEspecial(self):
        return self.defesaEspecial
        
    def newAtaqueEspecial(self, ataqueEspecial):
        self.ataqueEspecial = ataqueEspecial
        return self.ataqueEspecial