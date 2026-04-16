from unittest import case

import pyautogui

intervalo = 0.1
cantidad = 300 #0 para infinito
UbicacionFija = True
posX, posY = pyautogui.size()/2
TipoClick = "Unico"
Boton = "left"
pyautogui.FAILSAFE = True

def clicker():
    match UbicacionFija:
        case "False":
            match TipoClick:
                case "Unico":
                    pyautogui.click(pyautogui.position().x,pyautogui.position().y, cantidad, intervalo, Boton)
                case "Doble":
                    pyautogui.doubleClick(pyautogui.position().x,pyautogui.position().y, cantidad, intervalo, Boton)
        case "True":
            match TipoClick:
                case "Unico":
                    pyautogui.click(posX, posY, cantidad, intervalo, Boton)
                case "Doble":
                    pyautogui.doubleClick(posX,posY, cantidad, intervalo, Boton)
