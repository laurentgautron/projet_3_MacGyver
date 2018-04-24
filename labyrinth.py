""" init labyrinth and display labyrinth """

#! /usr/bin/env python3
# coding: utf-8

import json
import random
import os
import pygame
from macpygame import Macpygame
from pygame.locals import *

class Labyrinth:

    """   init function open labyrinth fich, display labyrinth and choose randomly location for items 
    labyrinth is displat-yed wthin function display _lab, and function found look for persons(choose in the main) in the labyrinth  """

    def __init__(self, map_lab): # open the fich lab and create labyrinth with list_items
        with open(map_lab, 'r') as labfich:
            try:
                self.lab = json.load(labfich)
            except OSError:
                print('cannot open file')
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
        perso_x = 0
        perso_y = 0
        mcpygame.ecran.blit(mcpygame.mur,(perso_x,perso_y))
        pygame.display.flip()
        continuer = True
        for indices, values in enumerate(self.lab):
            for ind, val in enumerate(values):
                perso_x = ind * 40
                perso_y = indices * 40
                if val == '*':
                    mcpygame.ecran.blit(mcpygame.mur,(perso_x,perso_y))
                if val == 'M':
                    mcpygame.ecran.blit(mcpygame.joueurmac,(perso_x,perso_y))
                if val == 'G':
                    mcpygame.ecran.blit(mcpygame.guard,(perso_x,perso_y))
                if val == 'B':
                    mcpygame.ecran.blit(mcpygame.blowpipe,(perso_x,perso_y))
                if val == 'S':
                    mcpygame.ecran.blit(mcpygame.syringe,(perso_x,perso_y))
                if val == 'P':
                    mcpygame.ecran.blit(mcpygame.poison,(perso_x,perso_y))
        pygame.display.flip()
        while continuer:
            for events in pygame.event.get():
                if events.type == QUIT:
                    continuer = False
            
    def found(self,person):
        for i, line in enumerate(self.lab):
            for j, column in enumerate(line):
                if column == person:
                    self.pos_x = i
                    self.pos_y = j
        return self.pos_x,self.pos_y