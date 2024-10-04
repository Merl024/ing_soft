#Ejemplo: creacion de correo con base a los datos del usuario
#este es el dominio del correo, es decir a la empresa en donde pertenece el correo
dominio = 'lavacalola.com'

#consiguiendo los datos
nombre = input('Digite su nombre: ')
apellido = input('Digite su apellido: ')
carnet = input('Digite su numero de carnet: ')
edad = input('Digite su edad: ')
meta = float(input('Cual es su meta de ahorro: '))
esquema = '{}{}{}@{}'

#capturando los elementos de las varibales para la creacion de un correo
correo = nombre[0].lower() + apellido.lower() +carnet+ '@'+dominio
print(correo)

"""otra manera de hacerlo seria 
correo = nombre[0] + apellido + @ + dominio
print(correo.lower())
#cualquiera de las dos maneras funciones
"""
###################################
##### OTRA MANERA DE HACERLO ######
###################################
"""#Ejemplo: creacion de correo con base a los datos del usuario
El correo va a estar compuesto por: 
- primera letra del nombre
- primera letra del apellido
- numero de carnet
- arroba
- dominio
"""
#asi ira estructurado el correo electronico
esquema = '{}{}{}@{}'
descripcion = 'El alumno {} {} con carnet {} de edad {} quiere ahorrar ${:,.2f}'

print(esquema.format(nombre[0],apellido[0],carnet,dominio).lower())
#el format es el FORMATO que se le dara a esquema con base a la estructura que ya le dimos
#Al final ponemos el metodo lower para que todo lo que escribamos, a pesar de usar mayus se imprima en minusculas

print(descripcion.format(nombre,apellido,carnet,edad,meta))

#Ya se ocupemes f-string o format cualquiera es posible