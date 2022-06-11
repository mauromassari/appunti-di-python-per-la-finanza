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

#definisco la posizione dei 4 grafici 
grafico1 = plt.subplot(221)

                            #aggiungo questa istruzione per far sì che quando zoommo su di un grafico, si estenda anche l'altro'''
grafico2 = plt.subplot(222, sharex = grafico1)


grafico3 = plt.subplot(223)

                            #aggiungo questa istruzione per far sì che quando zoommo su di un grafico, si estenda anche l'altro'''
grafico4 = plt.subplot(224, sharex = grafico2)


# 
grafico1.plot(dfTesla.index, dfTesla['Adj Close'])
grafico2.bar(dfTesla.index, dfTesla['Volume'])
grafico3.plot(dfFerrari.index, dfFerrari['Adj Close'])
grafico4.bar(dfFerrari.index, dfFerrari['Volume'])

#elimino le etichette dall'asse x dal grafico 1
#grafico1.xaxis.set_visible(False)

plt.show()

