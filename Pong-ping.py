from pygame import *



font.init()
font2 = font.SysFont('Arial', 36)

lose_r = font2.render('Player 1 lose', True, (180, 0, 0))
lose_l = font2.render('Player 2 lose', True, (180, 0, 0))

img_back = 'Fon.jpg'
img_Ball = 'Ball.png'
img_player = 'Player.jpg'


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x
        global speed_y
        if self.rect.y < 10 or self.rect.y > win_height - 50:
            speed_y = speed_y * -1
        if sprite.collide_rect(Ball, player_l) or sprite.collide_rect(Ball, player_r):
            speed_x = speed_x * -1
        self.rect.y += speed_y
        self.rect.x -= speed_x



win_width = 700
win_height = 500
display.set_caption('Pong-ping')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

player_l = Player(img_player, 40, 250, 20, 100, 15)
player_r = Player(img_player, 640, 250, 20, 100, 15)
Ball = Ball(img_Ball, 250, 350, 70, 50, 10)

speed_y = 10
speed_x = 10


finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False




    if not finish:
        window.blit(background,(0, 0))
        player_l.reset()
        player_l.update_l()
        player_r.reset()
        player_r.update_r()
        Ball.reset()
        Ball.update()

        if Ball.rect.x < -10:
            finish = True
            window.blit(lose_r, (250, 240))
        if Ball.rect.x > 645:
            finish = True
            window.blit(lose_l, (250, 240))
       








        display.update()

    time.delay(60)








    


    


































