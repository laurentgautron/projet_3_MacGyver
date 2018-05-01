import pygame
from pygame.locals import *
import sys

class Macgyver:
    """ """
    
    def __init__(self):
        """ """
        with open('bagcontents.txt', 'w') as init_bag:
            init_bag.write("you've got already in your bag:")

    def move(self,lastx,lasty):
        """ """ 
        self.x = lastx
        self.y = lasty
        event = pygame.event.wait()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                    self.x -= 1
            elif event.key == K_RIGHT:
                self.y += 1
            elif event.key == K_LEFT:
                self.y -= 1
            elif event.key == K_DOWN:
                self.x += 1
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
        return self.x,self.y
                            
    def bagcontents(self,it):
        """ """
        if it == 'B':
            return 'Blowpipe'
        elif it == 'S':
            return 'Syringe'
        else:
            return 'Poison'

    def add_contents(self,item_piece):
        """ """
        with open('bagcontents.txt', 'a') as item_fich:
            item_fich.write("\n"+item_piece)
            
