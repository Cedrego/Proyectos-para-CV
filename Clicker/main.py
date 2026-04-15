import pyautogui

import customtkinter as ctk
from tkinter  import messagebox

root = ctk.CTk()    
root.title("Clicker | Hecho por Thiago Cedrés y Enzo Brun")
root.geometry("500x500")
root.resizable(0, 0)
title_label = ctk.CTkLabel(root, text="Clicker | Hecho por Thiago Cedrés y Enzo Brun", font=("Arial", 12), text_color="#565656" )
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 0))

color_texto = "000000"
color_boton = "#D9D9D9"

#def menu():
    #Intervalo de tiempo entre clicks
    