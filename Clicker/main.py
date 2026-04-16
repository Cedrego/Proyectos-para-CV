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

cant_veces = tk.StringVar(value="1") # "0" para infinito

boton_del_mouse = tk.StringVar(value="Derecho")
tipo_de_click = tk.StringVar(value="Unico")# "Unico" | "Doble"

posicion_tipo = tk.StringVar(value="Actual")# "Actual" | "Fija"
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

#Contenedor con un borde y un título en el borde (como los recuadros "Intervalo de clic", etc). Recibe el padre donde se va a colocar, 
# el título, la posición en la grilla (fila y columna), y opcionalmente el rowspan, columnspan, y los padding. 
# Devuelve el LabelFrame listo para colocar con .grid().
def marco_con_titulo(padre, titulo, fila, columna, rowspan=1, columnspan=1, padx=6, pady=4):
    """Devuelve un LabelFrame estilizado."""
    frame = tk.LabelFrame(
        padre, text=titulo,
        bg=COLOR_MARCO, fg=COLOR_TEXTO,
        font=FUENTE_TITULO,
        bd=1, relief="groove",
        labelanchor="nw"
    )
    frame.grid(row=fila, column=columna, rowspan=rowspan, columnspan=columnspan, padx=padx, pady=pady, sticky="nsew")
    return frame

# Crea un Entry, que es simplemente un campo de texto donde el usuario escribe. La función lo estiliza con los colores oscuros del tema y
# lo vincula a una StringVar. Devuelve el widget listo para colocarlo en la grilla con .grid().
def entrada(padre, textvariable, ancho=5):
    return tk.Entry(
        padre, textvariable=textvariable, width=ancho,
        bg=COLOR_ENTRADA, fg=COLOR_TEXTO,
        insertbackground=COLOR_TEXTO,
        relief="sunken", bd=1, font=FUENTE
    )
    
#Crea un Button estilizado con los colores del tema, un cursor de manito al pasar por encima, y 
# un comando opcional que se ejecuta al hacer clic. También devuelve el widget listo para colocarlo.
def boton(padre, texto, comando=None, ancho=16):
    return tk.Button(
        padre, text=texto, command=comando, width=ancho,
        bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
        activebackground="#505050", activeforeground=COLOR_TEXTO,
        relief="raised", bd=1, font=FUENTE, cursor="hand2"
    )

#Crea un Combobox de ttk, que es una lista desplegable. Recibe los valores posibles,
# la variable vinculada y el ancho. Lo pone en modo readonly para que el usuario solo pueda elegir opciones de la lista y 
# no escribir texto libre. También devuelve el widget listo para colocar.
def combo(padre, valores, variable, ancho=10):
    cb = ttk.Combobox(
        padre, values=valores, textvariable=variable,
        width=ancho, state="readonly", font=FUENTE
    )
    cb.style = "Dark.TCombobox"
    return cb

# Estilo ttk
# Personalizar la apariencia de los widgets "modernos" de la librería ttk, como el Combobox.
estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("Dark.TCombobox", fieldbackground=COLOR_ENTRADA, background=COLOR_BOTON, foreground=COLOR_TEXTO, arrowcolor=COLOR_TEXTO,
                 selectbackground=COLOR_ENTRADA, selectforeground=COLOR_TEXTO)
estilo.map("Dark.TCombobox", fieldbackground=[("readonly", COLOR_ENTRADA)], foreground=[("readonly", COLOR_TEXTO)])

#  Contenedor principal
# Frame que se coloca directamente dentro de la ventana principal y actúa como base sobre la que se construye toda la UI.
contenedor = tk.Frame(ventana_principal, bg=COLOR_FONDO, padx=8, pady=8)
contenedor.pack(fill="both", expand=True)

# Intervalo de clic <--
frame_intervalo = marco_con_titulo(contenedor, "Intervalo de clic", 0, 0, columnspan=2)
# Etiquetas y entradas para horas, minutos, segundos y milisegundos. Se colocan en una grilla dentro del frame_intervalo,
# con un poco de padding entre ellas para que no queden pegadas. Cada entrada está vinculada a una StringVar que almacena
# el valor ingresado por el usuario. Las etiquetas indican qué unidad de tiempo corresponde a cada entrada.
tk.Label(frame_intervalo, text="horas",        bg=COLOR_MARCO, fg=COLOR_TEXTO, font=FUENTE).grid(row=0, column=1, padx=(0,6))
tk.Label(frame_intervalo, text="minutos",      bg=COLOR_MARCO, fg=COLOR_TEXTO, font=FUENTE).grid(row=0, column=3, padx=(0,6))
tk.Label(frame_intervalo, text="segundos",     bg=COLOR_MARCO, fg=COLOR_TEXTO, font=FUENTE).grid(row=0, column=5, padx=(0,6))
tk.Label(frame_intervalo, text="milisegundos", bg=COLOR_MARCO, fg=COLOR_TEXTO, font=FUENTE).grid(row=0, column=7, padx=(0,4))
entrada(frame_intervalo, horas,        ancho=4).grid(row=0, column=0, padx=(6,2), pady=6)
entrada(frame_intervalo, minutos,      ancho=4).grid(row=0, column=2, padx=(0,2))
entrada(frame_intervalo, segundos,     ancho=4).grid(row=0, column=4, padx=(0,2))
entrada(frame_intervalo, milisegundos, ancho=5).grid(row=0, column=6, padx=(0,2))

# Cantidad de clicks y Botón de clic <--
frame_cantidad = marco_con_titulo(contenedor, "Cantidad de clicks", 1, 0)
frame_boton    = marco_con_titulo(contenedor, "Boton de clic",       1, 1)

# — Cantidad —
tk.Label(frame_cantidad, text="Veces (0 = infinito)", bg=COLOR_MARCO, fg=COLOR_TEXTO, font=FUENTE).grid(row=0, column=0, padx=6, pady=6)
entrada(frame_cantidad, cant_veces, ancho=6).grid(row=0, column=1, padx=4, pady=6)

# — Botón de clic —
tk.Label(frame_boton, text="Boton del Mouse:", bg=COLOR_MARCO, fg=COLOR_TEXTO, font=FUENTE).grid(row=0, column=0, sticky="w", padx=6, pady=(6,2))
combo_boton = combo(frame_boton, ["Derecho", "Izquierdo", "Medio"], boton_del_mouse , ancho=10)
combo_boton.grid(row=0, column=1, padx=6, pady=(6,2))

tk.Label(frame_boton, text="Tipo de clic:", bg=COLOR_MARCO, fg=COLOR_TEXTO, font=FUENTE).grid(row=1, column=0, sticky="w", padx=6, pady=(2,6))
combo_tipo = combo(frame_boton, ["Unico", "Doble"], tipo_de_click, ancho=10)
combo_tipo.grid(row=1, column=1, padx=6, pady=(2,6))

combo_boton.configure(style="Dark.TCombobox")
combo_tipo.configure(style="Dark.TCombobox")

# Posicion del Cursor <--
frame_posicion = marco_con_titulo(contenedor, "Posicion del cursor", 2, 0, columnspan=2)

rb_actual = tk.Radiobutton(
    frame_posicion, text="Ubicación actual del cursor",
    variable=posicion_tipo, value="actual",
    bg=COLOR_MARCO, fg=COLOR_TEXTO, selectcolor=COLOR_ENTRADA,
    activebackground=COLOR_MARCO, font=FUENTE
)
rb_actual.grid(row=0, column=0, columnspan=4, sticky="w", padx=6, pady=(6,2))

rb_fija = tk.Radiobutton(
    frame_posicion, text="Ubicación fija",
    variable=posicion_tipo, value="fija",
    bg=COLOR_MARCO, fg=COLOR_TEXTO, selectcolor=COLOR_ENTRADA,
    activebackground=COLOR_MARCO, font=FUENTE
)
rb_fija.grid(row=1, column=0, sticky="w", padx=6, pady=(0,6))

entrada(frame_posicion, pos_x, ancho=6).grid(row=1, column=1, padx=(4,0))
tk.Label(frame_posicion, text="X", bg=COLOR_MARCO, fg=COLOR_TEXTO, font=FUENTE).grid(row=1, column=2, padx=(2,6))
entrada(frame_posicion, pos_y, ancho=6).grid(row=1, column=3, padx=(4,0))
tk.Label(frame_posicion, text="Y", bg=COLOR_MARCO, fg=COLOR_TEXTO, font=FUENTE).grid(row=1, column=4, padx=(2,6))

def elegir_ubicacion():
    """El amigo implementará la lógica aquí."""
    pass

boton(frame_posicion, "Elegir Ubicación", elegir_ubicacion, ancho=14).grid(row=1, column=5, padx=8)

#Botones de control <--
frame_control = tk.Frame(contenedor, bg=COLOR_FONDO)
frame_control.grid(row=3, column=0, columnspan=2, pady=(4, 2), sticky="ew")
# Están vacías, son los puntos de conexión donde tu Thiago llamara a las funciones con la logica.
def iniciar():
    pass

def detener():
    pass

def reiniciar_ajustes():
    pass

def abrir_ajustes():
    ventana_ajustes.deiconify()
    ventana_ajustes.lift()

boton(frame_control, "Comienzo(8)", iniciar,          ancho=18).grid(row=0, column=0, padx=6, pady=2)
boton(frame_control, "Detener(9)",  detener,          ancho=18).grid(row=0, column=1, padx=6, pady=2)
boton(frame_control, "Reiniciar Ajustes", reiniciar_ajustes, ancho=18).grid(row=1, column=0, padx=6, pady=2)
boton(frame_control, "Ajustes ⚙",  abrir_ajustes,    ancho=18).grid(row=1, column=1, padx=6, pady=2)

# Ajustes de Tecla <--
#Toplevel crea una ventana separada que depende de la principal. El withdraw() la oculta al inicio y 
# solo aparece cuando el usuario presiona el botón "Ajustes".
ventana_ajustes = tk.Toplevel(ventana_principal)
ventana_ajustes.title("Ajustes de Tecla")
ventana_ajustes.resizable(False, False)
ventana_ajustes.configure(bg=COLOR_FONDO)
ventana_ajustes.withdraw()   # oculta hasta que se abra

# Encabezado verde
encabezado_ajustes = tk.Frame(ventana_ajustes, bg=COLOR_ENCABEZADO)
encabezado_ajustes.pack(fill="x")
tk.Label(encabezado_ajustes, text="Ajustes de Tecla", bg=COLOR_ENCABEZADO, fg="white", font=FUENTE_TITULO, pady=4).pack(side="left", padx=8)

cuerpo_ajustes = tk.Frame(ventana_ajustes, bg=COLOR_FONDO, padx=12, pady=10)
cuerpo_ajustes.pack(fill="both", expand=True)

# Tecla de inicio 
tk.Label(cuerpo_ajustes, text="Comienzo", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE).grid(row=0, column=0, sticky="w", pady=(0,6))

entrada_tecla_comenzar = tk.Entry(cuerpo_ajustes, textvariable=tecla_comenzar, width=16, bg=COLOR_ENTRADA, fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO, relief="sunken", bd=1, font=FUENTE)
entrada_tecla_comenzar.insert(0, "Presiona Aqui")
entrada_tecla_comenzar.grid(row=0, column=1, padx=(10,0), pady=(0,6))

# Tecla de detención 
tk.Label(cuerpo_ajustes, text="Detener", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE).grid(row=1, column=0, sticky="w", pady=(0,10))

entrada_tecla_detener = tk.Entry(cuerpo_ajustes, textvariable=tecla_detener, width=16, bg=COLOR_ENTRADA, fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO, relief="sunken", bd=1, font=FUENTE)
entrada_tecla_detener.insert(0, "Presiona Aqui")
entrada_tecla_detener.grid(row=1, column=1, padx=(10,0), pady=(0,10))

# Botones Guardar / Reiniciar 
frame_botones_ajustes = tk.Frame(cuerpo_ajustes, bg=COLOR_FONDO)
frame_botones_ajustes.grid(row=2, column=0, columnspan=2)

def guardar_ajustes():
    pass

def reiniciar_teclas():
    entrada_tecla_comenzar.delete(0, tk.END)
    entrada_tecla_comenzar.insert(0, "Presiona Aqui")
    entrada_tecla_detener.delete(0, tk.END)
    entrada_tecla_detener.insert(0, "Presiona Aqui")

boton(frame_botones_ajustes, "Guardar",    guardar_ajustes,  ancho=10).grid(row=0, column=0, padx=4)
boton(frame_botones_ajustes, "Reiniciar",  reiniciar_teclas, ancho=10).grid(row=0, column=1, padx=4)

# Captura de tecla en los campos de ajuste <--
def capturar_tecla(evento, campo):
    campo.delete(0, tk.END)
    campo.insert(0, evento.keysym)
    return "break"
# El .bind() le dice a tkinter que cuando el usuario presione cualquier tecla mientras el campo está enfocado, ejecute la función capturar_tecla. 
# Esa función borra el contenido actual del campo y escribe el nombre de la tecla presionada, por ejemplo "F8" o "space".
entrada_tecla_comenzar.bind("<KeyPress>",  lambda e: capturar_tecla(e, entrada_tecla_comenzar))
entrada_tecla_detener.bind("<KeyPress>", lambda e: capturar_tecla(e, entrada_tecla_detener))

# Arranque <--
ventana_principal.mainloop()