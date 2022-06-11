'''
DISTRIBUZIONE DI PROBABILITA'

Data una variabile aleatoria X, la sua distribuzione
di probabilità è la funzione che a un insieme di valori possibili
di X associa la rispettiva probabilità


DISTRIBUZ DISCRETE
trattano variabili intere (ad esempio il lancio di un dado)


DISTRIBUZ Continue
trattano variabili continue (
ad esempio i rendimenti o i prezzi di un'azione)


DISTRIBUZIONE NORMALE (o Gaussiana)
è una distribuzione continua usata per descrivere
variabili che tendono a concentrarsi attorno a un singolo valor medio.
Il grafico simmetrico e ha forma a campana.

Questa è facile da utilizzare perché bastano 2 parametri
per identificarla:
- la media e la varianza

Esemopio
N(media = 2; varianza = 1)

varianza minore = volatilità minore
se aumentiamo la varianza = più volatilità

FUNZIONE DI RIPARTIZIONE
è la probabilità che una variabile sia maggiore o minore
di un determinat valore (ad esempio la probabilità che nel lancio di un
dado mi capiti un numero minore o uguale a 3)
'''

''' La disribuzione dei prezzi azionari

il logaritmo naturale dei prezzi di un'azione si distribuisce in modo normale'''


'''
1- Calcoleremo la media e la varianza della distribuzione del logaritmo dei prezzi

2- Avendo i parametri della distribuzione possiamo calcolare con Python la probabilità che
   il prezzo di un'azione sia maggiore o minore ad un determinato valore.
   A tal scopo useremo la funzione di ripartizione
'''
