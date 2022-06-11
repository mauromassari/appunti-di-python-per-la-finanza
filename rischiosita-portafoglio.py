'''
Rischiosità di portafoglio

    Nella finanza il portafoglio rappresenta
    l'insieme di titoli detenuti da un investitore

    Logicamente è possibile calcolare la rischiosità,
    oltre che di un singolo titolo, anche dell'intero portafoglio

    Nel calcolo bisogna tenere in considerazione la
    correlazione fra i 2 o più titoli


    se la corr = 1 --> Non vi è alcun beneficio nella diversificazione

    se la corr < 1 --> il beneficio in termini di riduzione del rischio
                       cresce al decrescere del coefficiente di correlazione


    La formula per calcolare la rischiosità di portafoglio con 2 titoli è

    [((qauntità in % del titolo A)*(deviazione standard titolo A))**2 +
    ((qauntità in % del titolo B)*(deviazione standard titolo B))**2 +
    2 * (qauntità in % del titolo A) * (qauntità in % del titolo B) *
    (deviazione standard titolo A)*(deviazione standard titolo B) *
    correlazione fra titolo A e B] tutto sotto radice quadrata
'''

#Ipotizziamo di avere 50% azioni di Tesla e 50% azioni di Ferrari

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

#calolo la varianza dei due titoli
varTesla = df4['Rendimenti'].var() 
varFerrari = df3['Rendimenti'].var()

#importa la libreria math per calcolare la radice quadrata
import math

#calcolo la deviazione standard dei due titoli
devStandTesla = math.sqrt(varTesla)
devStandFerrari = math.sqrt(varFerrari)


#calcolo della correlazione fra i due titoli
corr = df3['Rendimenti'].corr(df4['Rendimenti'])

#calcolo la rischiosità del portafoglio
#            50%                    50%                       50% 50%
varianza_p =(0.5*devStandTesla)**2+(0.5*devStandFerrari)**2+2*0.5*0.5*devStandTesla*devStandFerrari*corr

rischiosità_portafoglio = math.sqrt(varianza_p)
print(rischiosità_portafoglio)
