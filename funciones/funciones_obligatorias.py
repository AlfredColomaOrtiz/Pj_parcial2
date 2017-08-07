import pandas as pd

##
# leerDataset:  toma una lista de nombres de archivos y los convierte en un diccionario
# creada en:    6/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def leerDataset(l_archivos):
    df_final   = pd.DataFrame()

    for archivo in l_archivos:
        df_arch  = pd.read_csv(archivo,sep=";",encoding="latin-1")
        df_final = pd.concat([df_final,df_arch],ignore_index=True)

    return df_final.to_dict()

def getTopTenJugadores(df,torneo,año):
    pass

def getEstadisticasJugador():
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

