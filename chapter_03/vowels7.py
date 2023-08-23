vowels = set("aeiou")
word = input("Podaj słowo, w którym należy wyszukać samogłoski: ")

vowel = vowels.intersection(set(word))

for i in sorted(vowel):
    print(i)
