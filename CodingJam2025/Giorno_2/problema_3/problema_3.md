# Un messaggio da Morpheus

Neo ha scelto la pillola rossa e si trova a bordo della Nabucodonosor, nella sua cabina. La realtà è difficile da accettare, ma si sta riprendendo e Morpheus gli ha lasciato un messaggio per spiegargli la situazione. 

In genere il codice di Matrix viene codificato con una parola chiave composta di caratteri ASCII che vengono usati per eseguire lo XOR dei vari caratteri del messaggio ciclicamente e ormai l'equipaggio ha imparato a decodificare tutto a mente! Per abituarlo a decodificare il codice di Matrix, il messaggio (composto solo di caratteri ASCII) è stato codificato con una parola chiave di tre caratteri ASCII: il primo carattere col primo della chiave, il secondo col secondo della chiave, il terzo col terzo della chiave, il quarto col primo della chiave, il quinto col secondo della chiave e così via.

Che cos'è Matrix? Che cosa vuole dire Morpheus?

Utilizzando il file `cipher.bin`, un file contenente i codici ASCII crittografati, e la consapevolezza che il testo deve contenere parole italiane comuni, decifra il messaggio.

## Esempi
Se i valori dei caratteri del messaggio cifrato fossero:
```
30 12 3 2 10 3 15
```
con la password `"neo"` si ottiene il messaggio `"pillola"`.

Se i valori dei caratteri del messaggio cifrato fossero:
```
91 65 69 91 78 74 83 76 93 83 13 69 91 13 74 83 67 93 79 95 72
```
con la password `":-)"` si ottiene il messaggio `"allacciati la cintura"`.

Ritorna la password che hai usato per decifrare il messaggio.





