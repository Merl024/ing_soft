
alumnos = ['Alisson', 'Mario', 'Dante', 'Christian', 'Andre', 'Melisa']

print(len(alumnos))

alumno1 = [20245324, 'Melisa', 18, 1.55, False]

print(alumno1)

alumno1[2] = 19
print(alumno1)
print(alumno1.index(19))

#.append() sirve para agregar elementos a variables ya existentes. Agrega
alumnoNuevo = ['Ale', 'Lis']
alumnos.append(alumnoNuevo)

#Otra manera
alumnos += alumnoNuevo
print(alumnos)