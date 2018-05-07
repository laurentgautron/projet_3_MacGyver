import json
import random
import sys

class Labyrinth:
    """ this class do operations with the lab variable, a list of lists representing the labyrinth. """

    def __init__(self, map_lab,macpygame):
        """ open the labyrinth file and create labyrinth with list_items randomly. 
            
            arg  map_lab: text file for the labyrinth, already contains walls and person

            raise an exception if file is not found.
                 
        """

        self.macpygame = macpygame
        try:
            with open(map_lab, 'r') as labfich:
                self.lab = json.load(labfich)
        except OSError:
            print('cannot open file')
            sys.exit()
        else:
            list_items = ['B','P','S']
            while list_items != []:
                column = random.randint(0,14)
                line = random.randint(0,14)
                if self.lab[column][line] == ' ':
                    # take an item in the list_items ( items to locate )
                    self.lab[column][line] = list_items[0]
                    del list_items[0]
        
    def display_lab(self,x,y,last_x,last_y):
        """ change lab variable.

            arg x, y : integer, macgyver's new position 
                last_x, last_y : integer macgyver's last position, become an empty space 

            Then labyrinth is displayed with a pygame 
        """

        self.lab[x][y] = 'M'
        # in the beginning no movement x, y = last_x, last_y
        # to not erase macgyver at the beginning
        if (x,y) != (last_x,last_y):
            self.lab[last_x][last_y] = ' '
        self.macpygame.display(self.lab)
            
    def find(self,person):
        """ search where are the person in the labyrinth, MacGyver or the Guardian and return position
            
            arg person: string
            return pos_x, pos_y : integers

        """

        for i, line in enumerate(self.lab):
            for j, column in enumerate(line):
                if column == person:
                    self.pos_x = i
                    self.pos_y = j
        return self.pos_x,self.pos_y

    def there_is_a_wall(self,x,y):
        """ check if there is a wall and return Boolean """

        if self.lab[x][y] == '*':
            return True
        else:
            return False
            
    def there_is_an_item(self,x,y):
        """ check if there is an iitem and return Boolean """

        if self.lab[x][y] in ['B','P','S']:
            return True
        else:
            return False