import sys

import pygame
from pygame.locals import *


class Macgyver:
    """ concern macgyver/ player's actions

        methods  move: player's position
                 bagcontents: to fill his bag
                 add_contents: record items in text file
    """
    
    def __init__(self):
        """ create a text file for bag contents """

        with open('bagcontents.txt', 'w') as init_bag:
            init_bag.write("you've got already in your bag:")

    def move(self,lastx,lasty,event):
        """ change macgyver's position 

            agr lastx, lasty : integers, macgyver's position
                event : event from player to make choice for movement, KEYDOWN

            return x, y : integers, new position for macgyver
        """ 

        self.x = lastx
        self.y = lasty
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
        """ check what is the item picked up and return is name
            
            arg it : string, letter for the item

            return: string
        """

        if it == 'B':
            return 'Blowpipe'
        elif it == 'S':
            return 'Syringe'
        else:
            return 'Poison'

    def add_contents(self,item_piece):
        """ add items in bag contents file 

            arg item_piece : string, name for the item wtrited in bagcontents.txt
        """

        with open('bagcontents.txt', 'a') as item_fich:
            item_fich.write("\n"+item_piece)
            
