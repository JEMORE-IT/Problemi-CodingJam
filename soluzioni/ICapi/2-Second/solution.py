def vede(n, k):
    return (k+1)%2**n == 0

if __name__ == "__main__":
    with open("2-Second/input_2.txt") as f: 
        s = f.read()
        s = s.split("\n")
    ss = []
    for line in s:
        l = line.split(" ")
        ll = [int(x) for x in l]
        ss.append(ll)
    s = ss
    casi_in_cui_vede = 0
    for caso in s:
        if vede(caso[0], caso[1]):
            casi_in_cui_vede += 1
    print(f"Final Answer: {casi_in_cui_vede}")