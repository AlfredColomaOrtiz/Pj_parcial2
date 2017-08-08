import pandas as pd
import numpy as np
from funciones import funciones_obligatorias as funo
from funciones import menu

str_user = ""

l_archivos      = ["atp1.csv","atp2.csv","atp3.csv","atp4.csv","atp5.csv"]
l_pciones       = ["Generar Reportes","Generar Gráficos","X-- Salir"]
l_subopciones_R = ["Top ten","Estadisticas","Eficiencia","Copmparar","Historial titulos","Historial ranking","<-- Volver"]
l_subopciones_G = ["Juegos ganados","Eficiencia en años","Ganados por superficie","Ganados por top ten", "Ganados por ubicacion","Ganados por perdidos","<-- Volver"]

## creando diccionario dataset
print("cargando base de datos...")
dic_dataset = funo.leerDataset(l_archivos)
print("...")
df_dataset  = funo.leerDataset(l_archivos,False)
print("...")
print("crando datos extras...")


##agrega la columna de años en el dataframe
l_anios   = []
isi = 1
for i,f in df_dataset.iterrows():
    l_anios.append(f["Date"][-4:])
    if i == int(46650/2) or i == int(46650/4) or i == int((46650/4)*3) or i == int((46650/4)*3.6):
        print(int(i*0.002),"%")
df_dataset["Años"] = np.array(l_anios)


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

            # opcion top ten
            if str_user == "1":
                print("""
                Top Ten de los jugadores
                por un torneo determminado 
                en un año determinado
                """)
                input("[ENTER]")

                df_torneos = menu.presentar(dic_dataset,"Tournament")
                print(df_torneos)
                int_torneo = menu.input_int("elija una torneo (indice):\n>> ")

                df_anios = pd.Series(range(2000,2017))
                print(df_anios)
                int_anio   = menu.input_int("elija una año (indice):\n>> ")

                if (int_torneo in df_torneos.keys()) and (int_anio in df_anios.keys()):
                    df_topTen = funo.getTopTenJugadores(df_dataset,df_torneos[int_torneo],df_anios[int_anio])
                    print(df_topTen)

                else:
                    print("selecciono un indice que no se encuentra en las lista, vuela a intentarlo")

            # opcion estadisticas
            if str_user == "2":
                pass

            # opcion eficiencia
            if str_user == "3":
                pass

            # opcion comparar
            if str_user == "4":
                pass

            # opcion historial titulos
            if str_user == "5":
                pass

            # opcion historial ranking
            if str_user == "6":
                pass

    # opcion de Graficos
    if str_user == "2":
        ## comiensa el menu graficos
        while str_user != str(len(l_subopciones_G)):
            menu.mostrarMenu(l_subopciones_G,l_pciones[1])
            str_user = input("elija una opcion:\n>> ")

            # opcion juegos ganados
            if str_user == "1":
                pass

            # opcion eficiencia en años
            if str_user == "2":
                pass

            # opcion ganados por superficie
            if str_user == "3":
                pass

            # opcion ganados por top ten
            if str_user == "4":
                pass

            # opcion ganados por ubicacion
            if str_user == "5":
                pass

            # opcion ganados por perdidos
            if str_user == "6":
                pass