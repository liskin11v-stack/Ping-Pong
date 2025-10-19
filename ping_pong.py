from pygame import *

window = display.set_mode((600, 600))
clock = time.Clock()

game = True
while game:
    window.fill((150, 150, 250))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(50)