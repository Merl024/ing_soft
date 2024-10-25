
online = True
personas = []
people = ["Juan", 'Maria', 'Sebastian', 'Marta']
ages = [23, 21, 20, 19]
p1 = ['Juan', 23]
p2 = ['Maria', 21]
p3 = ['Sebastian', 20]
p4 = ['Marta', 19]

#Ejemplo de lista de listas. 
personas = [p1, p2, p3, p4]

#Subsetting de subsetting, es decir que a la lista personas, quiero la primera lista (que esta en la posicion 0)
# De esta primera lista, que imprima el primer DATO
# print(personas[0][0])

for i in personas:
    print(f'Name: {i[0]}, Age: {i[1]}')

name = input('Ingrese su nombre: ')
age = int(input('Ingrese su edad: '))
p5 = [name, age]

personas.append(p5)
for i in personas:
    print(f'Name: {i[0]}, Age: {i[1]}')
