#Los indices para los diccionarios pueden ser de todo tipo, no solo enteros. 
# Estos indices son “clave - valor”

#Los diccionarios es como el constructor de una clase en JS.

#Con una lista se hace referencia por su INDICE o POSICION. Se reconoce que es lista si tiene [ ]
persona = ['Alfonso', 27, 'San Salvador']

# Las tuplas por estar ( ) - no es modificable
#Los diccionarios se reconocen por tener { } - son mutables

#En el diccionario importa la clave valor
people = {'nombre': 'Alfonso', 'edad': 27, 'direccion': 'San Salvador'}
print(people['nombre'])
print(people['edad'])
print(people['direccion'])

nombre = input().capitalize()
personas = {'nommbre': nombre}

print(personas)
#Va a tirar error porque los diccionarios NO TIENEN INDICE, tienen claves
#print(people[0])

#Agregandole una nueva clave - valor
people['Perros']= ['Candy', 'Thiago', 'Princess']
print(people)
print(people['direccion'])


clientes = [
    {"Nombre": "Juan", "Apellido": "Perez"},
    {"Nombre": "Ana", "Apellido": "Garcia"},
    {"Nombre": "Luis", "Apellido": "Lopez"}
]

apellido_a_buscar = "Garcia"
posicion = -1  # Se inicializa en -1 para indicar si no se encuentra

for i, cliente in enumerate(clientes):
    if cliente["Apellido"] == apellido_a_buscar:
        posicion = i
        break  # Se detiene el bucle cuando se encuentra el elemento

if posicion != -1:
    print(f"El cliente con apellido {apellido_a_buscar} está en la posición {posicion}.")
else:
    print(f"No se encontró un cliente con el apellido {apellido_a_buscar}.")
