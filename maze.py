from pygame import * 

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,55))
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
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
class Enemy(GameSprite):
    direction = "left"
    def update (self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
 
        # картинка стены - прямоугольник нужных размеров и цвета
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
 
        # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
 
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0    ))

w1 = Wall(154, 205, 50, 100, 20 , 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)
    

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
player = Player('hero2.png', 5, win_height - 80, 4)
monster = Enemy('hero.png',win_width - 80, 280,2)
final = GameSprite('treasure.png',win_width - 120, win_height - 80, 0)
game = True 
finish = False
clock = time.Clock()
FPS = 60


mixer.init()
mixer.music.load('Shadowraze-Astral-Step.ogg')
mixer.music.play()
kick = mixer.Sound('Bount_death_05_ru.mp3.ogg')
('Nev_arc_lose_03_ru.mp3_1.ogg') or ('Bount_death_05_ru.mp3.ogg')
money = mixer.Sound('zvuk--donata-.ogg')
duel = mixer.Sound('Legion_Commander_Press_the_Attack.mp3.ogg')
while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
   if finish != True:
  
       window.blit(background,(0, 0))
       player.reset()
       monster.reset()
       w1.draw_wall()
       w2.draw_wall()
       w3.draw_wall()
       final.reset()
       if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()
       if sprite.collide_rect(player, monster):
            finish = True
            window.blit(lose, (200, 200))
            duel.play()
       if sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2)or sprite.collide_rect(player, w3):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
   player.update()
   monster.update()
   display.update()
   final.reset()
   final.update()
   clock.tick(FPS)
   w1.draw_wall()