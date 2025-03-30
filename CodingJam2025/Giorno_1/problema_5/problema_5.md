# **Art Keys**

Una volta ottenuta la chiave riesci a decrittare il contenuto del file: sembra un normalissimo indirizzo IP. **«**Che sia un altro terminale?**»**, pensi tra te e te. Provi a connetterti usando il solito protocollo, ma ti serve una password. Provi la stessa password che hai usato per questo terminale senza successo, e ricordi che hai ancora la cartella `key`  da esplorare (che dal nome sembra promettere bene).

Ti trovi davanti ai soliti due file di testo che ti sono ormai troppo familiari. Il primo contiene tanti caratteri disposti a forma di **quadrato** (il tuo input); il secondo file ha invece un’ estensione particolare: `.rkey` . Ti ricordi i file trapelati che hai studiato all’inizio della tua avventura, in particolare un file che parlava delle **Art Keys**. Utilizzando una matrice di caratteri come “password” si può accedere ad un qualsiasi terminale che abbia installato la tua stessa chiave.

Recuperi il file e inizi a leggere: le chiavi sono conservate in forma “mischiata”. Solamente tramite un programma specifico installato in genere su chiavetta le chiavi vengono rese utilizzabili, per poi essere cancellate subito dopo l’uso. Viene spiegato anche l’algoritmo utilizzato per risalire alla chiave originale.

Ipotizziamo di avere questa **matrice quadrata**:

```markdown
. . . . . . . .
. . . . . - . .
. . o . . . . .
. - . . . * . .
. . . . . . . .
. . . . . . o .
. . . . . . . .
. . . . . . . .
```

L’obiettivo è attraversare la matrice seguendo alcune regole:

- `*`  è la cella in cui ti trovi in questo momento. Immaginiamo che il carattere `*` sia un robottino che si muova in una direzione, finchè non incontra un ostacolo che lo costringe a cambiare direzione. **La direzione iniziale è sempre sinistra.**
- `-`  è un **muro** che ti costringe di andare a **sinistra** rispetto alla direzione in cui stai guardando
- `o`  è un **muro** che ti costringe di andare a **destra** rispetto alla direzione in cui stai guardando
- Tutti gli altri caratteri sono da considerarsi spazi vuoti su cui il robottino può muoversi.

Considerando queste regole, dopo 1 passo il robottino si troverà in questa posizione.

```markdown
. . . . . . . .
. . . . . - . .
. . o . . . . .
. - . . * . . .
. . . . . . . .
. . . . . . o .
. . . . . . . .
. . . . . . . .
```

Il robottino si muove verso sinistra finché non incontra il primo muro `-`

```markdown
. . . . . . . .
. . . . . - . .
. . o . . . . .
. - * . . . . .
. . . . . . . .
. . . . . . o .
. . . . . . . .
. . . . . . . .
```

Il robottino, che sta guardando in questo momento verso sinistra, deve girare a sinistra e quindi verso il basso in questo caso:

```markdown
. . . . . . . .
. . . . . - . .
. . o . . . . .
. - . . . . . .
. . * . . . . .
. . . . . . o .
. . . . . . . .
. . . . . . . .
```

Ora il robottino continuerà ad andare verso il basso finchè non arriva alla fine della matrice:

```markdown
. . . . . . . .
. . . . . - . .
. . o . . . . .
. - . . . . . .
. . . . . . . .
. . . . . . o .
. . . . . . . .
. . * . . . . .
```

Quando il robottino arriva alla fine della matrice, lui **arriva dalla parte opposta della riga/colonna su cui si sta muovendo ora**. In questo caso si sta muovendo verso il basso, quindi lungo in colonna, ed è arrivato in fondo: quindi al prossimo passo il robottino tornerà in cima alla colonna.

```markdown
. . * . . . . .
. . . . . - . .
. . o . . . . .
. - . . . . . .
. . . . . . . .
. . . . . . o .
. . . . . . . .
. . . . . . . .
```

Al prossimo passo il robottino si troverà davanti un muro di tipo `o` , quindi il robottino si muoverà nella casella marcata con `X` **** nella matrice sottostante:

```markdown
. . . . . . . .
. **X** * . . - . .
. . o . . . . .
. - . . . . . .
. . . . . . . .
. . . . . . o .
. . . . . . . .
. . . . . . . .
```

Dopo essersi spostato verso sinistra una seconda volta il robottino sarà alla fine della matrice: quindi al prossimo passo si troverà alla fine della riga (casella marcata con `X` )

```markdown
. . . . . . . .
* . . . . - . **X**
. . o . . . . .
. - . . . . . .
. . . . . . . .
. . . . . . o .
. . . . . . . .
. . . . . . . .
```

e così via…

Al 20-esimo passo la matrice sarà questa:

```markdown
. . . . . . . .
. . . . . - . .
. . o . . . . .
. - . . . . . .
. . * . . . . .
. . . . . . o .
. . . . . . . .
. . . . . . . .
```

La matrice reale però ha negli spazi vuoti ha altri caratteri scelti tra questa lista: [`O`, `p`, `T`, `0`, `<`, `>`], inoltre ad ogni carattere è associato un punteggio:

- `O`: 210
- `p`: 136
- `T`: 60
- `0`: 421
- `<`: 130
- `>`: 370
- ogni altro carattere vale 0 punti

Quando il robottino visita una cella che contiene un carattere della lista, dobbiamo **rimpiazzare quel carattere con il carattere successivo.** Ad esempio se il robottino visita una cella contenente il carattere `p` , dovrà essere rimpiazzato con `T` . **L’ultimo carattere della lista sarà rimpiazzato con il primo carattere della lista.** 

Il punteggio della matrice, usato per verificare la correttezza della chiave, si calcola sommando per ogni carattere della matrice il punteggio associato al carattere moltiplicandolo per l’indice della riga (partendo da 0) e sommando l’indice della colonna (partendo da 0) del carattere. In pseudo codice:

```
punteggio = 0
foreach riga
	foreach colonna
		punteggio += punteggio_carattere(matrice[riga][colonna]) * indice_riga + indice_colonna
```

Secondo esempio

```
- 0 . . p . > T
. . . - o . p O
0 p p . . 0 . -
. > o 0 . . p .
. 0 - 0 . 0 > O
p 0 < O . . - .
. - > 0 . > . <
. . > < 0 - . .
```

Usando questa matrice iniziale, partendo dalla 4° riga e 6° colonna, dopo 20 passi il punteggio della matrice è **27892.**

**Obiettivo: calcola il punteggio della matrice (input.txt) dopo 200 passi, partendo dalla 4° riga e 7° colonna.**
