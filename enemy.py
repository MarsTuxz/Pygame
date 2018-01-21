import pygame

import sys
from random import *

from pygame.locals import *


##class Enemy(pygame.sprite.Sprite):
##     #  size-- 表示飞机的尺寸
##     def __init__(self,image,bg_size):
##          pygame.sprite.Sprite.__init__(self);
##          self.image = pygame.image.load(image).convert()
##          self.rect = self.image.get_rect();
##          self.width,self.height = bg_size[0],bg_size[1];
          



# 小的敌机

class SmallEnemy(pygame.sprite.Sprite):
     # 飞机的能量
     # 每当敌机被击中的时候将senergy减1
     energy = 10;

     
     
     def __init__(self,bg_size):
          pygame.sprite.Sprite.__init__(self);
          self.image = pygame.image.load('picture/enemy_1.png').convert()

          
          self.bomb_image = [];
          self.bomb_image.extend([ pygame.image.load('picture/bomb_plane1.png').convert()\
                                   ,pygame.image.load('picture/bomb2_plane1.png').convert()])

           
          #飞机是否存活
          self.active = True;
          
          self.rect = self.image.get_rect();
          self.width,self.height = bg_size[0],bg_size[1];
          self.rect.left,self.rect.top = (randint(0,self.width-self.rect.width),\
                                         randint(-30,10))
          self.speed = 1

          self.mask = pygame.mask.from_surface(self.image);

          self.energy = SmallEnemy.energy


     def relive(self):
          self.energy = SmallEnemy.energy
          self.active = True;
          self.rect.left,self.rect.top = (randint(0,self.width-self.rect.width),\
                                         randint(-50,10))

     #飞机的移动
     def move(self):
          if self.rect.top < self.height:
               self.rect.top += self.speed;
          else:
               self.relive();
     
class MiddleEnemy(pygame.sprite.Sprite):
     def __init__(self,bg_size):
          pygame.sprite.Sprite.__init__(self);
          self.image = pygame.image.load('picture/enemy_2.png').convert()

          
          self.bomb_image = [];
          self.bomb_image.extend([ pygame.image.load('picture/bomb_plane2.png').convert()\
                                   ,pygame.image.load('picture/bomb2_plane2.png').convert()])

          #飞机是否存活
          self.active = True;
          
          self.rect = self.image.get_rect();
          self.width,self.height = bg_size[0],bg_size[1];
          
          self.rect.left,self.rect.top = (randint(0,self.width-self.rect.width),\
                                         randint(-60,10))
          self.speed = 2
          self.mask = pygame.mask.from_surface(self.image) 
     #飞机的移动
     def move(self):
          if self.rect.top < self.height:
               self.rect.top += self.speed;
          else:
               self.relive();
     def relive(self):
          self.active = True;
          self.rect.left,self.rect.top = (randint(0,self.width-self.rect.width),\
                                         randint(-60,10))
                                               
class BigEnemy(pygame.sprite.Sprite):
     def __init__(self,bg_size):
          pygame.sprite.Sprite.__init__(self);
          self.image1 = pygame.image.load('picture/enemy_3.png').convert()
          self.image2 = pygame.image.load("picture/enemy_3_1.png").convert()

          self.bomb_image = [];
          self.bomb_image.extend([ pygame.image.load('picture/bomb3_plane1.png').convert()\
                                   ,pygame.image.load('picture/bomb3_plane2.png').convert()])

          #飞机是否存活
          self.active = True;
          self.rect = self.image1.get_rect();
          self.width,self.height = bg_size[0],bg_size[1];
          self.rect.left,self.rect.top = (randint(0,self.width-self.rect.width),\
                                         randint(-100,-60))
          self.speed = 1
          self.mask = pygame.mask.from_surface(self.image1) 
     #飞机的移动
     def move(self):
          if self.rect.top < self.height:
               self.rect.top += self.speed;
          else:
               self.relive();
     def relive(self):
          ##print("ggg")
          self.active = True;
##          self.rect.left,self.rect.top = (randint(0,self.width-self.rect.width),\
##                                         randint(-100,-60))
