'''
Rendimento atteso di un titolo

    si intende la stima del suo probabile rendimento futuro.

    Una delle metodologie per calcolarlo consiste
    nell'effettuare la media dei rendimenti passati

    Metodo molto basilare e poco sicuro

    Sarebbe ottimo utilizzare una serie storica molto lunga
    
'''

#importo le altre librerie necessarie
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt

#definizione data inizio rilevazione
start = dt.datetime(2021,1,1)

#definizione data inizio rilevazione
end = dt.datetime(2022,1,1)

#importo i dataframe di Tesla(serie storiche)
#df è la variabile che conterrà il dataframe,avrei potuto chiamarla anche pippo
dfTesla = web.DataReader('TSLA','yahoo',start,end)
dfFerrari = web.DataReader('RACE','yahoo',start,end)


#creo prima due dataframe vuoti
df3 = pd.DataFrame()
df4 = pd.DataFrame()


#dentro df3 metto i rendimenti di Ferrari
df3['Rendimenti'] = dfFerrari['Adj Close'].pct_change()
    
#dentro df4 metto i rendimenti di Tesla
df4['Rendimenti'] = dfTesla['Adj Close'].pct_change()

#rimuovi i valori Nan in maniera definitiva
df3.dropna(inplace = True)
df3.dropna(inplace = True)

#calolo il rendmento atteso dei due titoli
rendAttTesla = df4['Rendimenti'].mean() 
rendAttFerrari = df3['Rendimenti'].mean() 



