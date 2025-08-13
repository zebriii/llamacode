import shutil
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # Oculta la ventana principal

# Seleccionar archivo origen
archivo_origen = filedialog.askdirectory(title="Selecciona la carpeta origen")
if not archivo_origen:
    print("No seleccionaste archivo origen.")
    exit()

# Seleccionar carpeta destino
carpeta_destino = filedialog.askdirectory(title="Selecciona la carpeta destino")
if not carpeta_destino:
    print("No seleccionaste carpeta destino.")
    exit()

# Construir ruta destino con el mismo nombre de archivo
import os
nombre_archivo = os.path.basename(archivo_origen)
ruta_destino = os.path.join(carpeta_destino, nombre_archivo)

# Mover archivo
shutil.move(archivo_origen, ruta_destino)

print(f"Archivo movido a: {ruta_destino}")
