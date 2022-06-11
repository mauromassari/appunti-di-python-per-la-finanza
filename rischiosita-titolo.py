'''
La rischiosità di un titolo si calcola in termini di varianza dei rendimenti

    Maggiore è la varianza, maggiore è la volatilità del titolo e
    quindi più alta è la probabilità di subire una perdita

    Più il prezzo di un titolo tende a variare

    Per utilizzare questo valore bisogna confrontarlo con quello di altri titoli
    e vedere quali sono quelli più volatili
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

#calolo la varianza/rischiosità dei 2 titoli
varianzaFerrari = df3['Rendimenti'].var()
varianzaTesla = df4['Rendimenti'].var()

print(varianzaFerrari)
print(varianzaTesla)


'''
Un altro modo per verificare la rischiosità di un titolo è utilizzare la deviazione standard'''

#importo la libreria math per poter calcolare la deviazione standard di un titolo
import math

#calcolo deviazione standard, ovvero calcolo la radice quadrata della varianza
devStandFerr = math.sqrt(varianzaFerrari)


