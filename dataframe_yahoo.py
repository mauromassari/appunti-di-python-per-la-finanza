''' questo è un commento multilinea '''

#importo dati da yahoo finance

#importo le librerie necessarie
import pandas as pd
import datetime as dt
import pandas_datareader.data as web

#definizione data inizio rilevazione
start = dt.datetime(2020,1,1)

#definizione data inizio rilevazione
end = dt.datetime(2022,1,1)

#importo il dataframe
#df è la variabile che conterrà il dataframe,avrei potuto chiamarla anche pippo
df = web.DataReader('TSLA','yahoo',start,end)
print(df) 

'''
print('-------------------')
#importo soltanto la colonna High e l'indice(data)
df['High'] #puoi lanciare questa riga direttamente nella shell(qui infatti è inutile)
high = df['High']
print(high)

print('-------------------')
#imposto un indice per ogni riga e la data diventa una colonna normale
df.reset_index() #posso lanciare #puoi lanciare questa riga direttamente nella shell(qui infatti è inutile)
                 #se lancio questo comando nella shell cmq il cambiamento non è permanente
print(df.reset_index())

print('-------------------')
#per rendere la modifica dell'indice permanete
df.reset_index(inplace=True)

print('-------------------')
#per modificare in modo permanente la colonna dell'indice con un altra colonna
df.set_index('Low', inplace= True)
print(df)

print('-------------------')
#per modificare in modo permanente la colonna dell'indice con un altra colonna
df.set_index('Date', inplace= True)
print(df)

print('-------------------')
#per poter visualizzare un massismo di righe e un massimo di colonne
pd.set_option('display.max_rows',1000,'display.max_columns',1000)
print(df)

print('-------------------')
#come isolare un singolo valore di una determinata colonna
singoloValore = df['High'][0]
print(singoloValore)

print('-------------------')
#come isolare una singola riga
df.iloc[[3]] #inserisco l'indice della stessa considerando che parte da 0
singolaRiga = df.iloc[[3]]
print(singolaRiga)

print('-------------------')
#come isolare più righe
df.iloc[[0,1,2]] #inserisco l'indice delle righe considerando che partono da 0
righeSelezionate = df.iloc[[0,1,2]]
print(righeSelezionate)

print('-------------------')
#come isolare un intervallo di righe
#qui seleziono le righe che vanno da 0 a prima di 2,quindi la righa 0 e 1
df.iloc[0:2] #inserisco l'indice delle righe considerando che partono da 0
righeSelezionate = df.iloc[0:2]
print(righeSelezionate)

print('-------------------')
#come isolare due colonne
df[['High','Close']] 
colonneSelezionate = df[['High','Close']]
print(colonneSelezionate)

print('-------------------')
#come isolare due colonne e solo derminare righe
df[['High','Close']].iloc[0:4] 
solo = df[['High','Close']].iloc[0:4] #da riga 0 a riga 3(prima di 4)
print(solo)

print('-------------------')
#mostrare solo righe che abbiano alla colonna 'Low' valori minori di 100
df[df['Low'] < 100]
df2 = df[df['Low'] < 100]
print(df2)

print('-------------------')
#inserisco in una nuova variabile df3 soltanto la col 'Low' e la quella delle date
df['Low']
df3 = df['Low']
print(df3)

print('-------------------')
#creo un datatframe vuoto
df4 = pd.DataFrame()

#e ci aggiiungo una colonna del dataframe 'df' ma con un nome diverso
df4['valori'] = df['Adj Close']
print(df4)

#creo un altro datatframe vuoto
df5 = pd.DataFrame()

#aggiungo tre colonne del dataframe 'df' rispettivamente con tre nomi diversi
df5[['Valori','Valori2','Valori3']] = df[['Open','Adj Close','Volume']]
print(df5)

#aggiungo un'altra colonna
df5['Valori4'] = df['Close']
print(df5)

#se invece volessi aggiungere una colonna in una determinata posizione
df5.insert(0, column = 'Valori5', value = df['High'])
print(df5)

#per rinominare l'intestazione di una tabella
df5.rename(columns = {'Valori4':'Prezzo chiusura'}, inplace = True)
print(df5)

#per rinominare le intestazioni di più colonne
df5.rename(columns = {'Valori':'Prezzo apertura', 'Valori3':'Azioni Scambiate'}, inplace = True)
print(df5)

#per elimiare una colonna
df5.drop(['Prezzo apertura'], axis='columns', inplace=True)
print(df5)

#per elimiare una riga
df5.drop(df5.index[0], inplace = True)
print(df5)

#per eliminare i valori Nan (not a number)
df.dropna() #provvisorio da lanciare nella shell
df.dropna(inplace = True) #permanente

#per sostituire gli Nan con un nostro valor epredefinito
df.fillna(00000, inplace = True)

#per sostiruirlo col valore presente nella riga precedente
df.fillna(method = 'ffill', inplace = True)
'''
