#importo dati da yahoo finance

#importo le librerie necessarie
import pandas as pd
import datetime as dt
import pandas_datareader.data as web

#definizione data inizio rilevazione
start = dt.datetime(2020,1,1)

#definizione data inizio rilevazione
end = dt.datetime(2022,1,1)

#importo i dataframe di Tesla e Ferrari
#df è la variabile che conterrà il dataframe,avrei potuto chiamarla anche pippo
df = web.DataReader('TSLA','yahoo',start,end)
df2 = web.DataReader('RACE','yahoo',start,end)

#unisco i 2 dataframe in un unico dataframe verticalmente
df3 = pd.concat([df, df2])
 #print(df3)

 #imposto il numero max di righe e colonne che voglio visualizzare
pd.set_option('display.max_rows', 1000, 'display.max_columns', 1000)

#unisco i 2 dataframe orizzontalmente
#imposto date come indice
 #df4 = pd.merge(df, df2, on = 'Date')


#----------------------

#Ricampionamento = Riduciamo il campione da analizzare (la popolazione) - si crea un sottoinsieme
    #riduciamo così i tempi di calcolo

#creo prima un dataframe vuoto
dfRicamp = pd.DataFrame()

#in questo nuovo dataframe creo una colonna che chiamo 'Ricampionato'
    #Poi seleziono quale dataframe e di questo quale colonna ricampionare
        #infine scelgo la frequnza:
            # W - settimnale (ultimo giorno della settimana)
            # M - mensile    (ultimo giorno del mese)
            # SM - a metà del mese
            # Q - trimestrale
            # A - annuale
           
dfRicamp['Ricampionato'] = df['Adj Close'].resample('W').last()
print(dfRicamp)


#ora riempo lo stesso dataframe ma con un ricampionamento mensile (ultimo giorno del mese)
    #creo prima un dataframe vuoto
dfRicamp1 = pd.DataFrame()

dfRicamp1['Ricampionato'] = df['Adj Close'].resample('M').last()
print(dfRicamp1)


#ora riempo lo stesso dataframe ma con un ricampionamento mensile (primo giorno del mese)
    #creo prima un dataframe vuoto
dfRicamp2 = pd.DataFrame()

dfRicamp2['Ricampionato'] = df['Adj Close'].resample('MS').first()
dfRicamp2['Ricampionato2'] = df['High'].resample('MS').first()
print(dfRicamp2)
