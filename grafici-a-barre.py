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


#creazione grafico a barre
#           X               Y
plt.bar(dfTesla.index, dfTesla['Volume'])
#plt.show()


#creazione grafico a barre con colorazione barre personalizzata
#           X               Y
plt.bar(dfTesla.index, dfTesla['Volume'], color='orange')
plt.show()



