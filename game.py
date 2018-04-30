from labyrinth import Labyrinth
from macgyver import Macgyver
from test import Test
from macpygame import Macpygame

class Main:
    """ two function in this class : the init function to define instances, initialize and show position of Macgyver, Guardianand items
        in thr labyrinth. The second function is used to play """
    def __init__(self):
        # instances and variables we need to play
        self.macpygame = Macpygame()
        self.testbox = Test()
        self.mcgyver = Macgyver()
        self.labyrinth = Labyrinth('labyrinth.json',self.macpygame)    # init labyrinth in lab with items randomly
        self.x, self.y = self.labyrinth.found('M') # found Macgyver
        self.guardian_x,self.guardian_y = self.labyrinth.found('G')   # found Guardian
        self.last_x, self.last_y = self.x, self.y # first and last positon are the same at the beginning
        self.bag = []  # init MacGyver's bag
        self.labyrinth.display_lab(self.x,self.y,self.last_x,self.last_y)
        self.macpygame.display_text('rules.txt')    # write rules

    def play(self):
        #  main programm to play 
        while (self.x,self.y) != (self.guardian_x,self.guardian_y):  # repeat while position is not guardian's position
            self.x,self.y = self.mcgyver.move(self.last_x,self.last_y)  # read new position for MacGyver
            if self.testbox.there_is_a_wall(self.labyrinth.lab,self.x,self.y):   # check if there is not a wall
                self.macpygame.display_text('meet_a_wall.txt')
                continue
            elif self.testbox.there_is_an_item(self.labyrinth.lab,self.x,self.y):   # check if there is not an item
                it = self.labyrinth.lab[self.x][self.y]
                self.bag.append(it)
                self.mcgyver.add_contents(self.mcgyver.bagcontents(it))
                self.labyrinth.display_lab(self.x,self.y,self.last_x,self.last_y)
                self.macpygame.display_text('bagcontents.txt')
            self.labyrinth.display_lab(self.x,self.y,self.last_x,self.last_y)
            self.last_x = self.x   # stock MacGyver last position
            self.last_y = self.y
        if len(self.bag) != 3:   # check if there is three items in bag
            self.macpygame.display_text('looser.txt')
        else:
            self.macpygame.display_text('winner.txt')
            
if __name__ == '__main__':
    main = Main()
    main.play()