import pygame

from labyrinth import Labyrinth
from macgyver import Macgyver
from macpygame import Macpygame

class Main:
    
    def __init__(self):
        """ define instances and variables we need to play, find macgyver and gauardian's position. """

        self.macpygame = Macpygame()
        self.macgyver = Macgyver()
        self.labyrinth = Labyrinth('labyrinth.json',self.macpygame)
        self.x, self.y = self.labyrinth.find('M')
        self.guardian_x,self.guardian_y = self.labyrinth.find('G')
        self.last_x, self.last_y = self.x, self.y
        self.bag = []

    def macgyver_bag(self):
        """ check if macgyver is on an item and so fill variable bag and display text to show bag content. """

        if self.labyrinth.there_is_an_item(self.x,self.y):
            it = self.labyrinth.lab[self.x][self.y]
            self.bag.append(it)
            self.macgyver.add_contents(self.macgyver.bagcontents(it))
            self.labyrinth.display_lab(self.x,self.y,self.last_x,self.last_y)
            self.macpygame.display_text('textfiles/bagcontents.txt')

    def play(self):
        """ main loop to play labyrinth game.

            Display initial labyrinth and rules,
            move macgyver while player is not in front of guardian testing if there is a wall or an item
            and recovering macgyver last position. Then test if bag is fill to win or loose.
        """

        self.labyrinth.display_lab(self.x,self.y,self.last_x,self.last_y)
        self.macpygame.display_text('textfiles/rules.txt')
        while (self.x,self.y) != (self.guardian_x,self.guardian_y):
            event = pygame.event.wait()
            self.x,self.y = self.macgyver.move(self.last_x,self.last_y,event)
            if self.labyrinth.there_is_a_wall(self.x,self.y):
                self.macpygame.display_text('textfiles/meet_a_wall.txt')
                continue
            else:
                self.macgyver_bag()   
            self.labyrinth.display_lab(self.x,self.y,self.last_x,self.last_y)
            # macgyver last position 
            self.last_x = self.x
            self.last_y = self.y
        if len(self.bag) != 3:
            self.macpygame.display_text('textfiles/looser.txt')
        else:
            self.macpygame.display_text('textfiles/winner.txt')
            
if __name__ == '__main__':
    main = Main()
    main.play()