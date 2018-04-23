""" class test if there is a wall or an item """

#! /usr/bin/env python3
# coding: utf-8

class Test:
    """ test if there is a wall or an item and return boolean
    use the labyrinth fich and player's position """
    def there_is_a_wall(self,lab,x,y):
        if lab[x][y] == '*':
            return True
        else:
            return False
            
    def there_is_an_item(self,lab,x,y):
        if lab[x][y] in ['B','P','S']:
            return True
        else:
            return False