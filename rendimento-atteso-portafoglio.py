'''
Rendimento atteso di portafoglio

    È dato dalla semplice media ponderata dei rendimenti
    attesi dei singoli titoli
'''

#Ipotizziamo di avere 50% azioni di Tesla e 50% azioni di Ferrari

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

#calolo la media dei rendimenti di entrambi i titoli
mediaFerrari = df3['Rendimenti'].mean()
mediaTesla = df4['Rendimenti'].mean()

#calcolo rendimento atteso portafoglio
#considero di avere il 40% dei titoli ferrari e 60% tesla nel mio portafoglio
rendimento_atteso = 0.4 * mediaFerrari + 0.6 * mediaTesla
print(rendimento_atteso)

