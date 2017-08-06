import pandas as pd

def mostrarMenu(l_opciones):
    print(pd.Series(l_opciones,index=range(1,len(l_opciones)+1)))
    print()