# Recursive keys

**Descrizione**

Una volta eliminati i file più pesanti dal sistema, noti che l’utente **`bunny`** potrebbe avere più accesso al sistema di quanto sembri. Sfogliando tra i suoi file trovi **progetti interni**, **algoritmi di crittazione e hashing incompleti**, dati personali di persone e… in una directory appare un file chiamato **`creds.zip`**.

Accanto ad esso, l’unico altro file presente è un semplice documento di testo contenente una frase enigmatica:

*“The answer lies within J_mod(2025)”*

Il nome **J_mod** ti ricorda la **successione combinata Padovan-Jacobsthal**, una sequenza costruita sulla base dei numeri della successione di **Padovan** e di una variazione della successione di **Jacobsthal**.

Provi a estrarre il file **creds.zip**, ma è protetto da password. È in quel momento che capisci esattamente cosa devi fare:

**Calcola il valore di**  $J_{mod}(2025)$  **e usalo come password per sbloccare i contenuti del file!**

---

**Definizione della successione combinata Padovan-Jacobsthal**

La successione modificata  $J_{mod}(n)$  si basa sulla successione di **Padovan**, definita come:

$P(n) = P(n-2) + P(n-3)$

con i seguenti valori iniziali:

$P(0) = 1, \quad P(1) = 1, \quad P(2) = 1$

Usando questi numeri, la successione **modificata** di **Jacobsthal** viene definita come:

$J_{mod}(n) = J_{mod}(n - P(n-1)) + 2J_{mod}(n - P(n-2))$

con valori iniziali:

$J_{mod}(0) = 0, \quad J_{mod}(1) = 1$

Tuttavia, per evitare **indici negativi**, se  $P(n-1) \geq n$  o ,  $P(n-2) \geq n$ allora si utilizza la formula di fallback:

$J_{mod}(n) = J_{mod}(n-1) + 2J_{mod}(n-2)$

Poiché i valori della sequenza crescono rapidamente, per evitare numeri troppo grandi, il risultato deve essere **modulo**  $10^6$  (cioè, il resto della divisione per  $10^6$ ).

---

**Esempio di input/output**

<aside>
💡

| **Input** | **Output** |
| --- | --- |
| 5 | 27 |
| 10 | 19 |
| 20 | 43667 |
| 50 | 118419 ( % $10^6$) |
| 100 | 966867 ( % $10^6$) |


</aside>