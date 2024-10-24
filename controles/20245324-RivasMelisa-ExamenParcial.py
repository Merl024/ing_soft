###################################
########### Ejercicio 1 ###########
###################################

##############################################################################################################################
#### Disclamer: cada una de las cosas aqui fue lo que se me ocurrio, se pudo haber hecho de otra manera e igual funcionar ####
##############################################################################################################################

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

#Declaramos una variable en true para luego ocuparla en while
online = True

# Decimos que mientras Online sea = a True, este realizara una serie de acciones.
while online:
    #1. Crenado el menu de la interfaz
    print('\n##### Bienvenido al sistema de consulta ####')
    print('1. Consultar empleados.')
    print('2. Agregar empleados.')
    print('3. Modificar PagoHora.')
    print('4. Consultar pago por empleado.')
    print('5. Salir del sistema. \n')

    # Guardamos la eleccion del cliente en una variable 
    eleccion = int(input('Escoja la opcion que desea, de un número del 1 al 5. '))
    #Con base a la eleccion del cliente puede pasar esto o aquello
    
    #2. Mostrando la lista de empleados
    #Si el cliente pone el #1, entoncees
    if eleccion == 1:

        print(f'Esta es la lista de empleados. ')
        
        #Esto lo hice para ocuparlo en el for, se explica mas adelante
        contador = 0

        """Aqui indexNames e indexLastnames son listas y sabemos que los indices empiezan a partir del numero 0, si yo pongo que el index
        de nombres y apellidos es -1, estoy diciendo que NO HAY NADA en la lista"""
        indexNames = -1
        indexLastNames = -1
        
        #Aqui i es cada uno de los elementos en la lista name y lastNames. Se pudo haber hecho de otra manera pero esta fue la que me furulo a mi
        for i in names and lastNames:
            """Mi objetivo con el contador era que me enlistara de forma AUTOMATICA cada unos de los nombres de las listas. 
            Esto era lo que queria que imprimiera: 
            1. 
            2. 
            3...
            y asi. Como arriba ya habia declarado que 'contador' es igual a 0, quiero que por cada iteracion que hace sume +1 al numero anterior. 
            Es decir, en la primera iteracion (o vuelta), contador es igual a 0 + 1, o sea que imprimira el numero 1.
            En la segunda vuelta, agarra el valor del contador de la vuelta anterior y le suma +1, 1+1=2, imprimira 2. Y asi hasta que termine con todos
            los valores de las listas"""
            contador +=1

            """Tantoc con el indice de Names y lastNames, habia dicho que tenia indice -1, y por cada iteracion (igual que con el contador) quiero
            que le sume +1. Es decir, indexLastNames = -1 + 1 = 0, imprimira el apellido en el indice (o posicion) 0
            En la segunda iteracion, indexLastNames = 0 +1 = 1, imprime el apellido en el indice 1, y asi con todos"""
            indexLastNames += 1
            indexNames += 1

            """Por ultimo, imprimimos el contador y la lista nombres y apellidos, puse el indexNames e indexLastNames en [ ] porque eso indica indice
            o posicion de la lista. """
            print(f'{contador}. {names[indexNames]} {lastNames[indexLastNames]}')
    
    #3. Agregando nuevo elemento a los arrays
    # Si el cliente escribe el numero 2, pasara lo siguiente
    elif eleccion == 2:  
        #Pedimos todos los datos que pedia el parcial
        print('¡Bienvenido a la seccion de agregar empleado! Ingrese los siguiente datos')
        newName = input('Nombre del empleado: ')
        newLastName = input('Apellido del empleado: ')
        horasDia1 = int(input('Horas del dia 1: '))
        horasDia2 = int(input('Horas del dia 2: '))
        horasDia3 = int(input('Horas del dia 3: '))
        horasDia4 = int(input('Horas del dia 4: '))
        horasDia5 = int(input('Horas del dia 5: '))
        horasDia6 = int(input('Horas del dia 6: '))

        #Agregandolos con .append()
        """.append() es metodo (una accion ya establecida en el lenguaje Python) que ayuda a AGREGAR en la ULTIMA POSICION lo que el
        cliente escribio arriba.
        La estructura es
        nombreDeLista.append(nombre del dato a agregar ¡SIN ESPACIOS!)"""
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
    #Lo que pasa si se escoge la opcion 3   
    elif eleccion == 3:
        print(pagoHora)
        #Primero le preguntamos que dia desea modificar
        diaModificar = int(input('!Bienvenido a la seccion de agregar empleado! ¿Qué día desea modificar (1 - 6)?: '))
        
        """Con base a su respuesta, vamos a ocuparla como posicion de INDICE en la lista pagoHora.
        Por ejemplo, si el usuario dice que quiere modificar el dato del dia2, el indice en la lista seria el [1], porque dia 1 [0],
        dia 2[1] y asi """
        posicion = pagoHora.count(diaModificar)

        ############ OJO: aqui se pudo haber hecho con un for, pero no medio la cabeza para hacerlo, continuemos ############
        ## Si el usuario quiere modificar el dia 1 hara lo siguiente.
        if diaModificar == 1:
            update = float(input('Ingrese el valor que desea actualizar: '))
            """Aqui le estoy diciendo que el valor que acaba de ingresar el usuario lo sistituya por la posicion que encontramoe en la
            linea 116 de la lista pagoHora"""
            pagoHora[posicion] = update
            print(pagoHora)
        elif diaModificar == 2:
            update = float(input("Ingrese el valor que desea actualizar: "))

            """Aqui y en las demas es CASI la misma logica, solo que a posicion se le suma +1 acumulativo para ir agarrando el indice
            que pide el usuario """
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
        """######### REPITO #########
        Esto se pudo haber hecho de otra manera mucho mas sencilla y logica, pero fue lo unico que se me ocurrio"""
    #4. Consultado pago por empleado
    elif eleccion == 4:
        #le pedimos el apellido al usuario
        buscarLast = input('Ingrese el apellido del empleado que busca: ')
    
    #Con base al apellido que ponga el usuario, lo buscamos en la lista lastNames.
        if  buscarLast in lastNames:
            # numBuscar es que en la lista de apellidos busque EL INDICE o POSICION del apellido que ingreso el usuario
            numBuscar = lastNames.index(buscarLast)
            #Con base a ese indice, lo buscamos en todas las listas de dias y lo multiplicamos con cada una de los pagoHora
            pagoTotal = ((dia1[numBuscar]* pagoHora[0]) + 
                         (dia2[numBuscar]* pagoHora[1]) + 
                         (dia3[numBuscar]* pagoHora[2]) + 
                         (dia4[numBuscar] * pagoHora[3]) + 
                         (dia5[numBuscar] * pagoHora[4]) + 
                         (dia6[numBuscar] * pagoHora[5]))
            #Imprmimos el nombre y apellido del indice numBuscar y el pago total sera escrito con comas y dos decimales
            print(f'El empleado {names[numBuscar]} {lastNames[numBuscar]} recibe un pago total de ${pagoTotal:,.2f}')
        else:
            #Si escribe un nombre o apellido que no esta en la lista tiramos este mensaje
            print("Ese nombre no existe. Agregalo y regresa pronto")
    
    #Dando la opcion que el usuario pueda salir del sistema
    elif eleccion == 5:
        """Para salir de la 'aplicacion', tenemos que RE DEFINIR la variable online.
        Como habia dicho antes, MIENTRAS online SEA TRUE hara tales acciones, entonces, para que deje de cumplir esas acciones (y para salir
        de la aplicacion), decimos que online sera igual a False y automaticamente la app se cierra. """
        print('Saliendo del sistema. ¡Vuelve pronto!')
        online = False
    
    #Asegurandonos que el usuario sepa que tiene que ingresar un numero del 1 al 5
    else:
        print('¡Cuidado! Ingrese un numero dentro de 1 - 5.')


