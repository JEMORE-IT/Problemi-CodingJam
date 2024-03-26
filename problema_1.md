# Esercizio 1
L'anno scorso a Pasqua, in casa del dottor Pivetta, dall'uovo di cioccolata saltò fuori un pulcino cosmico, simile in tutto ai pulcini terrestri, ma con un berretto da capitano in testa e un'antenna della televisione sul berretto. 

Il pulcino si guardava intorno con aria malcontenta. “Che seccatura! Che brutta seccatura!” Cos'è che la preoccupa? - domandò il dottor Pivetta. “Avete rotto il sistema di navigazione dell'uovo volante e io non potrò tornare su Marte Ottavo.” disse il pulcino mostrando una copia del sistema di navigazione al dottor Pivetta (il tuo input).

Il sistema di navigazione è composto da diverse linee, ognuna delle quali contiene uno o più gruppi. Ogni gruppo contiene a sua volta zero o più gruppi. Gruppi adiacenti non sono separati da alcun delimitatore: quando un gruppo si chiude il successivo può aprirsi immediatamente. Ogni gruppo è delimitato da uno delle seguenti quattro coppie di caratteri: 
- Se un gruppo si apre con un (, deve chiudersi con una );
- Se un gruppo si apre con un [, deve chiudersi con una ];
- Se un gruppo si apre con un {, deve chiudersi con una };
- Se un gruppo si apre con un <, deve chiudersi con una >;

Questo significa che () identifica un gruppo che non contiene altri gruppi, così come [], {} e <>. Esempi di gruppi e sottogruppi più complessi sono riportati di seguito: `([])`, `{()()()}`, `<([{}])>`, `[<>({}){}[([])<>]]`, `(((((((((())))))))))`, ecc.

Alcune linee sono incomplete ed altre corrotte. Per aiutare il pulcino cosmico tu e il dottor Pivetta dovete trovare e scartare le linee corrotte. 

Una riga è corrotta se un gruppo si chiude con il carattere sbagliato,  ad esempio: (], {()()()>, (((()))}, <([]){()}[{}]). I gruppi corrotti possono comparire in qualsiasi posizione nella linea. 

Ad esempio, dato il seguente sistema di navigazione, 

```
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
```

alcune delle linee sono incomplete, ma non corrotte, e possono quindi essere ignorate. Le rimanenti cinque linee sono invece corrotte (alcune anche incomplete): 

`{([(<{}[<>[]}>{[]{[(<()>` - } si trova al posto di ];
`[[<[([]))<([[{}[[()]]]` - ) si trova al posto di ];
`[{[{({}]{}}([{[{{{}}([]` - ] si trova al posto di );
`[<(<(<(<{}))><([]([]()` - ) si trova al posto di >;
`<{([([[(<>()){}]>(<<{{` - > si trova al posto di ].

Un modo per valutare gli errori di sintassi è quello di assegnare un punteggio ad ogni errore, riga per riga. Per fare ciò è sufficiente prendere il primo carattere non valido nella riga e cercarlo nella seguente tabella: 

- ):         7 punti
- ]:       42 punti
- }:   1337 punti
- >: 64880 punti

Quindi, prendendo l’esempio precedente, il carattere non valido ) è stato trovato due volte (2 * 7 = 14 punti); il carattere non valido ] è comparso una volta (42 punti); il carattere non valido } è apparso una volta (1337 punti), infine, il carattere non valido > è apparso una volta (64880 punti), per un totale di 14 + 42 + 1337 + 64880 = 66273.

Trova il primo carattere illegale in ogni riga danneggiata del sottosistema di navigazione fornito come input_1.txt . Qual è il punteggio totale degli errori di sintassi per tali errori?
