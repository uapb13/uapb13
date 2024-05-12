import pygame as pg
import random
pg.init()
screen = pg.display.set_mode([500, 500])
screen.fill([255, 255, 255])
print(random.random() * 7)
#plim = 'player.png'


class Player(pg.sprite.Sprite):
    def __init__(self, name):
        super(Player, self).__init__()
        self.surf = pg.Surface((75, 25))
        self.surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect()

    def move(self):
        pass


class Wall:
    def __init__(self, width, height, x, y, image):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__image = image


player = Player('idkwhattoput')
pg.display.flip()
r = True
while r:
    screen.blit(player.surf, player.rect)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            r = False

    pk = pg.key.get_pressed()
    pg.display.flip()

pg.quit()
