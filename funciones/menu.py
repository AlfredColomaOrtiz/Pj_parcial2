import pandas as pd
import os

##
# mostrarMenu:  muestra el menu en base a una lista y un tiutulo
# crada en:     6/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      2
##
def mostrarMenu(l_opciones,titulo):
    os.system("cls")
    print("\n*****",titulo,"*****\n")
    print(pd.Series(l_opciones,index=range(1,len(l_opciones)+1)))
    print("\n*****","*"*len(titulo),"*****\n")
