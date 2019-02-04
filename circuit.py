#! python3
# chrono per palestra! circuiti di crossfit

import time
import gi
from playsound import playsound

x=30
while(True):
    try:
        print ("quanti secondi vuoi nel tuo circuito?")
        x=int(input())
        break
    except:
        continue

while(True):
    for i in range(0,x):
        print(x-i-1)
        time.sleep(1)
    playsound('/home/thresorts/Dev/circuit/sound1.wav')
    print('\n\tCAMBIO\n')
