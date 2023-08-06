from datetime import datetime
from random import randint
from time import sleep

odds = []
for i in range(1,60,2):
    odds.append(i)
    
for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print('Ta minuta wydaje się dość nieprzysta.')
    else:
        print('Minuta parzysta.')

    wait_time = randint(1,60)
    sleep(wait_time)
