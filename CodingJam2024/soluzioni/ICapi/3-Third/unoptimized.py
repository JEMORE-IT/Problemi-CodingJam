import time
def index_of_split(P, k):   #Returns up to which number can fit(included)
    s = 0
    for i, val in enumerate(P):
        s += val
        if s > k:
            return i - 1

if __name__ == "__main__":
    r = 1000000000  #Numero di giri
    k = 100         #Quanti ne stanno
    #r = 4
    #k = 6
    P_test = [1, 4, 2, 1]
    P = [2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 2, 2, 7, 4, 2, 3, 2, 8, 12, 2, 2, 2, 7, 4, 2, 3, 2, 8, 12, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2]
    #P = P_test
    t = 0
    grams_of_pancetta = 0
    for i in range(r):
        can_fit = P[:index_of_split(P,k)+1]
        cannot_fit = P[index_of_split(P,k)+1:]
        #print(f"Fit:{can_fit}, Cannot:{cannot_fit}")
        grams_of_pancetta += sum(can_fit)
        P = cannot_fit + can_fit
        if i % 1000000 == 0:
            print("ciclo")
            print("Delta: ")
            print((time.time() - t))
            t = time.time()
    print(grams_of_pancetta)

# 930