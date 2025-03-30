Nel cuore del Matrix, un mondo digitale dove nulla è ciò che sembra e ogni pixel cela una scelta, Neo si risveglia in una prigione di caratteri. Intrappolato in un flusso costante di dati, deve decifrare la realtà da dietro il velo del codice.

Il suo obiettivo? Trovare il percorso a costo minimo dalla lettera `a` alla lettera `z` — un tragitto nascosto tra glitch di sistema e inganni del codice, dove ogni simbolo può essere un alleato o una trappola. Solo attraversando correttamente questa griglia di dati potrà avanzare verso la verità.

## Descrizione della matrice:
La Matrice si manifesta come una griglia di dimensione M x N, composta da diversi elementi digitali. Ogni simbolo ha un significato ben preciso e influisce sul costo del percorso:

| Tipo di carattere     | Significato                                                         |
|-----------------------|---------------------------------------------------------------------|
| Lettere minuscole (a–z) | Zone attraversabili. Il loro costo è calcolato come `ASCII % 10` (es: a=7, b=8, i=5, j=6, k=7). |
| Lettere maiuscole (A–Z) | Anche queste sono attraversabili. Il costo è identico alla loro versione minuscola (`ASCII.to_lower() % 10`). |
| Numeri (0–9)          | Puoi attraversarli. Ogni numero aggiunge il valore numerico corrispondente al costo.  |
| Simboli (!@#$...)     | Glitch del sistema: zone instabili, impossibili da attraversare.  |

## Obiettivo:
Individuare il percorso a costo minimo che congiunge una cella contenente la lettera `a` a una cella contenente la lettera `z`, seguendo rigorosamente le regole del sistema. Devi restituire la stringa di caratteri e numeri che corrispondo al percorso a costo minimo.

## Regole:
- Movimento: Solo lungo i quattro assi cardinali — Nord, Sud, Est, Ovest. Nessun salto diagonale: il sistema lo rileverebbe.
- Visite: Ogni cella può essere visitata una sola volta. Tornare indietro significherebbe esporsi al rilevamento degli agenti.
- Ingressi e Uscite: Possono esserci più punti di partenza (`a`) e di arrivo (`z`). Ma solo uno è la via del risveglio — quella con il costo minimo.
- Costo iniziale: Si parte da 0. Ogni mossa aggiunge il costo della nuova cella.

Dimostra di essere l'Eletto. Trova la via. Svela il codice.