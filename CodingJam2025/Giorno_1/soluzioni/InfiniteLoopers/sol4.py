def is_vowel(c):
    return c in ["a", "e", "i", "o", "u"]


with open("../../problema_4/input.txt") as f:
    word = f.read()

word = word.strip()

vowels = 0
consonants = 0
length = len(word)
for idx, c in enumerate(word.lower()):
    if is_vowel(c):
        vowels += length - idx
    else:
        consonants += length - idx

vowels_list = [int(x) for x in str(vowels)]
consonants_list = [int(x) for x in str(consonants)]

print(sum(vowels_list) + sum(consonants_list))
