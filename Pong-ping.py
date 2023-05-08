from pygame import *



font.init()
font2 = font.SysFont('Arial', 36)

win = font2.render('YOU WIN', True, (255, 255, 10))
lose = font2.render('YOU LOSE', True, (180, 0, 0))

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
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 10:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 10:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        if self.rect.y < 10:
            self.speed = self.speed * -1
        if self.rect.y > win_width - 10:
            self.speed = self.speed * -1
        


win_width = 700
win_height = 500
display.set_caption('Pong-ping')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

player_l = Player(img_player, 20, 250, 20, 80, 5)

player_r = Player(img_player, 660, 250, 20, 80, 5)





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
        
        display.update()

    time.delay(60)








    


    


































