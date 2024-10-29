##########################################################################################
###       Sistema de registro de ventas - Introduccion al Desarrollo de Software       ###
##########################################################################################

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
  eleccion = int(input('¿Qué desea hacer?: \n'))
  
  if eleccion == 1:
    print('\n#### Seccion de crear un pedido ####')
    nombre = input('Escriba su primer nombre: ').capitalize()
    apellido = input('Escriba su primer apellido: ').capitalize()
    detalle = True

    print('#### Sus datos han sido ingresados ####\n')
    while detalle: 
      print(codigo)
      pedido = input('Digite su opcion.\n# Presione 5 para regresar al menú # \t').upper()
      
      usuario = {"Nombre": nombre, "Apellido": apellido, 'Detalle': detallePedido}      

      if pedido in codigo:
        detallePedido.append(pedido)
        print(f'Sus datos son {usuario["Nombre"]} {usuario["Apellido"]}, {usuario["Detalle"]}.\n')
      else:
        print('Ingrese un codigo disponible. \n')

      if pedido == '5':
        detalle = False
        detallePedido = []

    clientes.append(usuario)

  elif eleccion == 2:
    buscar = input('\nConsulta de pedido. \nIngrese el apellido del pedido que desea buscar: ').capitalize()
    encontrado = False

    for cliente in clientes:
      if cliente['Apellido'] == buscar:
        encontrado = True
        total = 0

        for p in cliente['Detalle']:
          indice = codigo.index(p)
          print(f'- {producto[indice]}')
          total += precio[indice]

        print(f'TOTAL: ${total:,.2f}\n')

    if not encontrado:
      print('Cliente no encontrado. \n')

  elif eleccion == 3:
    print('¡Vuelve pronto!')
    online = False