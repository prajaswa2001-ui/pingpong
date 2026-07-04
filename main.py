from pygame import *

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("ping pong Game")
background = (120, 255, 50)
window.fill(background)

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) 
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

rackek1 = Player("racket.png", 30,200,4,50,150)
rackek2 = Player("racket.png", 520,200,4,50,150)
ball = GameSprite("tennis.png",200,200,4,50,50)
game = True
fps = 60
clock = time.Clock()
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill(background)
    rackek1.reset()
    rackek2.reset()
    ball.reset()

    rackek1.update_1()
    rackek2.update_2()

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    #if ball touch wall
    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= -1

    # if ball touch racket
    if sprite.collide_rect(rackek1, ball) or sprite.collide_rect(rackek2, ball):
        speed_x *= -1
        speed_y *= -1
    display.update()
    clock.tick(fps)
