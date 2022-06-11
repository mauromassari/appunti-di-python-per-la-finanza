'''
La Correlazione

Come varia una variabile al variare di un altra variabile
Può assumere valori fra 1 e -1

se corr > 0 = le variabili si dicono correlate positivamente
    All'aumentare di una variabile, l'altra aumenta di valore

se corr = 0 = le variabili si dicono indipendenti

se corr < 0 = le variabili si dicono correlate negativamente
    All'aumentare di una variabile, l'altra diminuisce di valore


Inoltre

se 0   < corr <  0,3 = la correlazione è debole
    All'aumentare di una variabile, l'altra aumenta di poco il proprio valore
    
se 0,3 < corr <  0,7 = la correlazione è moderata

se 0,7 < corr <  1 = la correlazione è forte
    All'aumentare di una variabile, l'altra aumenta di tanto il proprio valore


Mentre se

se 0   < corr <  -0,3 = la correlazione è debole
    All'aumentare di una variabile, l'altra diminuisce di poco il proprio valore
    
se -0,3 < corr <  -0,7 = la correlazione è moderata

se -0,7 < corr <  -1 = la correlazione è forte
    All'aumentare di una variabile, l'altra diminuisce di tanto il proprio valore


In finanza, la correlazione è un valore statistico che misura come due titoli
si influenzano reciprocamente.

corr =  1 (correlazione positiva)
corr = -1 (correlazione negativa)
corr = 0 (i 2 titoli non hanno nessuna correlzione)
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


#calcolo la correlazione fra Tesla e Ferrari
    #Serve una serie storica molto lunga

#Calcoliamo prima i rendimenti
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

#calolo la correlazione fra i 2 titoli
corr = df3['Rendimenti'].corr(df4['Rendimenti'])
print(corr)
