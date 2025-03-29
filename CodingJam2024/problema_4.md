# Quarto Problema
Il Dottor Pivetta, osservando il pulcino cosmico all’opera per riparare il sistema di navigazione, vede che tutti i progetti sono sparsi alla rinfusa e chiede: “Non siete preoccupati che chiunque passi sia in grado di leggere i vostri documenti super segreti?” Il pulcino fa un piccolo sorrisetto compiaciuto e inizia a spiegare: “Tutti i nostri dati sono criptati da un algoritmo inventato da me personalmente!”
“In particolare ho generato 4 numeri numeri casuali tra 1024 e 4096: `x,y,w,z`. Poi ho calcolato le seguenti grandezze:
```
M=xy-1
e=wM+x
d=zM+y
n=ed-1M
```
Mi bastano `e` ed `n` per codificare qualunque testo, procedendo in questo modo:
prendo il testo (una sequenza di numeri da 0 a 255 corrispondenti alla codifica in UTF-8 del messaggio). Ad esempio: “Alè!” sarebbe (in hex) `41 6C C3 A8 21`.
Ogni 5 byte vengono combinati formando un numero `m` a 40 bit senza segno in big endian. Ad esempio i byte `00 00 00 01 00` (sono 5 byte scritti in base 16) formano il numero 2^8=256, mentre i byte `00 80 00 00 00` formano il numero 2^31=2147483648 e i byte `80 00 00 00 00` formano il numero 2^39=549755813888. La sequenza di byte `41 6C C3 A8 21` produce il numero 280997636129. Se ho meno di 5 byte, alla fine, riempio con dei byte uguali a zero.
Ogni numero viene criptato facendo il calcolo `c=em (mod n)`, ovvero il valore criptato `c` è dato dal resto della divisione per `n` del prodotto di `e` per `m`.
I nostri dati sono conservati come sequenze di numeri codificati in questo modo!”
Il Dottor Pivetta è abbastanza perplesso e chiede: “Ma come fate a decodificare i numeri?”
Il pulcino prontamente risponde: “Facile! Il valore ricostruito `r` può essere ottenuto come `r=cd (mod n)`, ovvero calcolando il resto della divisione per `n` del prodotto di `c` per `d`.”
Il Dottor Pivetta è adesso completamente spiazzato e chiede: “Ma non è possibile che qualcuno decodifichi il messaggio senza sapere i valori utilizzati per criptarlo?”
Il pulcino è adesso fierissimo: “Impossibile! Nessuno ci potrebbe riuscire nemmeno in un milione di anni se provasse a caso. Dirò di più: i valori di e e di n sono pubblici e noti a tutti! Eppure nessun pulcino è mai riuscito a decodificare il messaggio. Ad esempio: ho codificato un messaggio usando `e=17459243613` e `n=66624478857659`:
```
35784176028369
63561241316534
40946911928892
56405696498538
38978109180990
16444276162313
38053979586003
57562671757853
```

Prova a decodificarlo!”

Qual è il messaggio criptato dal pulcino cosmico?
