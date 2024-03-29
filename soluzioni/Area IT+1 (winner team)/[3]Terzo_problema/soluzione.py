from collections import deque

arr = deque(
    [2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2,
     1, 3,
     2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 2, 2, 7, 4, 2, 3, 2, 8, 12, 2, 2, 2, 7, 4, 2, 3, 2, 8, 12, 2, 4, 2, 3, 4, 2, 1, 2,
     1,
     3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3,
     8,
     8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4,
     2,
     3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9,
     7,
     4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2])

r = 1000000000
k = 100


# cerco quante iterazioni servono affinchè si ripetano gli stessi numeri:
def funz(r, k, arr):
    cicli = 0
    pancetta_tmp = 0
    states = {}
    while cicli < r:
        buff = 0
        while buff + arr[0] <= k:
            buff += arr[0]
            arr.append(arr.popleft())
        pancetta_tmp += buff

        state = tuple(arr)
        cicli += 1
        if state in states:
            # Calcoliamo la dimensione del ciclo e la pancetta del ciclo
            dimensione_loop = cicli - states[state][1]
            pancetta_loop = pancetta_tmp - states[state][0]

            # Calcoliamo il numero di cicli rimanenti e la pancetta finale
            cicli_rimasti = r - cicli
            pancetta_finale_sp = pancetta_tmp + pancetta_loop * (cicli_rimasti // dimensione_loop)

            idx = cicli_rimasti % dimensione_loop
            pancetta_parziale = 0
            for key, value in states.items():
                if value[1] == idx:
                    pancetta_parziale = value[0]
                    break
            # Restituisci la pancetta finale
            return pancetta_finale_sp + pancetta_parziale

        else:
            states[state] = (pancetta_tmp, cicli)

    return pancetta_tmp


print(funz(r, k, arr))