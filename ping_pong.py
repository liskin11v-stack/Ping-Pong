from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image_object, speed_object_x, speed_object_y, xc, yc, w, h):
        self.image = transform.scale(image.load(image_object), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = xc
        self.rect.y = yc
        self.speed_x = speed_object_x
        self.speed_y = speed_object_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updateL(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys[K_s] and self.rect.y < 600 - 200:
            self.rect.y += self.speed_y
    
    def updateR(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys[K_DOWN] and self.rect.y < 600 - 200:
            self.rect.y += self.speed_y

window = display.set_mode((600, 600))
clock = time.Clock()

player_L = Player("left.png", 0, 5, 5, 200, 40, 200)
player_R = Player("right.png", 0, 5, 555, 200, 40, 200)

game = True
while game:
    window.fill((150, 150, 250))
    player_L.reset()
    player_R.reset()
    player_L.updateL()
    player_R.updateR()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(50)
