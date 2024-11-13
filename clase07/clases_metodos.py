# los métodos pueden utilizar parámetros

class Perros:
    """Representación de un perro"""
    patas = 4
    alegre = True
    nombre = ""

    # dentro de una clase quiero meter una función debo ocupar 'self' pq es la propiedad de una clase
    def ladrar(self): # parámetros: valores que se vuelven requisitos # self es como de pertenencia
        print("El perro dice guau")
    

perro01 = Perros()    # para cambiarlo puede ser: perro01.nombre = "Luis"
perro02 = Perros()

perro01.nombre = "Firulais"
perro02.nombre = "Ambulancia"

print(perro01.patas)
print(perro01.alegre)
print(perro01.nombre)
perro01.ladrar()

print(perro02.patas)
print(perro02.alegre)
print(perro02.nombre)