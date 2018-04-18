""" Chang MacGyver's position and bagcontents """

#! /usr/bin/env python3
# coding: utf-8

class Macgyver:   
    def __init__(self):
        self.x = 13
        self.y = 1
        
    def move(self,choice):
        if choice == 'z':
            self.x -= 1
        elif choice == 'd':
            self.y += 1
        elif choice == 'q':
            self.y -= 1
        else:
            self.x += 1
        return self.x,self.y
                    
    def bagcontents(self,it):
        if it == 'B':
            return 'Blowpipe'
        elif it == 'S':
            return 'Syringe'
        else:
            return 'Poison'