def persona(nombre, edad=10):
    print(f'E; nombre es {nombre} y la edad {edad}')

#Esto sirve para no tener que poner los parametros en orden y no tener margen de error. 
persona(edad = 19, nombre='Melisa')

#Asignandole valor al parametro de la funcion y no ponerle al momento de llamarla agarrara 
#el valor POR DEFECTO
persona(nombre='Jonathan')