import pandas as pd
import matplotlib.pyplot as plt

##
# leerDataset:  toma una lista de nombres de archivos y los convierte en un diccionario
# creada en:    6/agosto/2017
# autor:        Danny Tenesaca Lopez
# version:      2
##
def leerDataset(l_archivos,): # l_archivos : lista copn nombres de archivos csv
    df_final   = pd.DataFrame()

    for archivo in l_archivos:
        df_arch  = pd.read_csv(archivo,sep=";",encoding="latin-1")
        df_final = pd.concat([df_final,df_arch],ignore_index=True)

    return df_final

##
# getTopTenJugadores:  toma  el toeneo y un año y los filtra del dataframe
# creada en:    8/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      4
##
def getTopTenJugadores(df,torneo,anio):
    df_torneo = df.loc[torneo]# extrae por indice el torneo solicitado
    df_filtro = df_torneo[df_torneo["Date"].str.endswith(str(anio))]# selecciona el año y ordena por wrank

    df_conteo = df_filtro["Winner"].value_counts(sort=False)# crea serie con numero de partidos ganados

    df_nodupli = df_filtro.drop_duplicates("Winner",keep="first")#  elimina jugadores repetidos
    df_nodupli = df_nodupli.set_index("Winner")
    df_nodupli = pd.concat([df_nodupli,df_conteo],axis=1)
    df_nodupli = df_nodupli.loc[:,["WRank","Wsets","Date","Winner"]]

    df_final = df_nodupli.rename(columns={"WRank":"Rankin Mundial","Wsets":"Sets Ganados","Date":"Año","Winner":"Partidos Ganados"})

    return df_final.sort_values("Rankin Mundial").head(10)

##
# getEstadisticasJugador:  troma edl dataframe y al jugador y filtra las estadisticas
# creada en:    13/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      2
##
def getEstadisticasJugador(df,jugador):
    df_filtro   = df.loc[jugador]# solo filas con el jugador (filtrado)

    int_Ttorneo   = len(df_filtro.drop_duplicates("Series",keep="first")["Series"])     # tipo de torneo #
    int_Urankin   = int(df_filtro["WRank"].ix[-1])                                      # ultimo ranking #
    int_oponentes = len(df_filtro.drop_duplicates("Loser",keep="first")["Loser"])       # Numero de oponentes #
    int_partG     = len(df_filtro["Loser"])                                             # partidos ganados #
    int_partP     = len(df[df["Loser"]== jugador]["Loser"])                             # Partidops perdidos #

    # Torneo serie con mayor rankin ######
    int_tsrmr   = int(pd.to_numeric(df_filtro["WRank"]).max())
    df_tsrmr    = df_filtro.loc[(df_filtro["WRank"] == str(int_tsrmr)) | (df_filtro["WRank"]==int_tsrmr)]
    str_tsrmr   = df_tsrmr["Tournament"].ix[0]
    str_tsrmr2  = df_tsrmr["Series"].ix[0]
    str_torSerM = str_tsrmr+" - "+str_tsrmr2
    # Torneo serie con mayor rankin ######

    str_superf = (df_filtro["Surface"].value_counts(sort=False)).argmax()               # Superficie #
    str_oponent = (df_filtro["Loser"].value_counts(sort=False)).argmax()                # Mayotr oponente #
    int_titulos = len(df_filtro.loc[df_filtro["Round"] == "The Final"])                 # titulos obtenidos #

    ###
    dic_datos= {
        "Tipos de torneo":{0:int_Ttorneo},
        "Ultimo ranking btenido":{0:int_Urankin},
        "Numero de oponentes":{0:int_oponentes},
        "Partidos ganados":{0:int_partG},
        "Partidos perdidos":{0:int_partP},
        "Torneo-serie con mayor ranking":{0:str_torSerM},
        "Superficie":{0:str_superf},
        "Mayor opponente":{0:str_oponent},
        "Numero de titulos obtenidos":{0:int_titulos}
    }

    df_final = pd.DataFrame(dic_datos)#,columns=l_colums)
    print(df_final)


##
# getEficienciaJugadorXsuperficie: muestra la estadiestica de un jugador en relacion a una superficie
# creada en:    19/agosto/2017
# autor:        Danny Tenesaca Lopez
# version:      1
##
def getEficienciaJugadorXsuperficie(df,jugador,supperficie):
    df_filtro  = df.loc[df["Surface"] == supperficie]
    int_pWin   = len(df_filtro.loc[df_filtro["Winner"] == jugador]["Winner"])
    int_pLose  = len(df_filtro.loc[df_filtro["Loser"] == jugador]["Loser"])

    int_eficiencia = round(int_pWin / int_pLose,2)

    df_final = pd.DataFrame([[jugador,supperficie,int_eficiencia]],columns=["Jugador","Superficie","Eficiencia"])
    print(df_final)

##
# getComparacionJugadores: recive 2 jugadores y crea una tabla de comparacion entre los 2
# creada en:    19/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def getComparacionJugadores(df,jugador1,jugador2):
    # jugador 1
    df_filtro1   = df.loc[df["Winner"]==jugador1]                                 # filtra con indices de solo el jugador #
    int_win1     = len(df.loc[df["Winner"]==jugador1])                                  # Número de victorias #
    int_lose1    = len(df.loc[df["Loser"] == jugador1])                                 # Número de derrotas #
    int_titulos1 = len(df_filtro1.loc[df_filtro1["Round"] == "The Final"])              # Títulos obtenidos #
    int_winE1    = len(df.loc[(df["Winner"]==jugador1) & (df["Loser"] == jugador2)])    # victorias en enfrentamientos #
    int_loseE1   = len(df.loc[(df["Winner"]==jugador2) & (df["Loser"] == jugador1)])    # derrotas en enfrentamientos #
    int_torneos1 = len(df_filtro1.drop_duplicates("Tournament",keep="first"))           # torneos en su carrera #
    int_rankin1  = df_filtro1["WRank"].iloc[-1]                                           # Ranking Actual #

    # jugador 2
    df_filtro2   = df.loc[df["Winner"]==jugador2]                                 # filtra con indices de solo el jugador #
    int_win2     = len(df.loc[df["Winner"] == jugador2])                                # Número de victorias #
    int_lose2    = len(df.loc[df["Loser"] == jugador2])                                 # Número de derrotas #
    int_titulos2 = len(df_filtro2.loc[df_filtro2["Round"] == "The Final"]["Round"])              # Títulos obtenidos #
    int_winE2    = len(df.loc[(df["Winner"] == jugador2) & (df["Loser"] == jugador1)])  # victorias en enfrentamientos #
    int_loseE2   = len(df.loc[(df["Winner"] == jugador1) & (df["Loser"] == jugador2)])  # derrotas en enfrentamientos #
    int_torneos2 = len(df_filtro2.drop_duplicates("Tournament", keep="first"))          # torneos en su carrera #
    int_rankin2  = df_filtro2["WRank"].iloc[-1]                                           # Ranking Actual #

    dic_fin = {
        jugador1:
        {
            "Número de victorias":int_win1,
            "Número de derrotas":int_lose1,
            "Títulos obtenidos":int_titulos1,
            "victorias en enfrentamientos":int_winE1,
            "derrotas en enfrentamientos":int_loseE1,
            "torneos en su carrera":int_torneos1,
            "Ranking Actual":int_rankin1
        },
        jugador2:
        {
            "Número de victorias": int_win2,
            "Número de derrotas": int_lose2,
            "Títulos obtenidos": int_titulos2,
            "victorias en enfrentamientos": int_winE2,
            "derrotas en enfrentamientos": int_loseE2,
            "torneos en su carrera": int_torneos2,
            "Ranking Actual": int_rankin2
        }
    }
    df_final = pd.DataFrame(dic_fin)
    print(df_final)

##
# getHistorialJugador: crea una tabla de los titulos de un jugador por su carrera
# creada en:    19/agosto/2017
# autor:        Danny Tenesaca Lopez
# version:      1
##
def getHistorialJugador(df,jugador):
    df_filtro = df.loc[(df["Winner"] == jugador)&(df["Round"] == "The Final")]
    df_final  = df_filtro.loc[:,["Date","Tournament","Series","Court","Surface","Loser","WRank"]]
    print(df_final.rename(columns={"Date":"Año","Tournament":"Torneo","Series":"Serie","Court":"Cancha","Surface":"Superficie","Loser":"oponente en la final","WRank":"Rankin logrado"}))

##
# getHistorialJugadorRankingAnio:  historial de partidos ganados con mayor rankin
# creada en:    20/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def getHistorialJugadorRankingAnio(df,jugador,anio):
    df_filtro = df.loc[(df["Winner"] == jugador) & (df["Date"].str.endswith(str(anio)))]
    df_Urank = df.loc[df["Winner"] == jugador]
    int_Urank = df_Urank["WRank"].iloc[-1]
    l_Urank   = [int_Urank] * len(df_filtro)
    df_filtro["Rankin actual"] = l_Urank
    df_final  = df_filtro.loc[:, ["Winner", "Date", "WRank","Rankin actual"]]
    print(df_final.rename(columns={"Winner":"Jugador", "Date":"Año", "WRank":"Ranking","Rankin actual":"Rankin actual"}))

#------------------------------------------ GRAFICOS---------------------------------------------#

##
# DrawDistribucionJuegosGanados:  dibuja la distribucion juagoa ganados
# creada en:    20/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def DrawDistribucionJuegosGanados(df,set,fecha_ini,fecha_fin):
    pass

def DrawTendenciasEficiencia():
    pass

def DrawPartidosGanadosJugadores():
    pass

##
# DrawComparativaTopTen:    grafica el top ten
# crada en:     21/agosto/2017
# autor:        Danny Tenesaca Lopez
# version:      1
##
def DrawComparativaTopTen(df):   #Funcion para crear el grafico
    grafico=df[["Partidos Ganados"]].plot(kind="Line", title="Comparacion del Top Ten", figsize=(10,10), legend=True, fontsize=10)
    grafico.set_xlabel("Jugadores")
    grafico.set_ylabel("Partidos Ganados")
    # df.plot(x="Rankin Mundial", y="Partidos Ganados", kind="Line")
    plt.show()

def DrawPartidosGanadosJugadorPorCiudad():
    pass

def DrawComparativaPartidosPorJugador():
    pass

