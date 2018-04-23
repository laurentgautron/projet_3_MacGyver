""" Change MacGyver's position and bagcontents """

#! /usr/bin/env python3
# coding: utf-8

class Macgyver:
    """ we move Macgyver starting from last position ( lastx, lasty) and change it  according to the player's choice: z(up), d(right), q(left), s(down)
        bagcontents return item's name when player is on an item """   
    def move(self,choice,lastx,lasty):
        self.x = lastx
        self.y = lasty
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