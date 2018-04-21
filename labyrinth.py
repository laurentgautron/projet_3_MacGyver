""" init labyrinth and display labyrinth """

#! /usr/bin/env python3
# coding: utf-8

import json
import random
import os
import pygame

class Labyrinth:   
    def __init__(self, map_lab):
        with open(map_lab, 'r') as labfich:
            try:
                self.lab = json.load(labfich)
            except OSError:
                print('cannot open file')
            else:
                notfree = ['*','G','M']
                list_items = ['B','P','S']
                while list_items != []:
                    column = random.randint(0,14)
                    line = random.randint(0,14)
                    print(line, column)
                    if self.lab[column][line] not in notfree:
                        self.lab[column][line] = list_items[0]
                        notfree.append(list_items[0])
                        del list_items[0]
                        print(notfree, list_items)
                        print(self.lab[column][line])
                        print(line, column)
                        print() 
        
    def display_lab(self,x,y,last_x,last_y):
        if (x,y) != (last_x,last_y):
            self.lab[last_x][last_y] = ' '
        for line in self.lab:
            for column in line:
                print(column, end='')
            print()
            
    def found_macgyver(self):
        for i, line in enumerate(self.lab):
            for j, column in enumerate(line):
                if column == 'M':
                    self.macinitpos_x = j
                    self.macinitpos_y = i