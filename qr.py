import tkinter as tk
from tkinter import ttk
import qrcode

def limpiar_campos():
    # Limpiar los campos de entrada en ambas pestañas
    entrada_texto.delete(0, tk.END)
    entrada_nombre.delete(0, tk.END)
    entrada_enlace.delete(0, tk.END)
    entrada_nombre_enlace.delete(0, tk.END)
    entrada_ssid.delete(0, tk.END)
    entrada_clave.delete(0, tk.END)
    entrada_nombre_wifi.delete(0, tk.END)

def generar_qr_desde_texto():
    texto = entrada_texto.get()
    nombre_archivo = entrada_nombre.get()
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo + ".png")

    resultado.config(text=f"El código QR se ha generado en {nombre_archivo}.png")

    # Limpiar los campos de entrada en ambas pestañas
    limpiar_campos()

def generar_qr_desde_enlace():
    enlace = entrada_enlace.get()
    nombre_archivo = entrada_nombre_enlace.get()

    # Agregar "http://" al enlace si no se proporciona
    if not enlace.startswith("http://") and not enlace.startswith("https://"):
        enlace = "http://" + enlace
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(enlace)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo + ".png")

    resultado.config(text=f"El código QR se ha generado en {nombre_archivo}.png")

    # Limpiar los campos de entrada en ambas pestañas
    limpiar_campos()

def generar_qr_wifi():
    ssid = entrada_ssid.get()
    clave_wifi = entrada_clave.get()
    nombre_archivo = entrada_nombre_wifi.get()
    
    texto_wifi = f"WIFI:T:WPA;S:{ssid};P:{clave_wifi};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto_wifi)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo + ".png")

    resultado.config(text=f"El código QR para la clave de Wi-Fi se ha generado en {nombre_archivo}.png")

    # Limpiar los campos de entrada en ambas pestañas
    limpiar_campos()

ventana = tk.Tk()
ventana.title("Generador de Códigos QR")
ventana.geometry("500x400")  # Establecer el tamaño fijo de la ventana

# Crear pestañas con ttk.Notebook
pestanas = ttk.Notebook(ventana)
pestana_texto = tk.Frame(pestanas)
pestana_enlace = tk.Frame(pestanas)
pestana_wifi = tk.Frame(pestanas)

pestanas.add(pestana_texto, text="Texto")
pestanas.add(pestana_enlace, text="Enlace")
pestanas.add(pestana_wifi, text="Clave Wi-Fi")

pestanas.pack(expand=1, fill="both")

# Pestaña de Texto
etiqueta_texto = tk.Label(pestana_texto, text="Texto:")
etiqueta_texto.pack()
entrada_texto = tk.Entry(pestana_texto)
entrada_texto.pack()
etiqueta_nombre = tk.Label(pestana_texto, text="Nombre del archivo:")
etiqueta_nombre.pack()
entrada_nombre = tk.Entry(pestana_texto)
entrada_nombre.pack()
boton_generar_texto = tk.Button(pestana_texto, text="Generar QR", command=generar_qr_desde_texto)
boton_generar_texto.pack()

# Pestaña de Enlace
etiqueta_enlace = tk.Label(pestana_enlace, text="Enlace:")
etiqueta_enlace.pack()
entrada_enlace = tk.Entry(pestana_enlace)
entrada_enlace.pack()
etiqueta_nombre_enlace = tk.Label(pestana_enlace, text="Nombre del archivo:")
etiqueta_nombre_enlace.pack()
entrada_nombre_enlace = tk.Entry(pestana_enlace)
entrada_nombre_enlace.pack()
boton_generar_enlace = tk.Button(pestana_enlace, text="Generar QR", command=generar_qr_desde_enlace)
boton_generar_enlace.pack()

# Pestaña de Clave Wi-Fi
etiqueta_ssid = tk.Label(pestana_wifi, text="SSID (Nombre de la red Wi-Fi):")
etiqueta_ssid.pack()
entrada_ssid = tk.Entry(pestana_wifi)
entrada_ssid.pack()

etiqueta_clave = tk.Label(pestana_wifi, text="Clave de Wi-Fi:")
etiqueta_clave.pack()
entrada_clave = tk.Entry(pestana_wifi, show="*")  # Para ocultar la clave
entrada_clave.pack()

etiqueta_nombre_wifi = tk.Label(pestana_wifi, text="Nombre del archivo:")
etiqueta_nombre_wifi.pack()
entrada_nombre_wifi = tk.Entry(pestana_wifi)
entrada_nombre_wifi.pack()
boton_generar_wifi = tk.Button(pestana_wifi, text="Generar QR", command=generar_qr_wifi)
boton_generar_wifi.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()