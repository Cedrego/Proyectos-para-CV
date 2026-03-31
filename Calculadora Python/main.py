import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x550")
        self.title("Calculadora Basica")        
        customtkinter.set_appearance_mode("dark")
        self.resizable(0,0)

        self.button = customtkinter.CTkButton(self, text="button 1", command=self.button_callbck)
        self.button.grid(row=0, column=0, padx=5, pady=20, sticky="ew", columnspan=2)
        self.button1 = customtkinter.CTkButton(self, text="1")
        self.button1.grid(row=1, column=0, padx=0, pady=(0, 2))
        self.button2 = customtkinter.CTkButton(self, text="2")
        self.button2.grid(row=1, column=1, padx=0, pady=(0, 2))
        self.button3 = customtkinter.CTkButton(self, text="3")
        self.button3.grid(row=1, column=2, padx=0, pady=(0, 2))
        self.button4 = customtkinter.CTkButton(self, text="4")
        self.button4.grid(row=2, column=0, padx=0, pady=(0, 2))
        self.button5 = customtkinter.CTkButton(self, text="5")
        self.button5.grid(row=2, column=1, padx=0, pady=(0, 2))
        self.button6 = customtkinter.CTkButton(self, text="6")
        self.button6.grid(row=2, column=2, padx=0, pady=(0, 2))
        
    def button_callbck(self):
        resultado = "a" + 2
        print(f"button clicked, resultado: {resultado}")

app = App()
app.mainloop()
##https://customtkinter.tomschimansky.com/tutorial/grid-system