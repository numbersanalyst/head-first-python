pharse = "Podaj jajko!"
plist = list(pharse)
print(pharse)
print(plist)

rlist = ["P", "a", "j"]

for remove_letter in rlist:
    plist.remove(remove_letter)

for triple in range(3):
    plist.pop()


new_pharse = ''.join(plist)
# W tym wierszu lista z powrotem przetwarzanma jest do postaci łańcucha znakowego.

print(plist)
print(new_pharse)
