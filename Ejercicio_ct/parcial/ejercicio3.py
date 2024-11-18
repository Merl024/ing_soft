## Ejercicio 3
"""
Elabore un menu en la interfaz de la Terminal, el cual contenga las siguientes opciones:
1. Ingresar nuevo alumno
2. Editar alumno existente
3. Borrar alumno existente
4. Consultar alumno existente
5. Salir del sistema.

1. Permitirá, mientras esté en ejecución el programa, capturar (cada valor será preguntado al usuario) los
datos del alumno:
    a. Nombre
    b. Apellido
    c. Carnet
    d. Edad
    e. Fruta favorita
2. A partir del numero de carnet, permitirá editar los valores existentes de un alumno ya ingresado. Es decir,
similar al punto anterior, donde le va pidiendo los datos, primero le pedirá el número de carnet (si el carnet
no existen en los datos registrados, deberá indicarlo), si el carnet existe, le pedirá Nombre, Apellido, Edad y
Fruta Favorita, y estos serán los nuevos valores del carnet ingresado.
3. Similar al anterior, le pedirá al usuario el número de carnet, si este carnet existe, le mostrará los datos
que corresponden a ese carnet, con la pregunta "Está seguro de borrar los datos del alumno... (datos del alumno): Si/No. Si Escribe Si, se borrarán, sino regresa al menú.
4. Le pedirá al usuario escribir el nombre del alumno a consultar. Esta busqueda podrá hacerse tanto en minusculas,
mayusculas o una combinación. Así por ejemplo, si se busca al alumno "Javier", pero el usuario escribió "javiEr",
el valor será dado por válido, y mostrará los datos que pertenecen a ese alumno.
5. Al elegir la opción 5, salir del menú.

Notas:
Para este ejercicio, y evitar resultados fortuitos, este script ya deberá contener los datos de 3 alumnos ficticios.
Si el usuario no ingresa una de la opciones válidas en el menú (1-5), deberá indicar un mensaje de error y mostrar
de nuevo el menú.
"""

online = True

nombres = []
apellidos = []
carnets = []
edades = []
frutaFavs = []
alumnos = [nombres, apellidos, carnets, edades, frutaFavs]

while online == True:
    #Haciendo que escoga a que parte del menu quiere ingresar
    print('#### Bienvenido al registro academico ####')
    print('1. Ingresar nuevo alumno')
    print('2. Editar alumno existente')
    print('3. Borrar alumno existente')
    print('4. Consultar alumno existente')
    print('5. Salir del sistema.')
    print('6. Consultar datos existentes')
    eleccion = int(input('Ingrese un numero del 1 a 5: '))

    if eleccion == 1:
        print('Ingrese los siguientes datos')
        #Obtenemos los datos necesarios
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        carnet = int(input('Carnet: '))
        edad = int(input('Edad: '))
        frutaFav = input('Fruta favorita: ')
        #Los guardamos en los array
        nombres.append(nombre)
        apellidos.append(apellido)
        carnets.append(carnet)
        edades.append(edad)
        frutaFavs.append(frutaFav)

        print('La informacion ha sido guardada con exito!')
    
    elif eleccion == 2:
        buscar = int(input('Ingrese el numero de carnet: '))

        if buscar not in carnets:
            print('No se encontro el carnet ingresado. Intente de nuevo.')
        else:  
            posicion = carnets.index(buscar)
            #Estamos sobreescribieno los datos sobre lo que ya existia
            nombreNew = input('Nombre: ')
            nombres[posicion] = nombreNew

            apellidoNew = input('Apellido: ')
            apellidos[posicion] = apellidoNew
            
            carnetNew = int(input('Carnet: '))
            carnets[posicion] = carnetNew
            
            edadNew = int(input('Edad: '))
            edades[posicion] = edadNew
            
            frutaFavNew = input('Fruta favorita: ')
            frutaFavs[posicion] = frutaFavNew

            print('La informacion ha sido actualizada')
    
    elif eleccion == 3:
        borrar = int(input('Ingrese el carnet del estudiante que desea eliminar: '))
        posicionBorrar = carnets.index(borrar)

        if borrar not in carnets:
            print('No existe el numero de carnet ingresado. Intente de nuevo.')
        else:
            print('Los datos a borrar son los siguiente: ')
            print(nombres[posicionBorrar], apellidos[posicionBorrar], carnets[posicionBorrar], edades[posicionBorrar], frutaFavs[posicionBorrar])

            decision = input('Esta segura que desea eliminarlo (Si/No): ').lower()
            if decision == 'si':
                nombres.remove(nombres[posicionBorrar])
                apellidos.remove(apellidos[posicionBorrar])
                edades.remove(edades[posicionBorrar])
                carnets.remove(carnets[posicionBorrar])
                frutaFavs.remove(frutaFavs[posicionBorrar])
                print('Eliminado exitosamente')
            elif decision == 'no':
                print('Entendido! Regresando al menu')
            else:
                print('Respuesta invalida')
    
    elif eleccion == 4:
        nombreBuscar = input('Ingrese el nombre del alumno que desea buscar: ').lower()
        #Se pone -1 para poder empezar a buscar desde el indice 0
        posicionBuscar = -1

        for i in range(len(nombres)):
            if nombreBuscar == nombres[i].lower():
                posicionBuscar = i

        if posicionBuscar == -1:
            print('No existe')
        else:
            print('La informacion es la siguiente: ')
            print(nombres[posicionBuscar], apellidos[posicionBuscar], carnets[posicionBuscar], edades[posicionBuscar], frutaFavs[posicionBuscar])

    elif eleccion == 6:
        if len(nombres) > 0 :
            print('Datos existentes:')
            for idx,(n, a, c, e, f) in enumerate(zip(nombres, apellidos, carnets, edades, frutaFavs)):
                print(f'{idx+1}. Nombre: {n}, Apellido: {a}, Carnet: {c}, Edad: {e}, Fruta Favorita: {f}')
        elif len(nombres) <= 0:
            print('No hay registros')
    elif eleccion == 5:
        print('Saliendo de la aplicacion')
        online = False
        
    else: 
        print('Ingrese una opcion valida')
