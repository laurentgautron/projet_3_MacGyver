import pygame
from pygame.locals import *
import sys

class Macgyver:
    """ we move Macgyver starting from last position ( lastx, lasty) and change it  according to the player's choice: z(up), d(right), q(left), s(down)
        bagcontents return item's name when player is on an item """

    def __init__(self): # initialze MacGyver's bag with 0 items
        with open('bagcontents.txt', 'w') as init_bag:
            init_bag.write("you've got already in your bag:")

    def move(self,lastx,lasty): # change last position according to Keyboard key
        self.x = lastx
        self.y = lasty
        pygame.event.set_allowed(pygame.MOUSEMOTION)
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
        elif event.type == QUIT: # can quit before finish the game
            pygame.quit()
            sys.exit()
        return self.x,self.y
                            
    def bagcontents(self,it):
        if it == 'B':
            return 'Blowpipe'
        elif it == 'S':
            return 'Syringe'
        else:
            return 'Poison'

    def add_contents(self,item_piece): # write item's name in bagcontents.txt
        with open('bagcontents.txt', 'a') as item_fich:
            item_fich.write("\n"+item_piece)
            
