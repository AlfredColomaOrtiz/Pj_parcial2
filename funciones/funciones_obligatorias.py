import pandas as pd

##
# leerDataset:  toma una lista de nombres de archivos y los convierte en un diccionario
# creada en:    6/agosto/2017
# autor:        Coloma Ortiz Alfred
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
# version:      1
##
def getEstadisticasJugador(df,jugador):
    df_filtro   = df.loc[jugador]# solo filas con el jugador (filtrado)

    # tipo de torneo #
    int_Ttorneo = len(df_filtro.drop_duplicates("Series",keep="first")["Series"])

    # ultimo ranking #
    int_Urankin = int(df_filtro["WRank"].ix[-1])

    # Numero de oponentes #
    int_oponentes = len(df_filtro.drop_duplicates("Loser",keep="first")["Loser"])

    # partidos ganados #
    int_partG = len(df_filtro["Loser"])

    # Partidops perdidos #
    int_partP = len(df[df["Loser"]== jugador]["Loser"])

    # Torneo serie con mayor rankin #
    int_tsrmr   = int(pd.to_numeric(df_filtro["WRank"]).max())
    df_tsrmr    = df_filtro.loc[(df_filtro["WRank"] == str(int_tsrmr)) | (df_filtro["WRank"]==int_tsrmr)]
    str_tsrmr   = df_tsrmr["Tournament"].ix[0]
    str_tsrmr2  = df_tsrmr["Series"].ix[0]
    str_torSerM = str_tsrmr+" - "+str_tsrmr2

    # Superficie #
    str_superf = (df_filtro["Surface"].value_counts(sort=False)).argmax()

    # Mayotr oponente #
    str_oponent = (df_filtro["Loser"].value_counts(sort=False)).argmax()

    # titulos obtenidos #
    int_titulos = len(df_filtro.loc[df_filtro["Round"] == "The Final"])

    ###
    l_datos  = [int_Ttorneo,int_Urankin,int_oponentes,int_partG,int_partP,str_torSerM,str_superf,str_oponent,int_titulos]
    l_colums = ["Tipos de torneo","Ultimo ranking btenido","Numero de oponentes","Partidos ganados","Partidos perdidos","Torneo-serie con mayor ranking","Superficie","Mayor opponente","Numero de titulos obtenidos"]

    df_final = pd.DataFrame([l_datos],columns=l_colums)
    print(df_final)


##
# getEficienciaJugadorXsuperficie: muestra la estadiestica de un jugador en relacion a una superficie
# creada en:    19/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def getEficienciaJugadorXsuperficie(df,jugador,supperficie):
    df_filtro = df.loc[df["Surface"] == supperficie]
    int_pWin   = len(df_filtro.loc[df_filtro["Winner"] == jugador]["Winner"])
    int_pLose  = len(df_filtro.loc[df_filtro["Loser"] == jugador]["Loser"])

    int_eficiencia = round(int_pWin / int_pLose,2)

    df_final = pd.DataFrame([[jugador,supperficie,int_eficiencia]],columns=["Jugador","Superficie","Eficiencia"])
    print(df_final)

def getComparacionJugadores():
    pass

def getHistorialJugador():
    pass

def getHistorialJugadorRankingAnio():
    pass

def DrawDistribucionJuegosGanados():
    pass

def DrawTendenciasEficiencia():
    pass

def DrawPartidosGanadosJugadores():
    pass

def DrawComparativaTopTen():
    pass

def DrawPartidosGanadosJugadorPorCiudad():
    pass

def DrawComparativaPartidosPorJugador():
    pass

