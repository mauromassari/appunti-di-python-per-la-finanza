'''
Frontiera efficiente
    Introdotta da markovitz nel 1959 con il libro:
    "Portfolio selection: efficient diversification of investmens"

    Il principio alla base della teoria è quello di individuare
    una combinazione di titoli tale da minimizzare il rischio e
    massimizzare il rendimento coplessivo.

    Sfruttando la correlazione che sussiste fra i titoli in portafoglio
    è possibile trovare le ponderazioni degli investimenti tali da
    minimizzare il rischio e massimizzare il rendimento

    La frontiera efficiente è una rappresentaione grafica di tutte le
    combinazioni di portafolgio che si possono avere

    Sull'asse x vi è il rischio di portafoglio, mentre sull'asse y
    il rendimento atteso di portafoglio
    
'''

'''
Esempi frontiera efficiente

    portafoglio 1 = 50% ferrari e 50% tesla
    Rischio portafoglio 1 = 0.05
    Rendimento atteso 1 = 0.003

    portafoglio 2 = 70% ferrari e 30% tesla
    Rischio portafoglio 2 = 0.06
    Rendimento atteso 2 = 0.004
    
'''

'''
Come realizzare la frontiera efficiente
    - cacolare il rendimento atteso, varianza e deviazione standard di due titol
    
    - creareun ciclo che permetta di calcolare automaticamente il rendimeno
      di portafolgio e il rischio di portafoglio per tutte le
      possibili combinazioni
      
    - creare un grafico che visualizzi tutte le possibili combinazioni
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
dfFerrari = web.DataReader('RACE','yahoo',start,end)


#creo prima due dataframe vuoti
ricampionato_tesla = pd.DataFrame()
ricampionato_ferrari = pd.DataFrame()

#qui faccio un ricampionamento dei dati scaricati e li inserisco nei nuoi datafr
ricampionato_tesla = dfTesla.resample('MS').first()
ricampionato_ferrari = dfFerrari.resample('MS').first()

#creo altri due dataframe vuoti
rend_tesla = pd.DataFrame()
rend_ferrari = pd.DataFrame()

#prendi le colonne di Adj close ricampionate e le inserisco nei nuovi dataframe
rend_tesla['Rendimenti'] = ricampionato_tesla['Adj Close'].pct_change()
rend_ferrari['Rendimenti'] = ricampionato_ferrari['Adj Close'].pct_change()

#rimuovo i valori Nan
rend_tesla.dropna(inplace = True)
rend_ferrari.dropna(inplace = True)

#calcolo la media dei rendimenti attesa ricampionati
media_rend_tesla = rend_tesla['Rendimenti'].mean()
media_rend_ferrari = rend_ferrari['Rendimenti'].mean()

#calcolo della varianza
var_rend_tesla = rend_tesla['Rendimenti'].var()
var_rend_ferrari = rend_ferrari['Rendimenti'].var()

#calcolo della deviazione standard
devStand_tesla = math.sqrt(var_rend_tesla)
devStand_ferrari = math.sqrt(var_rend_ferrari)

#calcolo della correlazione
corr = rend_tesla['Rendimenti'].corr(rend_ferrari['Rendimenti'])


#calcolo frontiera efficiente
ponderazione1 = 1
ponderazione2 = 2
x = 0

while x <= 50:
    rischiosita=(ponderazione1*devStand_tesla)**2+(ponderazione2*devStand_ferrari)**2+2*ponderazione1*ponderazione2*devStand_tesla*devStand_ferrari*corr
    rischiosita_portafoglio = math.sqrt(rischiosita)
    rendimento_portafoglio = media_rend_tesla  * ponderazione1 + media_rend_ferrari * ponderazione2
    ponderazione1 = ponderazione1 - 0.02 #tolgo il 2% ad ogni ciclo
    ponderazione2 = ponderazione2 + 0.02 #aggiungo il 2% ad ogni ciclo
    x+=1
    plt.scatter(rischiosita_portafoglio, rendimento_portafoglio, color='k', s=10)

plt.xlabel('Deviazione standard')
plt.ylabel('Rendimento atteso')
plt.title('Frontiera efficiente')
plt.show()

#il titolo che ha la deviaszione standard più elevata
# corrsiponde a quello che se presente al 100% nel portafoglio
# è il più rischioso
    
    
