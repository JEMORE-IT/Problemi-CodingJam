def calc(num):
    sum = 0
    while num > 0:
        floored = num // 10
        sum += num - floored * 10
        num = floored
    return sum

def countsubstr(stri: str) -> int:
    scores = {
        "vowel": 0,
        "consonant": 0,
    }
    
    l = len(stri)
    for idx, c in enumerate(stri.lower()):
        if c in "aeiou":
            scores["vowel"] += l - idx
        else:
            scores["consonant"] += l - idx
    
    print(scores)
    return sum([calc(i) for i in scores.values()]) 
    
with open("input.txt", "r") as f:
    print(countsubstr(f.readline()))
