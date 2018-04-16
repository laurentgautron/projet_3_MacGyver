#! /usr/bin/env python3
# coding: utf-8

import json

class Labyrinth:   
    def __init__(self, labyrinth.json):
        with open('labyrinth.json', 'r') as labfich:
            self.lab = json.load(labfich)
        self.lab[1][14] = 'G'
        
    def display_lab(self,x,y,lastx,lasty):
        self.lab[x][y] = 'M'
        self.lab[lastx][lasty] = ' '
        for lines in self.lab:
            for columns in lines:
                print(columns, end='')
            print()