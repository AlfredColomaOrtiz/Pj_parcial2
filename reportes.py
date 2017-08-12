from funciones import funciones_obligatorias as funo
from funciones import menu
import pandas as pd

##
# primera opcion del menu graficos
# creada en:    12/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def opcion_1(df_dataset):
    print("""
                    Top Ten de los jugadores
                    por un torneo determminado 
                    en un año determinado
                    """)
    input("[ENTER]")

    # pide el año
    df_anios = pd.Series(range(2000, 2017))
    print(df_anios)
    int_anio = menu.input_int("\nelija una año (indice):\n>> ")

    #pide el torneop
    df_torn = menu.presentar(df_dataset[df_dataset["Date"].str.endswith(str(int_anio))], "Tournament")
    print(df_torn)
    int_torneo = menu.input_int("\nelija una torneo (indice):\n>> ")

    # si el torneo y año existen llama al top ten
    if (int_torneo in df_torn.keys()) and (int_anio in df_anios.keys()):

        df_topTen = funo.getTopTenJugadores(df_dataset.set_index("Tournament"), df_torn[int_torneo], df_anios[int_anio])
        print(df_topTen)
        input("[ENTER]")

    else:
        print("selecciono un indice que no se encuentra en las lista, vuela a intentarlo")
        input("[ENTER]")

##
# segunda opcion del menu graficos
# creada en:    12/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def opcion_2(df_dataset):
    pass

def opcion_3(df_dataset):
    pass

def opcion_4(df_dataset):
    pass

def opcion_5(df_dataset):
    pass

def opcion_6(df_dataset):
    pass
