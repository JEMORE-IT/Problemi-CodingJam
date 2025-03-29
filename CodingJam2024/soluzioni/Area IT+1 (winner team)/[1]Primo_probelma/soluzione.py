

dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
punteggi = {')': 7, ']': 42, '}': 1337, '>': 64880}
list = []
punteggio = 0
with open("input.txt") as f:
    for i, l in enumerate(f.readlines()):
        list.append(l.replace('\n', ''))
stack = []
for i, l in enumerate(list):
    for j, c in enumerate(l):
        if c in dict.keys():
            stack.append(c)
        else:
            tmp = stack.pop()
            if c != dict[tmp]:
                print(f" linea {i} corrotta: {c}")
                punteggio += punteggi[c]
                break
print(f"punteggio finale: {punteggio}")
