# Disk cleanup

Trovato un terminale funzionante ti serve una password, ma per fortuna chiunque abbia reso pubblici tutti quei dati ha fornito una lista di utenti con password rispettive trapelate da chissà dove. **«**Gentile da parte loro**»**, pensi. Provi tutte le credenziali finché non trovi un utente funzionante: `bunny`.

Sembra che anche nel Matrix usino Linux (per fortuna), ma per qualche motivo il terminale è molto lento e non puoi nemmeno installare alcuni "strumenti" che ti servono per esplorare meglio il sistema. Eventualmente trovi la fonte del problema: il disco è pieno!

Ti chiedi quanto budget abbiano effettivamente dedicato a questo "Matrix" e se valga la pena continuare, ma alla fine decidi di smettere di pensarci e cerchi una soluzione al problema. Noti che la maggior parte dello spazio è occupato proprio dal tuo utente e decidi di creare uno script in bash per mappare quanti file esistono nella sua home directory.

```bash
$ ls
52581 a
30763 b
41829 c
4986 d
51187 e
161937173 f/
10615 g
$ cd f
$ ls
57019 a
42276204 b/
29529325 c/
58520210 d/
31379510 e/
6832 f
31347 g
40615 h
33859 i
62252 j
$ cd ..
```

Esegui lo script nella home directory (`/home/bunny`) e alla fine ottieni una lista di comandi bash e il loro rispettivo output (il tuo input). 

**Esempio:**

- I comandi sono sempre preceduti da un `$` e il loro risultato viene mostrato nelle linee sottostanti.
- Il comando `ls` mostra quali file (intesi come directory e non) sono presenti nella cartella corrente preceduti dallo spazio che occupano su disco.
- I file con il nome che finiscono per `/` sono delle directory e si può usare `cd <nome_directory>` per entrare al suo interno.

Nell'esempio possiamo vedere che il secondo comando eseguito è `cd f`: 

quindi siamo passati dalla directory `/home/bunny` alla `/home/bunny/f`. 

Se vogliamo tornare alla directory superiore il comando eseguito sarà `cd ..` .

In questo caso la risposta corretta è `/home/bunny/f/j`.

**Il tuo obiettivo è trovare il percorso del file più grande mostrato nel file (directory escluse).**