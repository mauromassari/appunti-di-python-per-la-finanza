'''
Lo Spread

    per l'Italia è l adifferenza fra i rendimenti dei titoli di stato
    con scadenza 10 anni e i rendimenti dei titoli di stato tedeschi con
    scadenza 10 anni

    Si utilizza come confront la Germania poiché viene considerato come
    uno stato sicuro

    E più uno stato viene percepito "sicuro" e più il suo costo per
    finanziarsi sarà basso

    Se lo spread aumenta significa che aumena anche il rischio per
    l'Italia di essere percepito come un Paese poco "sicuro"
    sempre rispetto alla Germania
'''


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
    
    
