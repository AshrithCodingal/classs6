import pygame
import random

screen_width= 500
screen_height = 400
movement_speed=5
font_size=72

pygame.init()

baground_image = pygame.transform.scale(pygame.image.load("bg.jpg"),(screen_width,screen_height))

font = pygame.font.SysFont("Times New Roman",font_size)


class Sprite(pygame.sprite.Sprite):
    
    def __init__(self,color,width,height):
     super().__init__()
     self.image = pygame.Surface([width,height])
     self.image.fill(pygame.Color("dogerblue"))
     pygame.draw.rect(self.image,color,pygame.Rect(0,0, width,height))
     self.rect = self.image.get_rect()


    def move(self,x_change,y_change):
     self.rect.x = max(min(self.rect.x+x_change,screen_width-self.rect.width),0)
     self.rect.y = max(min(self.rect.y+y_change,screen_height-self.rect.height),0)

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite collosion")

all_sprite =pygame.sprite.Group()

sprite1 = Sprite(pygame.Color('red'),20,30)
sprite1.rect.x = random.randint(0,screen_width - sprite1.rect.width)
sprite1.rect.y = random.randint(0,screen_height - sprite1.rect.height)
all_sprite.add(sprite1)
sprite2 = Sprite(pygame.Color(''),20,30)
sprite2.rect.x = random.randint(0,screen_width - sprite1.rect.width)
sprite2.rect.y = random.randint(0,screen_height - sprite1.rect.height)
all_sprite.add(sprite2)







