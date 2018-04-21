""" game of Labyrinth with MacGyver: try to help MacGyver to escape from labyrinth """

#! /usr/bin/env python3
# coding: utf-8

from textdescription import Textdescription
from labyrinth import Labyrinth
from macgyver import Macgyver
from test import Test

class MacgyverMain:
    def __init__(self):
        testbox = Test()
        text = Textdescription()
        text.rules()    # write rules
        labyrinth = Labyrinth('labyrinth.json')    # init labyrinth in lab with items randomly
        x, y = labyrinth.found_macgyver.macinitpos_x, labyrinth.found_macgyver.macinitpos_y
        last_x, last_y = x, y
        mcgyver = Macgyver() # init MavGyver's position
        labyrinth.display_lab(x,y,last_x,last_y)
        bag = []  # init MacGyver's bag
        print("MacGyver is in line %d and column %d" %(x,y))# show MacGyver's position
        while (x,y) != (1,14):  # repeat while position is not guardian's position
            choice = text.menu()   # display menu to move MacGyver and choose a new position
            x,y = mcgyver.move(choice)  # read new position for MacGyver
            print(x, y)
            if testbox.there_is_a_wall(labyrinth.lab,x,y):   # check if there is not a wall
                print("you can't move: there is a wall in this direction")
                print("try again")
                mcgyver.x,mcgyver.y = last_x,last_y # don't move
                print ('toujours en :', x,y)     
                continue # try again   
            elif testbox.there_is_an_item(labyrinth.lab,x,y):   # check if there is not an item
                it = labyrinth.lab[x][y]
                bag.append(mcgyver.bagcontents(it))
                print("bag contents: ", bag)   # fill the bag
            labyrinth.display_lab(x,y,last_x,last_y)  # move Macgyver: display labyrinth
            last_x = x   # stock MacGyver last position
            last_y = y

        if len(bag) != 3:   # check if there is three items in bag
            print("you loose: you dont own all the items to asleep the guardian")
        else:
            print("good work, you won")
            
if __name__ == '__main__':
    main = MacgyverMain()