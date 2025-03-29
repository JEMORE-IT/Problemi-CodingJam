# MTX Protocol

Recentemente un gruppo di hacker sconosciuto è riuscito ad ottenere informazioni su "Matrix": il sistema che simula la nostra realtà così come la vediamo... o almeno questo è quello che si dice online.
Un po' scettico e preso dalla curiosità decidi di dare un' occhiata alle presunte informazioni trapelate.

Il primo file che ti salta all'occhio è un file chiamato `mtrx_ips.dmp`: è una lista di IP di terminali usati dagli agenti del matrix. Secondo gli attaccanti i terminali non sono protetti da password ma usano un protocollo particolare per comunicare che li rende inaccessibili usando `ssh`.

Trovi un'implementazione del protocollo scritta in python, ma non sembra funzionare per nessun IP della lista. Decidi allora di eseguire un "ping" su tutti gli IP per vedere se sono ancora online e noti che non tutti i terminali restituiscono una risposta corretta (il tuo input). **Il tuo obiettivo è trovare l’indirizzo IP dell’UNICO terminale funzionante che risponde correttamente alla richiesta di ping.**

Il tuo input è formato da tante linee strutturate in questo modo:

```bash
SAYING HI TO <ip>: <dati> (time=<numero>ms) (v=32)
```

La parte interessante è il campo dati, una stringa esadecimale che rappresenta 32 bytes avente queste caratteristiche:

- la sequenza di bytes deve sempre iniziare con i byte `44 45 44 5a`
- la sequenza di bytes deve sempre terminare con i byte `4e 55 54 53`
- non ci devono essere due byte ripetuti di seguito nella stringa
- se è presente almeno uno di questi byte “cattivi” `11 42 00` la connessione non è sicura e la sequenza di bytes non è valida
- devono essere presenti almeno tre byte tra questi bytes magici `13 37 2a b1`

File di esempio:

```bash
$ python3 [scan.py](http://scan.py/) --file=test_ips.dmp
SAYING HI TO 185.155.1.1: 4445445a135c20092a63991492b22af369bb747e56af1f6e52c57bc74e555453 (time=27ms) (v=32)
SAYING HI TO 185.155.2.1: 4445445ab17e64f5f9b13de1df36fe9cb4aec7583fce88bc085606cdbc594e555453 (time=21ms) (v=32)
SAYING HI TO 185.155.3.1: 4445445aa3e35c4715ec127c5ecfdf3788de12c464c26a0fe4 (time=23ms) (v=32)
SAYING HI TO 185.155.4.1: 4445445a6fa662792f9a2103b123a3fd9c87c8c5f2be3437554e555453 (time=31ms) (v=32)
Done! The scan took <0s.
$
```

- la risposta dell’IP `138.243.2.1` non è valida perchè il numero di byte della sequenza non è corretto.
- la risposta dell’IP `185.155.3.1` non è valida perchè la sequenza di byte finale non è corretta
- la risposta dell’IP `185.155.4.1` invece non contiene abbastanza bit “buoni”
- il primo IP rispetta tutti i requisiti necessari