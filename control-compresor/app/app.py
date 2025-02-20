import serial
import tkinter as tk

# Configura la conexión serial (ajusta el puerto según tu sistema)
ser = serial.Serial('COM3', 9600)  # 'COM3' es un ejemplo; usa el puerto correcto en tu sistema

def enviar_intensidad():
    intensidad = slider.get()  # Obtiene el valor del deslizador (0-255)
    ser.write(str(intensidad).encode())  # Envia el valor de intensidad a Arduino

# Configura la interfaz gráfica
root = tk.Tk()
root.title("Control de Compresor de Aire")

# Crea un deslizador
slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Intensidad")
slider.pack()

# Botón para enviar la intensidad a Arduino
btn_enviar = tk.Button(root, text="Enviar Intensidad", command=enviar_intensidad)
btn_enviar.pack()

# Inicia la interfaz gráfica
root.mainloop()