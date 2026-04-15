import pyautogui

import tkinter as tk
from tkinter import ttk

# Ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Clicker")
ventana_principal.resizable(False, False)
ventana_principal.configure(bg="#2b2b2b")

# Variables
horas = tk.StringVar(value="0")
minutos = tk.StringVar(value="0")
segundos = tk.StringVar(value="0")
milisegundos = tk.StringVar(value="0")

cant_clicks_infinitos = tk.StringVar(value="Infinito")# "infinito" | "veces"
cant_veces = tk.StringVar(value="1")

boton_del_mouse = tk.StringVar(value="Derecho")
tipo_de_click = tk.StringVar(value="Unico")

posicion_tipòn = tk.StringVar(value="Actual")# "Actual" | "Fija"
pos_x = tk.StringVar(value="0")
pos_y = tk.StringVar(value="0")

tecla_comenzar = tk.StringVar(value="")
tecla_detener = tk.StringVar(value="")

# Colores y Fuentes

COLOR_FONDO = "#2b2b2b"
COLOR_MARCO = "#3c3c3c"
COLOR_ENCABEZADO = "#78AE68"
COLOR_TEXTO = "#e0e0e0"
COLOR_ENTRADA = "#1e1e1e"
COLOR_BORDE = "#555555"
COLOR_BOTON = "#3c3c3c"
COLOR_BOTON_TEXTO = "#e0e0e0"
FUENTE = ("Consolas", 9)
FUENTE_TITULO = ("Consolas", 9, "bold")

# Funciones auxiliares
def marco_con_titulo(padre, titulo, fila, columna, rowspan=1, columnspan=1, padx=6, pady=4):
    """Devuelve un LabelFrame estilizado."""
    frame = tk.LabelFrame(
        padre, text=titulo,
        bg=COLOR_MARCO, fg=COLOR_TEXTO,
        font=FUENTE_TITULO,
        bd=1, relief="groove",
        labelanchor="nw"
    )
    frame.grid(row=fila, column=columna, rowspan=rowspan, columnspan=columnspan,
               padx=padx, pady=pady, sticky="nsew")
    return frame