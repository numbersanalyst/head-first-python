import datetime

today = datetime.date.today().day
condition = 'Dobrze jest...! 😀'


if today == 'Sobota':
    print('Impreza!...')
elif today == 'Niedziela':
    if condition == 'Ból głowy':
        print('Tabletka, później odpoczynek.')
    else:
        print('Odpoczynek.')

else:
    print('Praca, praca...!')


for i in [1,2,3]:
    print(i)
for ch in "Hej, jak się masz?":
    print(ch)
for num in range(5):
    print('Python jest okej! 🧐')
