import pandas as pd

##
# leerDataset:  toma una lista de nombres de archivos y los convierte en un diccionario
# creada en:    6/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def leerDataset(l_archivos,dic=True): # l_archivos : lista copn nombres de archivos csv
    df_final   = pd.DataFrame()

    for archivo in l_archivos:
        df_arch  = pd.read_csv(archivo,sep=";",encoding="latin-1")
        df_final = pd.concat([df_final,df_arch],ignore_index=True)

    if dic == True:
        return df_final.to_dict()
    else:
        return df_final

##
# getTopTenJugadores:  toma  el toeneo y un año y los filtra del dataframe
# creada en:    8/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def getTopTenJugadores(df,torneo,anio):
    df_filtro = df[(df["Tournament"] == torneo) & (df["Años"] == str(anio))]
    a=df_filtro.pop("Winner")
    b=df_filtro.pop("WRank")
    c=df_filtro.pop("Wsets")
    d=df_filtro.pop("Años")
    dic_filto ={"Tenista":a,"Ranking mundial":b,"Sets ganados":c,"Año":d}
    return pd.DataFrame(dic_filto)

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

