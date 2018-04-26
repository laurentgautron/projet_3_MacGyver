#! /usr/bin/env python3
# coding: utf-8

import json
import random
import os
from macpygame import Macpygame


class Labyrinth:

    """   init function open labyrinth fich, display labyrinth ( write 'M' at MacGyver's position and ' 'at MacGyver's last place) and choose randomly location for items 
    labyrinth is displayed wthin function display _lab, and function found look for persons(choose in the main) in the labyrinth  """

    def __init__(self, map_lab): # open the fich lab and create labyrinth with list_items
        with open(map_lab, 'r') as labfich:
            try:
                self.lab = json.load(labfich)
            except OSError:
                print('cannot open file')
                sys.exit()
            else:
                list_items = ['B','P','S']
                while list_items != []:   # take an item in the list_items ( items to locate) , locate it randomly and delete it in the list_items
                    column = random.randint(0,14)
                    line = random.randint(0,14)
                    if self.lab[column][line] == ' ':
                        self.lab[column][line] = list_items[0]
                        del list_items[0]
        
    def display_lab(self,x,y,last_x,last_y): # last position become an empty space and the new position is Mavgyver: 'M'
        mcpygame = Macpygame()
        self.lab[x][y] = 'M'
        if (x,y) != (last_x,last_y):
            self.lab[last_x][last_y] = ' '
        mcpygame.display(self.lab) # then display labyrinth with Pygame
            
    def found(self,person):  # search where are the person in the labyrinth, MacGyver or the Guardian
        for i, line in enumerate(self.lab):
            for j, column in enumerate(line):
                if column == person:
                    self.pos_x = i
                    self.pos_y = j
        return self.pos_x,self.pos_y