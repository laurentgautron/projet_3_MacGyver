#! /usr/bin/env python3
# coding: utf-8

class Macgyver:   
    def __init__(self):
        self.x = 1
        self.y = 13
        
    def move(self,choice):
        if choice == 'z':
            return self.x = self.x - 1
        elif choice == 'd':
            return self.y = self.y + 1
        elif choice == 'q':
            return self.y = self.y - 1
        else:
            return self.x = self.x + 1
        
    def bagcontents(self,it):
        if it == 'B':
            return 'Blowpipe'
        elif it == 'S':
            return 'Syringe'
        else:
            return 'poison'