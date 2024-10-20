###################################
########### Ejercicio 1 ###########
###################################

dia1 = [5, 8, 5, 9, 1, 4, 8, 8, 6, 5, 9, 10]
dia2 = [7, 6, 0, 4, 6, 0,1, 3, 5, 7, 7, 5]
dia3 = [7, 10, 7, 4, 1, 4, 10, 3, 3, 6, 3, 10]
dia4 = [0, 9, 1, 9, 5, 2, 6, 5, 3, 3, 0, 8 ]
dia5 = [7, 6, 1, 10, 5, 0, 3, 5, 8, 1, 4, 7]
dia6 = [2, 8, 10, 3, 9, 3, 6, 7, 2, 7, 7, 3]

names = ['Justin', 'Jacqueline', 'Allison', 'Alfreda', 'Ina', 'Logan', 'Elsie', 'Jannie', 'Daniel', 'Melissa', 'Carol', 'Catherine']
lastNames = ['Roberts', 'Benton', 'Jacobs', 'Daigle', 'Wilcher', 'Gump', 'Dittmar', 'Baird', 'Le', 'Putnam', 'Cutter', 'Bailey']
pagoHora = [17.75, 17.5, 17.65, 16.90, 17.98, 26.15]

#El orden que aparacen las horas de los dias es correspondiente a los nombres
online = True

while online == True:
    #1. Crenado el menu de la interfaz
    print('\n##### Bienvenido al sistema de consulta ####')
    print('1. Consultar empleados.')
    print('2. Agregar empleados.')
    print('3. Modificar PagoHora.')
    print('4. Consultar pago por empleado.')
    print('5. Salir del sistema. \n')

    eleccion = int(input('Escoja la opcion que desea, de un número del 1 al 5. '))
    
    #2. Mostrando la lista de empleados
    if eleccion == 1:
        print(f'Esta es la lista de empleados. ')
        contador = 0
        indexNames = -1
        indexLastNames = -1
        
        for i in names and lastNames:
            contador +=1
            indexLastNames += 1
            indexNames += 1
            print(f'{contador}. {names[indexNames]} {lastNames[indexLastNames]}')
    
    #3. Agregando nuevo elemento a los arrays
    elif eleccion == 2:  
        print('¡Bienvenido a la seccion de agregar empleado! Ingrese los siguiente datos')
        newName = input('Nombre del empleado: ')
        newLastName = input('Apellido del empleado: ')
        horasDia1 = int(input('Horas del dia 1: '))
        horasDia2 = int(input('Horas del dia 2: '))
        horasDia3 = int(input('Horas del dia 3: '))
        horasDia4 = int(input('Horas del dia 4: '))
        horasDia5 = int(input('Horas del dia 5: '))
        horasDia6 = int(input('Horas del dia 6: '))

        #Agregandolos con .append
        names.append(newName)
        lastNames.append(newLastName)
        dia1.append(horasDia1)
        dia2.append(horasDia2)
        dia3.append(horasDia3)
        dia4.append(horasDia4)
        dia5.append(horasDia5)
        dia6.append(horasDia6)

        print(f'Los datos han sido guardados exitosamente: {newName} {newLastName}')
    
    #4. Modificando el pagoHora
    elif eleccion == 3:
        print(pagoHora)
        diaModificar = int(input('!Bienvenido a la seccion de agregar empleado! ¿Qué día desea modificar (1 - 6)?: '))
        posicion = pagoHora.count(diaModificar)
        if diaModificar == 1:
            update = float(input('Ingrese el valor que desea actualizar: '))
            pagoHora[posicion] = update
            print(pagoHora)
        elif diaModificar == 2:
            update = float(input("Ingrese el valor que desea actualizar: "))
            pagoHora[posicion+1] = update
            print(pagoHora)
        elif diaModificar == 3:
            update = float(input("Ingrese el valor que desea actualizar: "))
            pagoHora[posicion+2] = update
            print(pagoHora)
        elif diaModificar == 4:
            update = float(input("Ingrese el valor que desea actualizar: "))
            pagoHora[posicion+3] = update
            print(pagoHora)
        elif diaModificar == 5:
            update = float(input("Ingrese el valor que desea actualizar: "))
            pagoHora[posicion+4] = update
            print(pagoHora)
        elif diaModificar == 6:
            update = float(input("Ingrese el valor que desea actualizar: "))
            pagoHora[posicion+5] = update
            print(pagoHora)
        else:
            print('Ingrese un número del 1 al 6.')

    #4. Consultado pago por empleado
    elif eleccion == 4:
        buscarLast = input('Ingrese el apellido del empleado que busca: ')
    
        if  buscarLast in lastNames:
            numBuscar = lastNames.index(buscarLast)
            pagoTotal = ((dia1[numBuscar]* pagoHora[0]) + (dia2[numBuscar]* pagoHora[1])+ (dia3[numBuscar]* pagoHora[2])+ (dia4[numBuscar] * pagoHora[3])+ (dia5[numBuscar] * pagoHora[4])+ (dia6[numBuscar] * pagoHora[5]))
            print(f'El empleado {names[numBuscar]} {lastNames[numBuscar]} recibe un pago total de ${pagoTotal:,.2f}')
        else:
            print("Ese nombre no existe. Agregalo y regresa pronto")
    
    #Dando la opcion que el usuario pueda salir del sistema
    elif eleccion == 5:
        print('Saliendo del sistema. ¡Vuelve pronto!')
        online = False
    
    #Asegurandonos que el usuario sepa que tiene que ingresar un numero del 1 al 5
    else:
        print('¡Cuidado! Ingrese un numero dentro de 1 - 5.')



