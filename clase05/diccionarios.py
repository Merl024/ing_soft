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

#Va a tirar error porque los diccionarios NO TIENEN INDICE, tienen claves
#print(people[0])

#Agregandole una nueva clave - valor
people['Perros']= ['Candy', 'Thiago', 'Princess']
print(people)
print(people['direccion'])