#\t es tabulacion, \n es salto de linea

online = True
person = []
people = ["Juan", 'Maria', 'Sebastian', 'Marta']
ages = [23, 21, 20, 19]

# Las triples comillas sirve para escribir textos de mas de una linea
menu = """ Elija una de las siguiente opciones
        1. Consultar people
        2. Crear people                
        3. Salir"""

while online: 
    print(menu)
    opcion = int(input('\tOpcion: '))
    if opcion == 3:
        online = False
    elif opcion == 1:
        if len(people) > 0:
            for n in range(len(people)):
                print(str(n+1)+ ". " + people[n]+ " - " + str(ages[n]))
        else: 
            print('No hay registros')
