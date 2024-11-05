#definimos la funcion 
def mi_funcion(nombre):
    print(f'Hi, {nombre}')
    print('yo soy meli')
    print('Hola, soy Python')
    print('Hola, soy Java')
#siempre hay que invocar la funcion
mi_funcion('Melisa')

profe = 'Alvin'
def usuario():
    #Oucpamos el global para tener acceso DENTRO DE LA FUNCION a "profe"
    global profe
    #Con el global hacemos que TODO el codigo tenga acceso a la variable usuarios
    global usuarios
    usuarios = 'Marito'
    print(f'Hola {profe}')
    print(f'Hola, {usuarios}')
usuario()

def suma(a, b):
    print(a+b)
suma(5, 7)

print(f'Hola, {usuarios}')