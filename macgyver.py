""" game of Labyrinth with MacGyver: try to help MacGyver to escape from labyrinth """

#! /usr/bin/env python3
# coding: utf-8

import json

itemperson = {'G':'Gardien','M':'MacGyver','P':'Poison','S':'syringe','B':'blowpipe'}

#
# display menu
#
def menu():      
    for k,v in itemperson.items():
        print(k + ': ' + v)
    choice = input('choose an item/person: ')
    return choice

#
# make a research of items/person and display labyrinth
#
def research(ch):
    for index, values in enumerate(lab):
        for ind, val in enumerate(values):
            print(val, end='')
            if val == ch:
                i,v = index+1,ind+1
        print()
    print('the %s is in position: %d,%d' %(itemperson[ch],i,v))

#    
# main programm
#
with open("labyrinth.json", 'r') as fichlab:
   lab = json.load(fichlab)
    
research(menu())
