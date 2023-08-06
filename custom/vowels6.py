vowels = ('a', 'e', 'i', 'o', 'u')
word = input("Podaj słowo, w którym należy wyszukać samogłoski: ")

found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    if v > 1:
        print(k, "znaleziono", v, 'razy.')
    else:
        print(k, "znaleziono", v, 'raz.')
    