from funciones import funciones_obligatorias as funo
from funciones import menu
import reportes
import graficos

str_user = ""

# menus y nombres de archivos
l_archivos      = ["atp1.csv","atp2.csv","atp3.csv","atp4.csv","atp5.csv"]
l_opciones      = ["Generar Reportes","Generar Gráficos","X-- Salir"]
l_subopciones_R = ["Top ten","Estadisticas","Eficiencia","Copmparar","Historial titulos","Historial ranking","<-- Volver"]
l_subopciones_G = ["Juegos ganados","Eficiencia en años","Ganados por superficie","Ganados por top ten", "Ganados por ubicacion","Ganados por perdidos","<-- Volver"]

## creando dataframe dataset
print("cargando base de datos...")
df_dataset = funo.leerDataset(l_archivos)

## Comiensa el menu principal
while str_user != str(len(l_opciones)):

    menu.mostrarMenu(l_opciones,"Menu Pprincipal")
    str_user = input("elija una opcion:\n>> ")

    # opcion de Reportes
    if str_user == "1":

        ## comiensa el menu reportes
        while str_user != str(len(l_subopciones_R)):

            menu.mostrarMenu(l_subopciones_R,l_opciones[0])
            str_user = input("elija una opcion:\n>> ")

            # opcion top ten
            if str_user == "1":
                reportes.opcion_1(df_dataset)

            # opcion estadisticas
            if str_user == "2":
                reportes.opcion_2(df_dataset)

            # opcion eficiencia
            if str_user == "3":
                reportes.opcion_3(df_dataset)

            # opcion comparar
            if str_user == "4":
                reportes.opcion_4(df_dataset)

            # opcion historial titulos
            if str_user == "5":
                reportes.opcion_5(df_dataset)

            # opcion historial ranking
            if str_user == "6":
                reportes.opcion_6(df_dataset)

    # opcion de Graficos
    if str_user == "2":

        ## comiensa el menu graficos
        while str_user != str(len(l_subopciones_G)):

            menu.mostrarMenu(l_subopciones_G,l_opciones[1])
            str_user = input("elija una opcion:\n>> ")

            # opcion juegos ganados
            if str_user == "1":
                graficos.opcion_1(df_dataset)

            # opcion eficiencia en años
            if str_user == "2":
                graficos.opcion_2(df_dataset)

            # opcion ganados por superficie
            if str_user == "3":
                graficos.opcion_3(df_dataset)

            # opcion ganados por top ten
            if str_user == "4":
                graficos.opcion_4(df_dataset)

            # opcion ganados por ubicacion
            if str_user == "5":
                graficos.opcion_5(df_dataset)

            # opcion ganados por perdidos
            if str_user == "6":
                graficos.opcion_6(df_dataset)
