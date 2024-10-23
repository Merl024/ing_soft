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
        #     # Esta es una manera de resolverlo #
        #     for n in range(len(people)):
        #     print(str(n+1)+ ". " + people[n]+ " - " + str(ages[n]))

        #     # Esta es otra manera de resolverlo #
        #     #El enumarate enumera cada uno de los objetos (Los valores que estan dentro de las listas)
        #     #El enumarate imprime el indice y el objeto.
        #     for index,name in enumerate(people):
        #     # Se le suma uno porque los indices empiezan desde 0 y se le suma el uno para que, cuando lo imprima, 
        #     # empiece a enumerar desde 1
        #         print(index+1, name)

        
            contador = 0
            #zip es agarrar dos listas y que se comporten como una
            for n,a in zip(people, ages):
            #Donde n es el nombre que esta dentro de people y a son las edades de ages
                contador += 1
                print(f'{contador}. {n} {a}')

        else: 
            print('No hay registros')
