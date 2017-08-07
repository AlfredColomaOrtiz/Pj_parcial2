import pandas as pd
from funciones import funciones_obligatorias as funo
from funciones import menu

str_user = ""

l_archivos      = ["atp1.csv","atp2.csv","atp3.csv","atp4.csv","atp5.csv"]
l_pciones       = ["Generar Reportes","Generar Gráficos","X-- Salir"]
l_subopciones_R = ["Top ten","Estadisticas","Eficiencia","Copmparar","Historial titulos","Historial ranking","<-- Volver"]
l_subopciones_G = ["Juegos ganados","Eficiencia en años","Ganados por superficie","Ganados por top ten", "Ganados por ubicacion","Ganados por pperdidos","<-- Volver"]

## creando diccionario dataset
print("cargando base de datos...")
dic_dataset = funo.leerDataset(l_archivos)

## Comiensa el menu principal
while str_user != str(len(l_pciones)):

    menu.mostrarMenu(l_pciones,"Menu Pprincipal")
    str_user = input("elija una opcion:\n>> ")

    # opcion de Reportes
    if str_user == "1":
        ## comiensa el menu reportes
        while str_user != str(len(l_subopciones_R)):

            menu.mostrarMenu(l_subopciones_R,l_pciones[0])
            str_user = input("elija una opcion:\n>> ")

    # opcion de Graficos
    if str_user == "2":
        ## comiensa el menu graficos
        while str_user != str(len(l_subopciones_G)):

            menu.mostrarMenu(l_subopciones_G,l_pciones[1])
            str_user = input("elija una opcion:\n>> ")