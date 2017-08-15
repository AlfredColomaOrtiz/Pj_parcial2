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
    int_tsrmr = int(pd.to_numeric(df_filtro["WRank"]).max())
    df_tsrmr  = df_filtro.loc[df_filtro["WRank"]==int_tsrmr]
    #str_tsrmr =

def getEficienciaJugadorXsuperficie():
    pass

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

