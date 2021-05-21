import pygame as pg
from pygame.time import delay
import pygamebg
import random
prozor = pygamebg.open_window(600, 600, "PYGAME")

prozor.fill(pg.Color("white"))
x = 30
y = 0
y2 = 600
for i in range(20):
    pg.draw.line(prozor, pg.Color("black"), (x, y), (x, y2), 1)
    pg.draw.line(prozor, pg.Color("black"), (y, x), (y2, x), 1)
    x += 30

pg.draw.circle(prozor, pg.Color("black"), (300, 300), 20)

walks = []
all_walks = []
pocetak = [(300, 300), (300, 300), (300, 300), (300, 300), (300, 300), (300, 300)]
boje = ["green", "red", "blue", "yellow", "orange", "purple"]

for i in range(8):
    for j in range(len(boje)):
        x_walk = random.randint(0, 1)
        y_walk = random.randint(0, 1)
        walks.append((x_walk, y_walk))
    all_walks.append(walks)
    walks = []

print(all_walks)
for i in range(8):
    for j in range(6):
        boja = boje[j]
        if all_walks[i][j][0] == 1:
            novi_pocetak = (pocetak[j][0]+30, pocetak[j][1])
            pg.draw.line(prozor, pg.Color(boja), pocetak[j], novi_pocetak, 3)
            
        else:
            novi_pocetak = (pocetak[j][0]-30, pocetak[j][1])
            pg.draw.line(prozor, pg.Color(boja), pocetak[j], novi_pocetak, 3)
        pocetak[j] = novi_pocetak
        if all_walks[i][j][1] == 1:
            novi_pocetak = (pocetak[j][0], pocetak[j][1]+30)
            pg.draw.line(prozor, pg.Color(boja), pocetak[j], novi_pocetak, 3)
            
        else:
            novi_pocetak = (pocetak[j][0], pocetak[j][1]-30)
            pg.draw.line(prozor, pg.Color(boja), pocetak[j], novi_pocetak, 3)
        pocetak[j] = novi_pocetak
            
    delay(500)
    pg.display.update()
    if i == 7:
        for _ in range(6):
            pg.draw.circle(prozor, pg.Color(boje[_]), pocetak[_], 10)
    

pygamebg.wait_loop()