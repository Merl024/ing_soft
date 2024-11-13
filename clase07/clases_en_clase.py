# CLASES
# debemos representar el mundo para que el software sepa que hacer
# métodos y características (propiedades)
# Las propiedades son características del objeto (nombre, edad, correo, etc) y 
# el método son cosas que el objeto puede hacer (hablar, caminar, comer, imprimir, etc)

# EJEMPLO DEL CARRITO
# atributes: year, model, color, doors, make
# methods: turn, stop, etc

# programación orientada a objetos (POO)
# podemos especificar la clase de información y las acciones que pueden ser realizadas con estas instancias

class Perros:
    """Representación de un perro"""
    patas = 4
    alegre = True
    nombre = ""

    
perro01 = Perros()    # para cambiarlo puede ser: perro01.nombre = "Luis"
perro02 = Perros()

perro01.nombre = "Firulais"
perro02.nombre = "Ambulancia"

print(perro01.patas)
print(perro01.alegre)
print(perro01.nombre)

print(perro02.patas)
print(perro02.alegre)
print(perro02.nombre)
