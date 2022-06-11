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


#creo un dataframe vuoto
df2 = pd.DataFrame()

df2['Valori'] = dfTesla['Adj Close']

#creo legenda nel grafico

plt.plot(df2, label = 'Tesla')
plt.plot(dfFerrari['Adj Close'], label = 'Ferrari')

#aggiungo titole ed etichette alle due assi
plt.title('Grafico Ferrari e Tesla')
plt.xlabel('Date')
plt.ylabel('Prezzi')

#aggiungo griglia al grafico
plt.grid()

plt.legend()
plt.show()
