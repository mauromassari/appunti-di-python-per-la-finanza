#importo le altre librerie necessarie
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt

#definizione data inizio rilevazione
start = dt.datetime(2020,1,1)

#definizione data inizio rilevazione
end = dt.datetime(2022,1,1)

#importo i dataframe di Tesla(serie storiche)
#df è la variabile che conterrà il dataframe,avrei potuto chiamarla anche pippo
dfTesla = web.DataReader('TSLA','yahoo',start,end)
dfFerrari = web.DataReader('RACE','yahoo',start,end)

#definisco la posizione dei 2 grafici 
grafico1 = plt.subplot(211)

                         #aggiungo questa istruzione per far sì che quando zoommo si di un grafico,si estenda anche l'altro
grafico2 = plt.subplot(212, sharex = grafico1)


grafico1.plot(dfTesla.index, dfTesla['Adj Close'])
grafico2.bar(dfTesla.index, dfTesla['Volume'])

#elimino le etichette dall'asse x dal grafico 1
grafico1.xaxis.set_visible(False)

plt.show()

