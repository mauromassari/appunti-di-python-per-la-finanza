#importo la librearia per creare i grafici
import matplotlib.pyplot as plt

x = [3,4,5]
y = [4,5,2]

'''plt.plot(x,y)
plt.show()'''

#------------------------->


#importo le altre librerie necessarie
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt

#definizione data inizio rilevazione
start = dt.datetime(2020,1,1)

#definizione data inizio rilevazione
end = dt.datetime(2022,1,1)

#importo i dataframe di Tesla e Ferrari (serie storiche)
#df è la variabile che conterrà il dataframe,avrei potuto chiamarla anche pippo
df = web.DataReader('TSLA','yahoo',start,end)
df2 = web.DataReader('RACE','yahoo',start,end)

#creo un dataframe vuoto
df3 = pd.DataFrame()

df3['Valori'] = df['Adj Close']

'''
plt.plot(df3) #se gli passo solo un valore, questo verrà ,messo sull'asse delle y
              #mentre sull'asse delle x di default verranno messe le date
plt.show()
'''

'''        asse x         asse y        
plt.plot(df['Volume'], df['Adj Close'])
plt.show()
'''
