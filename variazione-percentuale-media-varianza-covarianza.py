#importo dati da yahoo finance

#importo le librerie necessarie
import pandas as pd
import datetime as dt
import pandas_datareader.data as web

#definizione data inizio rilevazione
start = dt.datetime(2020,1,1)

#definizione data inizio rilevazione
end = dt.datetime(2022,1,1)

#importo i dataframe di Tesla e Ferrari (serie storiche)
#df è la variabile che conterrà il dataframe,avrei potuto chiamarla anche pippo
df = web.DataReader('TSLA','yahoo',start,end)
df2 = web.DataReader('RACE','yahoo',start,end)

#creiamo un datatframe vuoto
df3 = pd.DataFrame()

#calcolo la variazione percentuale (in numeri decimali) del titolo di tesla giorno per giorno
df3['Rendimenti'] = df['Adj Close'].pct_change()


#poichè il primo valore sarà sempre Nan, vado ad eliminarlo
df3.dropna(inplace = True)

#ora tasformo i valori decimali in percentuale
df4 = df3*100
print(df4)


#CALCOLO LA MEDIA dei rendimenti
media = df3['Rendimenti'].mean()
print('la media dei rendimenti di Tesla è ' + str(media))

#valore massimo della colonna di un dataframe
massimo = df3['Rendimenti'].max()
print('Il valore massimo è ' + str(massimo))

#valore minimo della colonna di un dataframe
minimo = df3['Rendimenti'].min()
print('Il valore minimo è ' + str(minimo))


'''Calcola della varianza (deviazione standard quadratica)
    - misura della variabilità di un elemento '''

varianza = df3['Rendimenti'].var()
print('La varianza dei rendimenti è ' + str(varianza))


'''Calcola della covarianza:
    è un numero che fornisce una misura di quanto due elementi varino assieme'''
covarianza = df['Adj Close'].cov(df2['Adj Close'])
print('La covarianza fra Tesla e Ferrari è pari a ' + str(covarianza))
