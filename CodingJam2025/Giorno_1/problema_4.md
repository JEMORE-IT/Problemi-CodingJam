# Keep counting

Riesci ad estrarre il contenuto del file e ti trovi di fronte a due cartelle chiamate rispettivamente `edge` e `key` . Decidi di aprire la prima e trovi altri due file di testo, prima di aprirli preghi che non siano altri strani enigmi. Ti chiedi chi possa averli lasciati qua: se avessero voluto nascondere queste informazioni di certo non ti avrebbero lasciato degli indizi.

Nel primo file vedi una stringa incomprensibile e nel secondo una lista di istruzioni: è l’ora di trovare un’altra chiave di decrittazione. **Trova tutte le sottostringhe della parola all’interno di input.txt, conta quante iniziano per vocale e quante per consonante e somma le CIFRE dei numeri che trovi tra loro.**

Beh almeno questa volta non devi interpretare quello che ti chiede…

Esempio: applichiamo la procedura alla parola `source` .

In questo caso le sottostringhe che iniziano per consonante sono **11**:

```markdown
's'
'r'
'c'
'so'
'rc'
'ce'
'sou'
'rce'
'sour'
'sourc'
'source'
```

Invece quelle che iniziano per vocale sono **10**:

```markdown
'o'
'u'
'e'
'ou'
'ur'
'our'
'urc'
'ourc'
'urce'
'ource'
```

Calcoliamo infine la comma delle cifre: 1 + 1 + 1 + 0 = 3(dai numeri ’11’ e ‘10’)