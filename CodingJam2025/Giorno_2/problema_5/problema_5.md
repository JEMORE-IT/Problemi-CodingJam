Neo si è appena incredibilmente ripreso dopo essere morto, grazie a Trinity. È l'eletto ed è finalmente in grado di vedere Matrix per quello che è: un enorme processore interconnesso con tutto e tutti. Questo è dotato di un unico accumulatore,inizialmente azzerato, che viene usato per fare i calcoli e spostare dati dalla memoria.

Matrix, il sistema delle macchine, legge un valore numerico `n` alla volta, codificato come una colonna verticale di `n` simboli casuali, dalla memoria e dopo ogni lettura sposta la posizione di lettura alla cella/colonna successiva. Inizialmente parte dalla prima colonna del file di input, numerata a partire da 0.

Il valore letto è un comando numerico che dice alla macchina che cosa fare:

comando | descrizione
--------|------------
aa| legge un valore dalla cella di memoria all'indirizzo specificato nella cella successiva e lo inserisce nell'accumulatore poi incrementa la posizione di lettura.
bb| scrive il valore dell'accumulatore nella cella di memoria all'indirizzo specificato nella cella successiva poi incrementa la posizione di lettura. Se l'indirizzo di destinazione è 0xd1, il carattere viene scritto in output.
cc| legge un valore dalla cella di memoria all'indirizzo specificato nella cella successiva e lo somma all'accumulatore poi incrementa la posizione di lettura.
dd| legge un valore dalla cella di memoria all'indirizzo specificato nella cella successiva e lo sottrae all'accumulatore poi incrementa la posizione di lettura.
ee| sposta la posizione di lettura all'indirizzo specificato nella cella successiva
ef| se il valore dell'accumulatore è uguale a 0, sposta la posizione di lettura all'indirizzo specificato nella cella successiva, altrimenti incrementa la posizione di lettura.
ff| termina l'esecuzione del programma

Neo ha preparato nel file `input.txt` un messaggio per l'umanità e le macchine: che cosa dice?

## Esempio
Il file seguente:
```
abcdef
abcd f
abcd f
a c  f
a     
```
sarebbe la codifica della sequenza `5,3,4,3,1,4` (che non significa nulla per la macchina).

Avendo invece un file che corrispondesse alla sequenza `0xaa, 0x06, 0xbb, 0xd1, 0xff, 0xff, 0x41`, la macchina produrrebbe in output il simbolo `'A'`. Infatti:

1. Legge il comando `0xaa` -> legge il dato alla cella 6 trovando il valore `0x41` e lo mette nell'accumulatore. -> si sposta alla cella 2.
2. Legge il comando `0xbb` -> scrive alla cella `0xd1` il dato nell'accumulatore, ovvero lo mette in output. -> si sposta alla cella 4.
3. Legge il comando `0xff` e termina.

Avendo un file che corrispondesse alla sequenza `0xee, 0x03, 0x20, 0xaa, 0x0a, 0xcc, 0x02, 0xbb, 0xd1, 0xff, 0x41`, la macchina produrrebbe in output il simbolo `'a'`. Infatti:

1. Legge il comando `0xee` -> sposta la posizione di lettura all'indirizzo 3.
2. Legge il comando `0xaa` -> legge il dato alla cella 10 trovando il valore 0x41 e lo mette nell'accumulatore. -> si sposta alla cella 5.
3. Legge il comando `0xcc` -> somma all'accumulatore il valore alla cella 2, che è `0x20`. L'accumulatore è ora `0x61`. -> si sposta alla cella 7.
4. Legge il comando `0xbb` -> scrive alla cella `0xd1` il dato nell'accumulatore, ovvero lo mette in output. -> si sposta alla cella 9.
5. Legge il comando 0xff e termina.

Che cosa avrà detto Neo al mondo col suo file `input.txt`?