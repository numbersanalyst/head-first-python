from datetime import datetime

# 🎠 - zainportowanie submodułu należacego do modułu datetime, pochodzącego z biblioteki standardowej Pythona.
# Biblioteka standardowa Pythona jest bardzo bogata i zawiera mnóstwo kodu wielokrotnego użytku.

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

# Przypisywanie literalnej listy liczb nieparzystych do zmiennej odds. W tym przypadku odds jest listą liczb całkowitych, ale listy w języku Python mogą zawierać dowolne dane jakiegokolwiek typu.
# Listy umieszcza się w nawiasach kwadratowych, zaczyna się ona od ([) - a kończy na (])
# Python oferuje wszystkie standardowe operatory, w tym <, >, <=, >=, ==, !=, jak również operator przypisania =.

right_this_minute = datetime.today().minute

# Przypisanie wyniku wywołania metody do zmiennej, noszącą nazwę right_this_minute.
# Wywoływana jest metoda o nazwie today wchodząca w skład submodułu datetime, który sam z kolei jest częścią składową modułu datetime.
# To, że funkcja today jest wywoływana, można stwierdzić dzięki występowaniu po jej nazwie standardowych nawiasów ()
# Utwórz obiekt reprezentujący bieżacy czas, a następnie wyodrębnij wartość atrybutu minut przed przypisaniem jej do zmiennej

if right_this_minute in odds:
    print('Ta minuta wydaje się dość nieprzysta.')
else:
    print('Minuta parzysta.')

# Fragment kodu wykorzystujący operator in, dzięki któremu można sprawdzić - czy wartość przechowywana w zmeinnej right_this_minute znajduje się na liście odds.
# Operator in zwraca wartość True lub False, którą my później wykorzystujemy w odpowiedni sposób - w zależności od otrzymanej wartości.
# Znajdują się tutaj dwa bloki/zestawy, które zawierają wywołanie funkcji print - można je łatwo zauważyć, ponieważ są odpowiednio wcięte.
