'''
Il beta
    in finanza rappresenta un indicatore che misura il comportamento
    di un titolo rispetto al suo mercato di riferimento, ossia
    di quanto variano storicamentee i rendimenti di un titolo ripetto
    ai rendimenti di mercato

    il bete si calcola come il rapporto fra la covarianza dei rendimenti
    del titolo e del mercato e la varianza dei rendimenti del mercato
'''

'''
Supponiamo che il beta di un titolo sia pari a 1,5.

Tale valore indica che in media qualora il rendimento di mercato
aumentasse dell'1% , il rendimento del titolo aumenterebbe dell'1,5%

Titoli con beta > 1 vengo detti titoli aggressivi
Titoli con beta < 1 vengo detti titoli difensivi
'''

#Ipotizziamo di avere 50% azioni di Tesla e 50% azioni di Ferrari

#importo le altre librerie necessarie
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import math

#definizione data inizio rilevazione
start = dt.datetime(2016,1,1)

#definizione data inizio rilevazione
end = dt.datetime(2022,1,1)

#importo i dataframe di Tesla(serie storiche)
#df è la variabile che conterrà il dataframe,avrei potuto chiamarla anche pippo
dfTesla = web.DataReader('TSLA','yahoo',start,end)
dfNasdaq = web.DataReader('^IXIC','yahoo',start,end)
    #indice del mercato di riferimento


#creo prima due dataframe vuoti
rendimenti_tesla = pd.DataFrame()
rendimenti_nasdaq = pd.DataFrame()

#popoloo i nuovi dataframe
rendimenti_tesla['Rendimenti'] = dfTesla['Adj Close'].pct_change()
rendimenti_nasdaq['Rendimenti'] = dfNasdaq['Adj Close'].pct_change()

#rimuovo gli nan
rendimenti_tesla.dropna(inplace=True)
rendimenti_nasdaq.dropna(inplace=True)

#calcolo la covarianza
cov = rendimenti_tesla['Rendimenti'].cov(rendimenti_nasdaq['Rendimenti'])

#calcolo la varianza
var = rendimenti_nasdaq['Rendimenti'].var()

#calcolo il beta
beta = cov/var

#arrotondo a due decimai il numero
beta2 = round(beta, 2)

print('Il beta del titolo Tesla con l\'indice Nasdaq è pari a ' + str(beta))
print(' ')
print('Quindi storicamente quando l\'indice Nasdaq è aumentato dell\'1% , il titolo Tesla è aumentato del ' + str(beta2) + '%')
    
    
