""" this is the text you need in the game of Labyrinth to show the rules and move MacGyver """

#! /usr/bin/env python3
# coding: utf-8

class Textdescription:
    
    def rules(self):
        print("this is a labyrinth game: you must help MacGyver to find the exit")
        print("for it , you need to asleep the guardian with items which scattered in this labyrinth")
        print("you can move MacGyver with keyboards keys")
        print("to win , you have to pick up all items: poison, blowpipe, an syringe and go in front of the Guardian")
        print("now you can play")
        
    def menu(self):
        ch = ''
        while ch not in ['z','d','q','s']:
            print("move Macgyver")
            print("to the top: type 'z'")
            print("to the right: type 'd'")
            print("to the left: type 'q'")
            print("to the down: type 's'")
            ch = input('your choice: ')
            if ch not in ['z','d','q','s']:
                print('be carefull, this choice is not in the list !!')
                continue
            else:
                return ch