
# input('Ingrese su nombre') 
# >>> Esta manera pide que el usuario ponga un valor pero no lo guarda en la memoria

## Pidale los datos al usuario y cuantos plumones ha ordenado
nombre = input('Ingrese su nombre: ')
apellido = input('Tambien su apellido: ')
precio = 1.25
cantidad = int(input('Digite su orden de plumones: ') )
"""Input es una funcion que captura cadena de texto, es decir STRING
Cuando se pone la cant de numeros de plumones (ej: 7) lo tirara como '7', lo cual lo hace
imposible de poder operar
"""
print(f'El usuario {nombre} {apellido}. Ha ordenado {cantidad} plumones. Su total sera de ${cantidad*precio}')

nombreCompleto = 'Melisa Rivas' #el len considera los espacios
edad = 18
altura = 1.55
mayoria = edad >= 18

print(type(nombre) is int)
print(type(edad) is str)
print(type(altura))

print(len(nombreCompleto)) #El len sirve para ver la longitud de un STRING, no numeros.
#Esto, a pesar que alvin lo enseño, no sirve para mucho
print(nombreCompleto[1:3]) #Incluye el primer numero pero no el ultimo. 
#En el subsetting toma en cuenta del 0 en adelante. 

print(nombreCompleto[0:3:2]) #Esto lo que hace es que toma el primero, no toma el segundo y salta cada 2
#Es decir, sale el M (indice 0), no sale e (1) porque se lo salta y sale l porque es el indice 2