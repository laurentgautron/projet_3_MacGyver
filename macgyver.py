""" game of Labyrinth with MacGyver: try to help MacGyver to escape from labyrinth """

#! /usr/bin/env python3
# coding: utf-8

import json

####################################################################################################################################
# calss Labyrinth to initiate labyrinth, Macgyver to initiate macgyver's position and move, an Items to dispose items randomly     #
####################################################################################################################################
class Labyrinth:
    
    def display_lab(self,lab,macgyver_newline,macgyver_newcolumn,tmp_line,tmp_column):
        if lab[macgyver_newline][macgyver_newcolumn] == '*':
            print("vous ne pouvez pas vous déplacer par là: il y a un mur ! essayez encore")
            print()
        else:
            lab[tmp_line][tmp_column] = " "            
            lab[macgyver_newline][macgyver_newcolumn] = "M"
            for lines in lab:
                for columns in lines:
                    print(columns,end='')
                print()
    
class Macgyver:
    
    # initial position for macgyver
    INITIAL_LINE = 13
    INIIAL_COLUMN = 1
    
    def mac_move(self,moving): # to move macgyver
        if moving == 'Z':
            self.line = -1
            self.column = 0
        elif moving == 'D':
            self.line = 0
            self.column = 1
        elif moving == 'Q':
            self.line = 0
            self.column = -1
        else:
            self.line = 1
            self.column = 0
          
        
    def macgyver_bag(self,lab,macgyver_newline,macgyver_newcolumn):  # to fill macgyver's bag
        if lab[macgyver_newline][macgyver_newcolumn] in ['B','S','P']:
            self.objectfound = 'TRUE'
            if lab[macgyver_newline][macgyver_newcolumn] == "B":
                object_name = "blowpipe"
            elif lab[macgyver_newline][macgyver_newcolumn] == "P":
                object_name = "poison"
            else:
                object_name = "syringe"
            self.bag = lab[macgyver_newline][macgyver_newcolumn]
            print("vous avez ramassé un objet the %s" %(object_name))
        else:
            self.objectfound = 'FALSE'
        
        pass
        
class Items:  # to deposit items randomly except the guardian
    
    def __init__(self): # initial psition for the guardian
        self.guardian_line = 2
        self.guardian_column = 15
        #self.syringe_line = 
        #self.syringe_column = 
        #self.poison_line = 
        #self.poison_column = 
        #self.blowpipe_line = 
        #self.blowpipe_column = 
           

############################### 
# main programm in a function #
###############################

def menu():
    print("move MacGyver")
    print("to the top   : type 'Z'")
    print("to the right. : type 'D'")
    print("to the left : type 'Q'")
    print("to the down  : type 'S'")
    print()
    choice = input("choisissez un déplacement: ")
    if choice not in ['Z','D','Q','S']:
        print("this reply is not in the list, pay attention to the uppercase")
        menu()
    return choice
        
def main():
    macgyver = Macgyver()
    labyrinth = Labyrinth()  
    item = Items()
    game = 'go'
    bag = []
    tmp_line = macgyver.INITIAL_LINE
    tmp_column = macgyver.INIIAL_COLUMN
    print("MacGyver is located in: line",tmp_line,", column",tmp_column)
    with open("labyrinth.json", 'r') as fichlab:
        lab = json.load(fichlab)
    labyrinth.display_lab(lab,macgyver.INITIAL_LINE,macgyver.INIIAL_COLUMN,0,0) # display labyrinth
    while game != 'end':
        moving = menu()
        line = 0
        column = 0
        macgyver.mac_move(moving)
        line = macgyver.line
        column = macgyver.column
        print("les lignes et colonnes de déplacement :",line,column)
        macgyver_newline = macgyver.INITIAL_LINE + line
        macgyver_newcolumn = macgyver.INIIAL_COLUMN + column
        print("la position: ",macgyver_newline,macgyver_newcolumn)
        if lab[macgyver_newline][macgyver_newcolumn] == "*":
            print("you can't move in this direction, there is a wall, try an other movement")
            print()
            continue
        else:
            print("new position for MacGyver: line",macgyver_newline,", column ",macgyver_newcolumn)
            print(tmp_line,tmp_column)
            labyrinth.display_lab(lab,macgyver_newline,macgyver_newcolumn,tmp_line,tmp_column)
        tmp_line = macgyver_newline
        tmp_column = macgyver_newcolumn
        print(tmp_line,tmp_column)
        macgyver.macgyver_bag(lab,macgyver_newline,macgyver_newcolumn)
        if macgyver.objectfound == 'TRUE':
            bag.append(macgyver.bag)
        nb_items = len(bag)
        if len(bag) == 0:
            print("vous n'avez aucun objet, continuez à chercher")
        elif len(bag) < 3:
            print("vous avez %d objets il vous en manque %d" %(len(bag),3-len(bag)))
        else:
            print("vous avez tous les objets nécessaires pour endormir le garde, vous devez encore trouver la sortie")
        if  not (lab[macgyver_newline][macgyver_newcolumn] == "G" and len(bag) == 3):
            continue
        elif lab[macgyver_newline][macgyver_newcolumn] == "G" and len(bag) == 3:
            print("vous avez gagné !!!")
            game = 'end'
        else:
            print("vous êtes mort: vous n'aviez pas tous les objets")
            game = 'end'
        break
    
     
main()    
