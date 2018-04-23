""" game of Labyrinth with MacGyver: try to help MacGyver to escape from labyrinth """

#! /usr/bin/env python3
# coding: utf-8

from textdescription import Textdescription
from labyrinth import Labyrinth
from macgyver import Macgyver
from test import Test

class MacgyverMain:
    """ two function in this class : the init function to define instances, initialize and show position of Macgyver, Guardianand items
        in thr labyrinth. The second function is used to play """
    def __init__(self):
        # instances and variables we need to play
        self.testbox = Test()
        self.text = Textdescription()
        self.text.rules()    # write rules
        self.mcgyver = Macgyver()
        self.labyrinth = Labyrinth('labyrinth.json')    # init labyrinth in lab with items randomly
        self.x, self.y = self.labyrinth.found('M') # found Macgyver
        self.guardian_x,self.guardian_y = self.labyrinth.found('G')
        self.last_x, self.last_y = self.x, self.y
        print("MacGyver is in line %d and column %d" %(self.x,self.y))# show MacGyver's position
        print("guardian is in line %d and column %d" %(self.guardian_x,self.guardian_y))
        self.bag = []  # init MacGyver's bag
        self.labyrinth.display_lab(self.x,self.y,self.last_x,self.last_y)

    def play(self):
        while (self.x,self.y) != (self.guardian_x,self.guardian_y):  # repeat while position is not guardian's position
            choice = self.text.menu()   # display menu to move MacGyver and choose a new position
            self.x,self.y = self.mcgyver.move(choice,self.last_x,self.last_y)  # read new position for MacGyver
            if self.testbox.there_is_a_wall(self.labyrinth.lab,self.x,self.y):   # check if there is not a wall
                print("you can't move: there is a wall in this direction")
                print("try again")
                print ('toujours en :', self.last_x,self.last_y)
                continue
            elif self.testbox.there_is_an_item(self.labyrinth.lab,self.x,self.y):   # check if there is not an item
                it = self.labyrinth.lab[self.x][self.y]
                self.bag.append(self.mcgyver.bagcontents(it))   # fill the bag
                print("bag contents: ", self.bag)   
            self.labyrinth.display_lab(self.x,self.y,self.last_x,self.last_y)
            self.last_x = self.x   # stock MacGyver last position
            self.last_y = self.y
        if len(self.bag) != 3:   # check if there is three items in bag
            print("you loose: you dont own all the items to asleep the guardian")
        else:
            print("good work, you won")
            
if __name__ == '__main__':
    main = MacgyverMain()
    main.play()