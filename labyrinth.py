""" init labyrinth and display labyrinth """

#! /usr/bin/env python3
# coding: utf-8

import json
import random
import os
import pygame

class Labyrinth:
    """   init function open labyrinth fich, display labyrinth and choose randomly location for items 
    labyrinth is displat-yed wthin function display _lab, and function found look for persons(choose in the main) in the labyrinth  """
    def __init__(self, map_lab):
        with open(map_lab, 'r') as labfich:
            try:
                self.lab = json.load(labfich)
            except OSError:
                print('cannot open file')
            else:
                list_items = ['B','P','S']
                while list_items != []: 
                    # take an item in the list_items ( items to locate) , locate it randomly and delete it inthe list_items
                    column = random.randint(0,14)
                    line = random.randint(0,14)
                    if self.lab[column][line] != '*':
                        self.lab[column][line] = list_items[0]
                        del list_items[0]
        
    def display_lab(self,x,y,last_x,last_y):
        self.lab[x][y] = 'M'
        if (x,y) != (last_x,last_y):
            self.lab[last_x][last_y] = ' '
        for line in self.lab:
            for column in line:
                print(column, end='')
            print()
            
    def found(self,person):
        for i, line in enumerate(self.lab):
            for j, column in enumerate(line):
                if column == person:
                    self.pos_x = i
                    self.pos_y = j
        return self.pos_x,self.pos_y