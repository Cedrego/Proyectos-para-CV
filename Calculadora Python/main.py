import customtkinter as ctk
from tkinter  import messagebox

root = ctk.CTk()
root.title("Calculadora Basica Python")
root.geometry("400x500")
root.resizable(0, 0)
title_label = ctk.CTkLabel(root, text="Calculadora Basica Python | Hecho por Thiago Cedrés y Enzo Brun", font=("Arial", 12), text_color="#565656" )
title_label.grid(row=0, column=0, columnspan=4, pady=(0, 0))

color_texto = "#79D0FF"
color_boton = "#313168"
color_boton_igual = "#8EFFAC"
boton_boton_clear = "#FF9191"

screen_text = ctk.StringVar()

def validate_input(P):
    return all(c in "0123456789+-*/.()" for c in P)

vcmd = (root.register(validate_input), '%P')
screen_entry = ctk.CTkEntry(root, textvariable=screen_text, font=("Arial", 24), width=400, height=50, justify='right', validate="key", validatecommand=vcmd)
screen_entry.grid(row=1, column=0, columnspan=4, sticky='we', pady=0)

expression = ''

def press(num):
    current = screen_text.get()
    new_text = current + str(num)
    screen_text.set(new_text)

def equalpress():
    try:
        result = str(eval(screen_text.get()))
        screen_text.set(result)
    except:
        messagebox.showerror("Error", "Expresión no válida")
        screen_text.set("")

def clear():
    screen_text.set("")

def update_expression(event=None):
    global expression
    expression = screen_text.get()


screen_entry.bind("<KeyRelease>", update_expression)
screen_entry.bind("<Return>", lambda event: equalpress())
screen_entry.bind("<BackSpace>", update_expression)

buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('C', 5, 0), ('0', 5, 1), ('.', 5, 2), ('+', 5, 3),
    ('=', 6, 0)
]
for (text, row, col) in buttons:
    button = ctk.CTkButton(root, text=text, width=60, height=60, font=('Arial',18), bg_color=color_texto, fg_color= color_boton, corner_radius=8, command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')

equal_button = ctk.CTkButton(root, text='=', width=60, height=60, font=('Arial',18), bg_color=color_boton_igual, fg_color="#139F50", corner_radius=8, command=equalpress)
equal_button.grid(row=6, column=0, padx=2, pady=2,columnspan=4, sticky='nsew')

clear_button = ctk.CTkButton(root, text='C', width=60, height=60, font=('Arial',18), bg_color=boton_boton_clear, fg_color="#A51F1F", corner_radius=8, command=clear)
clear_button.grid(row=5, column=0, padx=2, pady=2, sticky='nsew')

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()