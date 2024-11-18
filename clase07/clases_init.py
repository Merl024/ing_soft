class Perros:
    # Lo que esta dentro de los parentesis son los parametros, cuando se espefician son argunmentos
    def __init__(self, patas, alegre, nombre, raza):
    #########################################
    ## A todo esto se le llama constructor ##
    #########################################
    # Estos son los atributos
        self.patas = patas
        self.alegre = alegre
        self.nombre = nombre
        self.raza = raza

    #El self sirve principalmente para que el metodo sea usado global, no sea exclusivo
    def ladrar(self):
        print(f'El perro {self.nombre} de la raza {self.raza} dice Guau')
    

perro01 = Perros(4, True, 'Candy', 'Maltes')
perro01.ladrar()


# Tiene que estar en el mismo orden en el que se ha puesto en la clase
perro02 = Perros('Thiago', True, 3)
perro02.ladrar()
