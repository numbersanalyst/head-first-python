from datetime import datetime
import random
import time

odds = []
for i in range(1,60,2):
    odds.append(i)
    
for i in range(5):
    right_this_minute = datetime.today().minute
    wait_time = random.randint(1,60)
    if right_this_minute in odds:
        print("Minuta nieparzysta")
    else:
        print("Minuta parzysta")
    time.sleep(wait_time)