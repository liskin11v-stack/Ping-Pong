from pygame import *
font.init()

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

class Ball(GameSprite):
    def update(self, rocketL, rocketR):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if sprite.collide_rect(self, rocketL) or sprite.collide_rect(self, rocketR):
            self.speed_x *= -1
        if self.rect.y < 0 or self.rect.y > 600 - 70:
            self.speed_y *= -1

font = font.Font(None, 35)
lose_L = font.render("Player Left lose", True, (180, 0, 0))
lose_R = font.render("Player Right lose", True, (180, 0, 0))

window = display.set_mode((600, 600))
clock = time.Clock()

player_L = Player("left.png", 0, 5, 5, 200, 40, 200)
player_R = Player("right.png", 0, 5, 555, 200, 40, 200)
ball = Ball("ball.png", 3, 3, 265, 265, 70, 70)

game = True
finish = False
while game:
    if not finish:
        window.fill((150, 150, 250))
        player_L.reset()
        player_R.reset()
        ball.reset()
        player_L.updateL()
        player_R.updateR()
        ball.update(player_L, player_R)
        if ball.rect.x < 0:
            finish = True
            window.blit(lose_L, (200, 200))
        if ball.rect.x > 530:
            finish = True
            window.blit(lose_R, (200, 200))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(50)
