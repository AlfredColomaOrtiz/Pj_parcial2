from funciones import funciones_obligatorias as funo
from funciones import menu
import reportes
import pandas as pd

##
# opcion_1:    opcion 1 de graficos
# crada en:     21/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
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

    df_jugador = menu.buscar_en(df_dataset, "Winner", "el apellido del jugador")
    print(df_jugador["Winner"])
    int_selec = menu.input_int("seleccione un jugador(indice):\n>>")

    df_anios_ini = pd.Series(range(2000, 2017))
    print(df_anios_ini)
    int_anio_ini = menu.input_int("\nelija una año de inicio (indice):\n>> ")

    df_anios_fin = pd.Series(range(2000, 2017))
    print(df_anios_ini)
    int_anio_fin = menu.input_int("\nelija una año de fin (indice):\n>> ")

    if int_anio_ini in df_anios_ini.keys() and int_anio_fin in df_anios_fin and int_selec in df_jugador["Winner"].keys() and int_anio_ini < int_anio_fin:

        str_anio_ini = df_anios_ini[int_anio_ini]
        str_anio_fin = df_anios_ini[int_anio_fin]
        str_jugador  = df_jugador["Winner"][int_selec]

        funo.DrawDistribucionJuegosGanados(df_dataset,int_set,str_anio_ini,str_anio_fin,str_jugador)

    else:
        print("selecciono un indice que no se encuentra en las lista\no elijio de forma incorrecta los intervalos de años\nvuela a intentarlo")
        input("[ENTER]")

#
# opcion_1:    opcion 2 de graficos
# crada en:     24/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def opcion_2(df_dataset):
    per4 = reportes.opcion_4(df_dataset,True)
    funo.DrawTendenciasEficiencia(per4)

#
# opcion_1:    opcion 3 de graficos
# crada en:     24/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def opcion_3(df_dataset):
    per4 = reportes.opcion_4(df_dataset, True)
    funo.DrawTendenciasEficiencia(per4)

##
# opcion_4:    opcion 4 de graficos
# crada en:     21/agosto/2017
# autor:        Danny Tenesaca Lopez
# version:      1
##
def opcion_4(df_dataset):
    b = reportes.opcion_1(df_dataset,True)  # En el programa principal llamamos a la funcion de crear el top ten
    print(b)  # Retorna un dataFrame y lo alojamos en una variable
    funo.DrawComparativaTopTen(b)  # Con el data frame del top t

##
# opcion_5:    opcion 5 de graficos
# crada en:     23/agosto/2017
# autor:        Danny Tenesaca Lopez
# version:      1
##

def opcion_5(df_dataset):
    df_jugador = menu.buscar_en(df_dataset, "Winner", "el apellido del jugador")
    print(df_jugador["Winner"])
    int_selec = menu.input_int("seleccione un jugador(indice):\n>>")

    if int_selec in df_jugador["Winner"].keys():
        str_nombre = df_jugador["Winner"][int_selec]
        print("selecciono: ", str_nombre)
        df_jugador = menu.buscar_en(df_dataset, "Winner", "el apellido del jugador")
        print(df_jugador["Winner"])
        int_selec = menu.input_int("seleccione un jugador(indice):\n>>")

        if int_selec in df_jugador["Winner"].keys():
            str_nombre = df_jugador["Winner"][int_selec]
            print("selecciono: ", str_nombre)

    ##
    # opcion_6:    opcion 6 de graficos
    # crada en:     23/agosto/2017
    # autor:        Danny Tenesaca Lopez
    # version:      1
    ##

    df_dataset = df_dataset.set_index("Winner")
    df_filtro = df_dataset.loc[str_nombre]
    df_filtro = df_filtro.drop_duplicates("Location")
    df_dataset2 = df_filtro.set_index("Location")

    funo.DrawPartidosGanadosJugadorPorCiudad(df_dataset2)


def opcion_6(df_dataset):
    df_jugador = menu.buscar_en(df_dataset, "Winner", "el apellido del jugador")
    print(df_jugador["Winner"])
    int_selec = menu.input_int("seleccione un jugador(indice):\n>>")

    if int_selec in df_jugador["Winner"].keys():
        str_nombre = df_jugador["Winner"][int_selec]
        print("selecciono: ", str_nombre)
        df_jugador = menu.buscar_en(df_dataset, "Winner", "el apellido del jugador")
        print(df_jugador["Winner"])
        int_selec = menu.input_int("seleccione un jugador(indice):\n>>")

        if int_selec in df_jugador["Winner"].keys():
            str_nombre = df_jugador["Winner"][int_selec]
            print("selecciono: ", str_nombre)

    df_dataset = df_dataset.set_index("Winner")
    año = 2000
    df_filtro = df_dataset.loc[str_nombre]
    # df_filtro = (df_filtro[df_filtro["Date"].str.endswith(str(año))])
    df = df_filtro.set_index("Date")

    funo.DrawComparativaPartidosPorJugador(df)