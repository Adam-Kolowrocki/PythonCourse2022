# Wyświetl 3 losowe cytaty
import random
from random import choice
with open('cytaty.txt') as file:
    cytaty = file.readlines()
    cytaty_3 = []
    while len(cytaty_3) < 3:
        cytaty_3.append(random.choice(cytaty))
    print(f' Trzy cytaty na dziś to : ''\n')
    for cyt in range(0, len(cytaty_3)):
        print(f'{cytaty_3[cyt]}')
