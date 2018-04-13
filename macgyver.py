""" game of Labyrinth with MacGyver: try to help MacGyver to escape from labyrinth """

#! /usr/bin/env python3
# coding: utf-8

import json

####################################################################################################################################
# calss Labyrinth to initiate labyrinth, Macgyver to initiate macgyver's position and move, an Items to dispose items randomly     #
####################################################################################################################################
class Labyrinth:
    
    def display_lab(self,lab,macgyver_newline,macgyver_newcolumn,tmp_line,tmp_column):
        self.wall = 'False'
        self.guardian = "no"
        if lab[macgyver_newline][macgyver_newcolumn] == "G":
            self.guardian = "yes"           
        if lab[macgyver_newline][macgyver_newcolumn] in ["B","S","P","G"] or lab[macgyver_newline][macgyver_newcolumn] == " " or (macgyver_newline == 13 and macgyver_newcolumn == 1):
            lab[tmp_line][tmp_column] = " "            
            lab[macgyver_newline][macgyver_newcolumn] = "M"
            for lines in lab:
                for columns in lines:
                    print(columns,end='')
                print()
        else:    
            print("there is a wall, you can't move in this direction")
            self.wall = 'True'
        
    
class Macgyver:
    
    # initial position for macgyver
    INITIAL_LINE = 13
    INITIAL_COLUMN = 1
    
    def mac_move(self,moving): # to move macgyver
        if moving == 'z':
            self.line = -1
            self.column = 0
        elif moving == 'd':
            self.line = 0
            self.column = 1
        elif moving == 'q':
            self.line = 0
            self.column = -1
        else:
            self.line = 1
            self.column = 0
        print("lines and columns of movement :",self.line,self.column) # check new indices position
        
        
    def macgyver_bag(self,ind,bag):  # to fill macgyver's bag
            if ind == "B":
                self.object_name = "blowpipe"
            elif ind == "P":
                self.object_name = "poison"
            else:
                self.object_name = "syringe"
            print("you've picked up the %s" %(self.object_name))
            print("you have %d items in your bag" %(len(bag)+1))
            if len(bag)+1 == 3:
                print("you own all the item to asleep the guardian, go to the exit !!")
            else:
                sp = '' if len(bag) == 1 else 's'
                print(f"you own only {len(bag)+1} item{sp}, you still need {3-(len(bag)+1)} item{sp}")
                        
        
class Items:  # to deposit items randomly except the guardian
    
    def __init__(self): 
        self.guardian_line = 2
        self.guardian_column = 15
        #self.syringe_line = 
        #self.syringe_column = 
        #self.poison_line = 
        #self.poison_column = 
        #self.blowpipe_line = 
        #self.blowpipe_column = 

    
#########
# rules #
#########

def rules():
    print('This is a Maze Game :')
    print("you must help MacGyver to exit the Labyrinth")
    print("you can move him with the keyboard keys")
    print("Macgyver have to bring together all the items before to present onself to the Gardien:")
    print(" P is the Poison")
    print(" D is the Dart")
    print(" B is the blowpipe")
    print(" G is the Guardian")
    print("goog luck !!")
    
########    
# menu #
########

def menu():
    print("move MacGyver : (M)")
    print("to the top   : type 'z'")
    print("to the right. : type 'd'")
    print("to the left : type 'q'")
    print("to the down  : type 's'")
    print()
    choice = input("choisissez un déplacement: ")
    if choice not in ['z','d','q','s']:
        print("this reply is not in the list, pay attention")
        menu()
    return choice
        
############################### 
# main programm in a function #
###############################

def main():
    macgyver = Macgyver()
    labyrinth = Labyrinth()  
    item = Items()
    bag = []
    rules()
    conditions =''
    tmp_line = macgyver.INITIAL_LINE
    tmp_column = macgyver.INITIAL_COLUMN
    print("MacGyver is located in: line",tmp_line,", column",tmp_column)
    with open("labyrinth.json", 'r') as fichlab:
        lab = json.load(fichlab)
    labyrinth.display_lab(lab,macgyver.INITIAL_LINE,macgyver.INITIAL_COLUMN,0,0) # display labyrinth
    while  not (len(bag) == 3 and labyrinth.guardian == "yes"):  # good conditions
        if len(bag) < 3 and labyrinth.guardian == "yes":  #wrong conditions
            print("you've losed: you don't have all items to asleep the guardian")
            conditions = 'wrong'
            break
        else:
            moving = menu()
            macgyver.mac_move(moving)   # make Macgyver move
            macgyver_newline = tmp_line + macgyver.line        # edit indices
            macgyver_newcolumn = tmp_column + macgyver.column  # for new position
            print("MacGyver's position : ",macgyver_newline,macgyver_newcolumn)
            #print(lab[macgyver_newline][macgyver_newcolumn])
            if lab[macgyver_newline][macgyver_newcolumn] in ["B","S","P"]:
                macgyver.macgyver_bag(lab[macgyver_newline][macgyver_newcolumn],bag)
                #print(macgyver.object_name)
                bag.append(macgyver.object_name)
                print("your bag : ",bag)
            labyrinth.display_lab(lab,macgyver_newline,macgyver_newcolumn,tmp_line,tmp_column)
            print()
            if labyrinth.wall == 'True':  # check wall or space
                continue
            else:
                tmp_line = macgyver_newline
                tmp_column = macgyver_newcolumn
    if conditions == 'wrong':
        pass          
    else:
        print(" you win !!!!!")
        
if __name__ == "__main__":
    main()  
   
