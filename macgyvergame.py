""" game of Labyrinth with MacGyver: try to help MacGyver to escape from labyrinth """

#! /usr/bin/env python3
# coding: utf-8

import textdescription
import labyrinth
import macgyver
import test

class Game:
    def __init__(self):
        last_x = 1
        last_y = 13
        testcase = Test()
        text = Textdescription()
        text.rules()    # write rules
        lab = Labyrinth()    # init labyrinth in lab with items randomly
        macgyver = Macgyver() # init MavGyver's position
        lab.display_lab(macgyver.x,macgyver.y,1,13)
        bag = []  # init MacGyver's bag
        print(f"MacGyver is in line {macgyver.x} and column {macgyver.y}")# show MacGyver's position
        while x != 13 and y != 1:  # repeat while position is not guardian's position
            choice = text.menu()   # display menu to move MacGyver and choose a new position
            x, y = macgyver.move(choice)  # read new position for MacGyver
            if testcase.there_is_a_wall(x,y):   # check if there is not a wall
                print("you can't move: there is a wall in this direction")
                print("try again") 
                x, y = sellast_x, last_y    # don't move 
                continue # try again   
            if testcase.there_is_an_item(x,y):   # check if there is not an item
                it = lab[x][y]
                bag.extend(macgyver.bagcontents(it))
                print("bag contents: ", bag)   # fill the bag
            lab.displa_lab(x,y,last_x,last_y)   # move Macgyver: display labyrinth
            last_x = x   # stock MacGyver last position
            last_y = y

        if len(bag) != 3:   # check if there is three items in bag
            print("you loose: you dont own all the items to asleep the guardian")
        else:
            print("good work, you won")