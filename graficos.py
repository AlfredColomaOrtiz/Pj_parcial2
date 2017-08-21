from funciones import funciones_obligatorias as funo
from funciones import menu
import reportes
import pandas as pd

def opcion_1(df_dataset):
    print("""
                    historial
                    de jugador
                    por mayor rankin 
                    en un año
                    """)
    input("[ENTER]")

    df_set = pd.DataFrame()
    while df_set.empty:
        print("Ingrese:", "elija el set")
        indice = menu.input_int(">>: ")
        df_set = df_dataset.loc[df_dataset["Wsets"] == indice]
    df_set = df_set.drop_duplicates("Wsets")

    int_set = df_set["Wsets"].iloc[0]

    df_anios_ini = pd.Series(range(2000, 2017))
    print(df_anios_ini)
    int_anio_ini = menu.input_int("\nelija una año de inicio (indice):\n>> ")

    df_anios_fin = pd.Series(range(2000, 2017))
    print(df_anios_ini)
    int_anio_fin = menu.input_int("\nelija una año de fin (indice):\n>> ")

    if int_anio_ini in df_anios_ini.keys() and int_anio_fin in df_anios_fin:

        str_anio_ini = df_anios_ini[int_anio_ini]
        str_anio_fin = df_anios_ini[int_anio_fin]

        funo.DrawDistribucionJuegosGanados(df_dataset,int_set,str_anio_ini,str_anio_fin)

    else:
        print("selecciono un indice que no se encuentra en las lista, vuela a intentarlo")
        input("[ENTER]")


def opcion_2(df_dataset):
    pass

def opcion_3(df_dataset):
    pass

def opcion_4(df_dataset):
    b = reportes.opcion_1(df_dataset,True)  # En el programa principal llamamos a la funcion de crear el top ten
    print(b)  # Retorna un dataFrame y lo alojamos en una variable
    funo.DrawComparativaTopTen(b)  # Con el data frame del top t

def opcion_5(df_dataset):
    pass

def opcion_6(df_dataset):
    pass
