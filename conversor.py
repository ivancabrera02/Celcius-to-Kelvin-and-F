#importamos las librerías

import tkinter as tk
from tkinter import ttk

#funcion para la lógica

def convertir_temperatura():
    temp_celsius = float(caja_temp_celsius.get())
    temp_kelvin = temp_celsius + 273.15
    temp_fahrenheit = temp_celsius*1.8 + 32
    kelvin_label.config(text=f"Temperatura en K: {temp_kelvin}")
    fahrenheit_label.config(text=f"Temperatura en ºF: {temp_fahrenheit}")

#lanzamos la ventana, titulo y tamaño

ventana = tk.Tk()
ventana.title("Conversor de temperatura")
ventana.config(width=450, height=350)

#texto e input

celsius_label = ttk.Label(text="Temperatura en ºC:")
celsius_label.place(x=20, y=20)

caja_temp_celsius = ttk.Entry()
caja_temp_celsius.place(x=140, y=20, width=80)

#boton

boton = ttk.Button(text="Convertir", command=convertir_temperatura)
boton.place(x=20, y=60)

#texto del label y kelvin

kelvin_label = ttk.Label(text="Temperatura en Kelvin: ...")
kelvin_label.place(x=20, y=120)

fahrenheit_label = ttk.Label(text="Temperatura en Fahrenheit: ...")
fahrenheit_label.place(x=20, y=160)

ventana.mainloop()