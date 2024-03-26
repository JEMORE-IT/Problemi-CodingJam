# Secondo Problema
I pulcini cosmici in attesa di imbarcarsi sulle loro navi spaziali sono soliti mettersi in fila e fare una ginnastica coordinata da un gallo comandante che li aiuta anche a migliorare la coordinazione in volo. 

In particolare si posizionano in fila indiana tutti rivolti verso l’ingresso della navicella e possono essere o in piedi, oppure accovacciati. 

Se un pulcino è in piedi, tutti quelli dietro di lui non vedono la nave spaziale. Viceversa, un pulcino che davanti a sé non ha pulcini in piedi vede la nave spaziale. 
Inizialmente tutti i pulcini sono in piedi. 
Ogni volta che il gallo comandante, posizionato in fondo alla fila, ovvero alle spalle dei pulcini, grida “Cambio!” tutti i pulcini che riescono a vedere la nave spaziale si alzano se sono accovacciati, oppure si accovacciano se erano in piedi. I pulcini che non riescono a vedere la nave spaziale stanno fermi e aspettano.

Avendo `N` pulcini, se il gallo comandante grida “Cambio!” per `K` volte, riuscirà a vedere la navicella spaziale?

Viene fornito un file di input (input_2.txt) con `T` casi (righe). Ogni caso contiene due numeri interi, `N` e `K`.

L’output richiesto è il numero di casi nei quali il gallo comandante riesce a vedere la navicella spaziale.

Esempio di input:
```
1 0
1 1
2 1
2 3
4 47
```

Elaborazione:
- Caso 1: C’è un solo pulcino in piedi. Il gallo non dice nulla. Non riesce a vedere la navicella.
- Caso 2: C’è un solo pulcino in piedi. Il gallo dice “Cambio!”. Il pulcino (che vede la navicella) si accovaccia. Il gallo riesce a vedere la navicella.
- Caso 3: Ci sono due pulcini in piedi. Il gallo dice “Cambio!”. Il primo pulcino (quello più verso la navicella e che quindi la vede) si accovaccia. L’altro (che non vedeva la navicella) resta in piedi. Il gallo non riesce a vedere la navicella. 
- Caso 4: Ci sono due pulcini in piedi. Il gallo dice “Cambio!” (1). Il primo pulcino (quello più verso la navicella e che quindi la vede) si accovaccia. L’altro (che non vedeva la navicella) resta in piedi. Il gallo dice “Cambio!” (2). Il primo pulcino si alza e il secondo si accovaccia. Il gallo dice “Cambio!” (3). Il primo pulcino si accovaccia, mentre il secondo (che non vedeva la navicella) resta fermo, cioè accovacciato. Il gallo riesce a vedere la navicella.
- Caso 5: Con 4 pulcini e 47 cambi la cosa è più lunga. Alla fine, il gallo riesce a vedere la navicella.

La risposta finale sarà 3

Dato il seguente input_2.txt come file di input, in quanti casi il gallo comandante riesce a vedere la navicella spaziale?
