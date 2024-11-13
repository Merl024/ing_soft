# EXCEPCIONES Y CLASES
# son para administrar errores que surgen durante la ejecución de un programa
# tipos de errores: sintaxis (falta de llave, etc), ejecución (falta variable, función, etc), 
# >> lógicos ("sin errores" pero con datos erróneos)

# SINTAXIS DE UN BLOQUE TRY-EXCEPT
# try: bloque de código que puede generar un error
 #   try:
 #      statement(s)
  #   except [expression [as target]]:
 #      statement(s)

try:
    ingreso = int(input("Digite el monto: "))
    impuesto = ingreso * 0.1
except:
    print("El valor ingresado no es válido.")
else:
    #Lo que han hecho aqui es se a puesto la logica en el try, si tira error pues se encapsula en el except 
    # sino (ELSE) se hace lo siguiente
    print(f"El impuesto a pagar es de: {impuesto:,.2f}")
finally: # independientemente de error o no, se ejecuta
    print("Está línea igual se va a ejecutar.")

# try - se indica que si try no devuelve una excepción, el bloque de código será ejecutado
# except - es lo que correrá, si try da error