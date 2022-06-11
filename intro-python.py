#questo è un commento

print("Ciao quanti anni hai?")

eta = input() #qui l'utente può inserire qualcosa e viene rilevato come stringa

print("Cavolo, non sapevo che tu avessi " + eta + " anni")

print('-------------------------------------')

differenza = 100 - int(eta)

print('Ti mancano ' + str(differenza) + ' anni per compiere il tuo centesimo compleanno')

#questa è una lista
miaLista = [1,2,3,4,"pesca", "mele"]

#con questo comando aggiungo il numero alla fine della mia lista 
miaLista.append(7)

#con questo comando cancello l'ultimo elemento della lista
miaLista.pop()

#questi comandi posso anche essere lanciati dalla shell


#come aggiungere/sostituire un elemento alla lista in una determinata posizione
miaLista[0] = 'primo elemento'

#posso inizializzare ed assegnare ad una nuova variabile un elemento della lista
primoElementoLista = miaLista[0]

#inserisco in una nuova lista alcune l'intervallo di elementi che vanno da indice 0 a 3(prima dell'indice 4) della lista "miaLista"
lista2 = miaLista[0:4]

#gli elementi della lista che vanno da 1 a prima di 5
varX = miaLista[1:5]


#questa è una tupla
miaTupla = (44, 48, 'cravatta')

elementoTupla = miaTupla[2]

#ricordati che a differenza delle liste, le tuple non sono modificabili

print('-------------------------------------')

#if
print('inserissci la tua età')

eta = input()

if int(eta) >= 18:
    print('sei maggiorenne')
else:
    print('non sei maggiorenne')

print('-------------------------------------')

#elif
print("quanti anni hai")

eta = input()

if int(eta)>= 18 and int(eta)<21:
    print('sei maggiorenne in italia')
elif int(eta)>=21 and int(eta):
    print("sei maggiorenne sia in italia che negli stati uniti")
else: 
    print('non sei maggiorenne')

print('-------------------------------------')

#i cicli
#ciclo for
for numero in range(6): #stampa da 0 a 5
    print(numero)

print('-------------------------------------')

numbers = 10 #qui parte da 20 xk prima incrementa la variabile
for numb in range(6):
    numbers = numbers + 10
    print(numbers)
    
print('-------------------------------------')

numbers2 = 10 #stampa anche il 10     
for numb in range(6):
    print(numbers2)
    numbers2 = numbers2 + 10 

print('-------------------------------------')

for numb in range(40,50): #stampa da 40 a 49
    print(numb)

print('-------------------------------------')

#ciclo while
contatore = 0
while contatore <= 5:
    print(contatore)
    contatore += 1
print('-------------------------------------')

contatore2 = 0
elemento = 2 
while contatore2 <= 5:
    elemento = elemento*5 #la variabile elemento verrà moltiplicata ad ogni giro *5
    print(elemento)       # fin quando il contatore non arriverà a 5
    contatore2 += 1

print('-------------------------------------')

contatore3 = 0
altroElemento = 10 
while contatore3 <= 5:
    altroElemento = altroElemento*10 
    print(altroElemento)       
    contatore3 += 1
    if altroElemento == 1000:
        break
    
print('-------------------------------------')
print('-------------------------------------')
