nombre = "Melisa"
apellido = "Rivas"
nombre_completo = nombre + " " + apellido

edad = 18
meta = 2000.00

# int: Integer, Entero
# str: String, texto (cadena de texto)

texto_completo = nombre_completo + " tiene " + str(edad) + " años, "
texto_completo_f = texto_completo + "y su meta es... " + str(meta)
texto_formateado = f"La meta es... ${meta:,.2f}"

print(nombre)
print(apellido)

print(nombre_completo)
print(texto_completo)
print(texto_completo_f)
print(texto_formateado)