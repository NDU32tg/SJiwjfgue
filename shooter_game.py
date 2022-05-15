#Создай собственный Шутер!

#Создай собственный Шутер!

from pygame import *
from random import randint
from time import time as timer
mixer.init()
mixer.music.load('123.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

font.init()
font2 = font.SysFont('Arial', 36)
win = font2.render('YOU PROIGRAL', True, (255, 255, 255))
lose = font2.render('YOU VIGRAL', True, (180, 0, 0))

imb_back = 'galaxy.jpg'
img_hero = 'rocket.png'
img_bullet = 'gey.png'
img_asteroid = 'asteroid.png'
img_enemy = 'pngegg.png'

score = 0
lost = 0
max_lost = 3
goal = 10


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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 74:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_height - 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

win_width = 700
win_height = 500
display.set_caption('Shooter')
window = display.set_mode((win_width,win_height))
background = transform.scale(image.load(imb_back), (win_width,win_height))
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 6))
    monsters.add(monster)

asteroids = sprite.Group()
for i in range(1, 3):
    asteroid = Enemy(img_asteroid, randint(80, win_width - 80), -40, 80, 50, randint(1, 2))
    asteroids.add(asteroid)


bullets = sprite.Group()

finish = False
run = True
rel_time = False 
num_fire = 0
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and rel_time == False:
                    num_fire = num_fire + 1
                
                    fire_sound.play()
                    ship.fire()
                if num_fire >= 5 and rel_time == False:
                    last_time = timer()
                    rel_time = True

    if not finish:
        window.blit(background,(0,0))

        text = font2.render('schet: ' +str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render('propyscheno: ' +str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))


        ship.update()
        monsters.update()
        bullets.update()
        asteroids.update()


        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        asteroids.draw(window)
        collides = sprite.groupcollide (monsters, bullets, True, True)
        if rel_time == True:
           now_time = timer() #считываем время
       
           if now_time - last_time < 3: #пока не прошло 3 секунды выводим информацию о перезарядке
               reload = font2.render('Wait, reload...', 1, (150, 0, 0))
               window.blit(reload, (260, 460))
           else:
               num_fire = 0   #обнуляем счётчик пуль
               rel_time = False #сбрасываем флаг перезарядки
        for c in collides:
            score = score +1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 6))
            monsters.add(monster)
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))
        if lost == max_lost:
            finish = True
            window.blit(lose,(200,200))
        if sprite.spritecollide(ship, monsters, False):
            finish = True
            window.blit(lose,(200,200))
        display.update()
    else:
       finish = False
       score = 0
       lost = 0
       for b in bullets:
           b.kill()
       for m in monsters:
           m.kill()
 
       time.delay(3000)
       for i in range(1, 6):
           monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
           monsters.add(monster)      
time.delay(50 )        
    