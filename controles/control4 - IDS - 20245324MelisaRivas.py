##########################################################################################
###       Sistema de registro de ventas - Introduccion al Desarrollo de Software       ###
##########################################################################################
"""
Se le pide (si, otra vez), crear un MENU [10 puntos] que permita las siguientes funcionalidades:
    - Crear un pedido
    - Consultar un pedido
    - Salir de la aplicacion

[30 puntos] Crear un pedido, el cual contendrá (por medio de un diccionario):
    - Nombre del cliente
    - Apellido del cliente
    - DETALLE del pedido:
        - Se mostrará el cliente las opciones de código, ademas de la opción S (Salir), la cual
          nos regresará al MENU
        - A medida que el cliente digite una opcion (C, P, Z, L, G) asumiremos 1 unidad
          se irán agregando al pedido
        - Un cliente podrá pedir varias veces un mismo articulo (no hay restriccion)
        - Si digita una opcion de codigo de producto que no existe, seguirá consultando
          hasta que se elija la opción S (Salir)
        - Ejemplos de "Detalle del pedido":
            - ["Z"]
            - ["L","P"]
            - ["C","P","C","G","Z"]
            - ["P","C","P","C"]
[30 puntos] Mostrar un pedido, el cual permitirá consultar el detalle de un pedido con sus datos:
    - La consulta se realizará por medio de apellido (asumiremos que los apellidos no se repiten,
      en todo caso, mostrar la primera coincidencia)
    - La consulta deberá considerar cualquier mezcla de mayusculas y minusculas como válida
    - En caso no hallar coincidencias de ese apellido, deberá indicarlo y continuar solicitando
      el apellido del cliente a buscar.
    - Ejemplo1 de "Consulta de pedido",  >> Apellido del cliente: porTillo
        Nombre: Alvin
        Apellido: Portillo
        Pedido:
            Camisa
            Pantalones
            Camisa
            Gorra
            Zapatos
        Total $161.22
    - Ejemplo de "Consulta de pedido",  >> Apellido del cliente: tiLiano
        Nombre: Javier
        Apellido: Tiliano
        Pedido:
            Lentes
            Pantalones
        Total $65.49
"""
#### Productos ####
online = True
codigo = ("C","P","Z","L","G")
producto =  ("Camisa", "Pantalones", "Zapatos", "Lentes", "Gorra")
precio = (19.99,35.50,75.99,29.99,9.75)

menu = """¡Bienvenidos a la aplicación!
\t 1. Crear un  pedido
\t 2. Consultar un pedido
\t 3. Salir de la aplicacion"""

clientes = []
detallePedido = []

while online:
  print(menu)
  eleccion = input('¿Qué desea hacer?: \n')
  
  if eleccion == '1':
    print('\n#### Seccion de crear un pedido ####')
    nombre = input('Escriba su primer nombre: ').capitalize()
    apellido = input('Escriba su primer apellido: ').capitalize()
    detalle = True

    print('#### Sus datos han sido ingresados ####\n')
    while detalle:
      for i, c in enumerate(codigo):
        print(f"{c} - {producto[i]}")
      pedido = input('Digite su opcion.\n# Presione S para regresar al menú # \t').upper()
      
      usuario = {"Nombre": nombre, "Apellido": apellido, 'Detalle': detallePedido}      

      if pedido in codigo:
        detallePedido.append(pedido)
        print(f'Sus datos son {usuario["Nombre"]} {usuario["Apellido"]}, {usuario["Detalle"]}.\n')
      elif pedido == 'S':
        detalle = False
        detallePedido = []
      else:
        print('Ingrese un codigo disponible. \n')

    clientes.append(usuario)

  elif eleccion == '2':
    encontrado = True

    while encontrado:
      buscar = input('\nConsulta de pedido. \nIngrese el apellido del pedido que desea buscar: ').capitalize()
      
      for cliente in clientes:
        if cliente['Apellido'] == buscar:
          encontrado = False
          total = 0

          print(f'Nombre: {cliente['Nombre']}\nApellido: {cliente['Apellido']}\nPedido:')

          for p in cliente['Detalle']:
            indice = codigo.index(p)
            print(f'- {producto[indice]}')
            total += precio[indice]

          print(f'TOTAL: ${total:,.2f}\n')

        else:
          print('Cliente no encontrado. \n')

  elif eleccion == '3':
    print('¡Vuelve pronto!')
    online = False
  
  else:
    print('Digito no válido.\n')