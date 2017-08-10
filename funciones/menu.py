import pandas as pd
import os

##
# mostrarMenu:  muestra el menu en base a una lista y un tiutulo
# crada en:     6/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      2
##
def mostrarMenu(l_opciones,titulo): # l_opciones: lista con strings de opciones # titulo: cabecera del menu
    os.system("cls")
    print("\n*****",titulo,"*****\n")
    print(pd.Series(l_opciones,index=range(1,len(l_opciones)+1)))
    print("\n*****","*"*len(titulo),"*****\n")

##
# presentar:    toma un diccionario y presenta sus opciones sin repeticion
# crada en:     7/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def presentar(df,titulo): #diccionario: del diccionario que se extraera #titulo: fracmento del diccionario
    listado = list(set(df[titulo].to_dict().values()))
    return pd.Series(listado)

##
# input_int:    convierte un input en entero mientras pueda, sino vuelve a preguntar
# crada en:     7/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def input_int(str):
    entrada = "SrColoma"
    while not entrada.isdigit():
        entrada = input(str)
        if entrada.isdigit():
            return int(entrada)

def input_buscar(str)
    entrada = "SrColoma"