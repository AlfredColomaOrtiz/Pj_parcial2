import pandas as pd
import os
from funciones import funciones_obligatorias as funo
from funciones import menu

user = -1
opciones = ["Generar Reportes","Generar Gráficos","Salir"]

while user != "3":
    os.system("cls")
    menu.mostrarMenu(opciones)
    user = input("helija una opcion:\n>>")