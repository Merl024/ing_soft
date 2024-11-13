"""
    La clase sirve similar a JS, por lo que hacer la clase, podes o no hacer un constructor de cuales son los parametros que se van a 
    utilizar, y las funciones (def) son los metodos de las clases, segun su logica. El self siempre sera necesario para acceder a TODA la 
    informacion dentro de la clase
"""

class Personaje:
    # nombre = "Default"
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    
    # Para darle valor a los atributos hace falta un METODO CONSTRUCTOR que reciba esos valores
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        # Self es un atributo que hace referencia a si mismo, para tener acceos a los atributos y metodos de la clase
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print("Nombre:", self.nombre)
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        print("Defensa:", self.defensa)
        print("Vida:", self.vida)

    def subirNivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
        print("\nNivel subido!")

    def vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha muerto...")

    def danio(self, enemigo):
        return self.fuerza - enemigo.defensa

    def ataque(self, enemigo):
        danio = self.danio(enemigo)
        enemigo.vida = enemigo.vida - danio
        print(f"El personaje {self.nombre} ataca al personaje {enemigo.nombre} y le hace {danio} puntos de daño!")
        if enemigo.vivo():
            print(f'La vida de {enemigo.nombre} es {enemigo.vida}')
        else: 
            enemigo.morir()



miPersonaje = Personaje("Melude", 10, 1, 5, 100)
# miPersonaje.atributos()
# miPersonaje.subirNivel(20, 50, 30)
# miPersonaje.atributos()
# print(miPersonaje.vivo())
# miPersonaje.morir()

# Personaje enemigo #
personajeEnemigo = Personaje('Bitboss', 8, 5, 3, 100)
print(miPersonaje.danio(personajeEnemigo))
print(miPersonaje.ataque(personajeEnemigo))
personajeEnemigo.atributos()



### Si ponemos miPersonaje = Personaje(), imprimira los valores por default
### Esto es para imprimir los valores por defecto ####
# print("El nombre del jugador es:", miPersonaje.nombre)
# print("La fuerza del personaje es:", miPersonaje.fuerza)