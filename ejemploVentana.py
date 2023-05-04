import tkinter as tk

# Función que se ejecuta al presionar el botón "Aceptar"
def capturar_texto():
    texto_ingresado = entrada.get()
    print("El texto ingresado es:", texto_ingresado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de entrada de texto en Tkinter")

# Crear el campo de entrada y agregarlo a la ventana usando grid()
entrada = tk.Entry(ventana)
entrada.grid(row=0, column=1)

# Crear una etiqueta para el campo de entrada y agregarla a la ventana usando grid()
etiqueta = tk.Label(ventana, text="Ingrese un texto:")
etiqueta.grid(row=0, column=0)

# Crear el botón "Aceptar" y agregarlo a la ventana usando grid()
boton = tk.Button(ventana, text="Aceptar", command=capturar_texto)
boton.grid(row=1, column=1)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()

