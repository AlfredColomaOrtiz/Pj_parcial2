import pandas as pd
import datetime as dt

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
# version:      2
##
def getTopTenJugadores(df,torneo,anio):
    df_torneo = df.loc[torneo]
    df_filtro  = df_torneo[df_torneo["Date"].str.endswith(str(anio))]

    return df_filtro.head(10).loc[:,["Winner","WRank","Wsets","Date","W1"]]

def getEstadisticasJugador(df,jugador):
    pass

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

