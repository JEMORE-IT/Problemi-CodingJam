# Il messaggio misterioso

Thomas Anderson, conosciuto nel mondo digitale come Neo, è un hacker dalla doppia vita. Da tempo sospetta che qualcosa non vada nel mondo in cui vive, ma non riesce a capire cosa. Una notte, un po' in dormiveglia sul suo letto, viene svegliato da una strana sensazione e nell'editor di testo che aveva lasciato aperto iniziano a comparire strane sequenze di caratteri, probabilmente frammenti di un codice di qualche tipo. Neo sa che questo non è un messaggio qualsiasi. Qualcuno lo sta mettendo alla prova. 

Salvato il file, lo esamina e vede che contiene molte righe di codice, ognuna delle quali rappresenta un enigma da risolvere. Ogni riga contiene due stringhe separate da spazio e osservando bene nota che la prima è sempre più lunga della seconda e si assomigliano molto. Alcune volte la seconda può essere ottenuta dalla prima rimuovendo una sola sottostringa (una sequenza di caratteri consecutivi), mentre altre volte no. Questa sequenza di vero e falso probabilmente ha un significato.

Il problema è che il codice è pieno di informazioni ridondanti, simboli e dati apparentemente casuali. Neo deve scoprire se esiste in ogni riga un unico frammento che, se rimosso, rivela il messaggio nascosto. È il primo passo per trovare la verità.

## Descrizione del problema
Il file di input è composto di numerose righee ogni riga ha due stringhe separate da uno spazio `a` e `b`.

Per ogni riga, si deve determinare se è possibile ottenere `b` da `a` rimuovendo esattamente una sottostringa continua. La rimozione deve avvenire in un solo passaggio e l'ordine dei caratteri rimanenti deve rimanere inalterato.

Le stringhe sono composte esclusivamente da caratteri ASCII compresi tra 33 e 126 (ovvero tutti i caratteri stampabili eccetto lo spazio).

Ogni riga produce un bit pari a 1 se è possibile ottenere b rimuovendo una sola sottostringa da a, altrimenti un bit pari a 0. Questi bit, dal più significativo al meno significativo,  formano una stringa di testo che è la soluzione del problema.

## Esempio
Input:
```
l>z>Nf8/?U l>>?U
G@Mpe<nf9M G@M9M
L}!pTQH]eF L}TeF
#zp&W`=AeW W`AeW
S=Ne$')+8q S=Ne8
\F8'Ejk8r' \jk8r
V<siZHO)8A VsZO8
dUb<,XHgqk dUb<k
mSR|vLugO* mS|L*
a)miY]nhZu ]nhZu
*-EBvoo5x: *o5x:
EH@{q~n#c~ E@{c~
w_er('rMYa _er('
77ze`GA8r[ 77zeG
;[9u2Uc^E? ;[9u2
f5:s|Y2at{ f5at{
```

Output:
```
Ac
```

### Spiegazione
- Nella prima riga, `"l>>?U"` non può essere ottenuto rimuovendo una sola stringa, quindi produciamo un bit uguale a 0.
- Nella seconda riga, `"G@M9M"` si ottiene rimuovendo `"pe<nf"`, quindi produciamo un bit uguale a 1.
- Nelle righe da 3 a 7, non è possibile ottenere la seconda stringa dalla prima, quindi sono tutti 0.
- Nella riga 8, `"dUb<k"` si ottiene rimuovendo `",XHgq"`, quindi produciamo un bit uguale a 1.
- Successivamente, danno 1 le righe 10, 11, 15 e 16.

In sequenza i bit ottenuti sono `01000001 01100011` in esadecimale `41 63`, che corrispondono ai due caratteri ASCII `A` e `c`.


