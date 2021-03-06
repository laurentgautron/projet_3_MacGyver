import sys

import pygame

from pygame.locals import *

class Macpygame:
	""" In this class we use the pyagame module for graphic interface."""

	def __init__(self):
		""" create screen for the game loading image for wall, gaurdian, poison, syringe, blowpipe and empty square. """

		pygame.init()
		self.screen = pygame.display.set_mode((750,950))
		self.empty = pygame.image.load('images_box/empty_box.bmp').convert()
		self.wall = pygame.image.load('images_box/wall_box.bmp').convert()
		self.player_mac = pygame.image.load('images_box/mac_box.bmp').convert()
		self.guard = pygame.image.load('images_box/guardian_box.bmp').convert()
		self.blowpipe = pygame.image.load('images_box/blowpipe_box.bmp').convert()
		self.syringe = pygame.image.load('images_box/syringe_box.bmp').convert()
		self.poison = pygame.image.load('images_box/poison_box.bmp').convert()

	def display(self,lab):
		""" copy pictures on the screen testing in lab file what is in the square:
		item , person or wall and ten display it. """

		# squares indices
		perso_x = 0
		perso_y = 0
		continuer = True
		# two loops to get square indices
		for indices, values in enumerate(lab):
			for ind, val in enumerate(values):
				 # square indices on the screen 
				perso_x = ind * 50
				perso_y = indices * 50
				if val == ' ':
					self.screen.blit(self.empty,(perso_x,perso_y))
				if val == '*':
					self.screen.blit(self.wall,(perso_x,perso_y))
				if val == 'M':
					self.screen.blit(self.player_mac,(perso_x,perso_y))
				if val == 'G':
					self.screen.blit(self.guard,(perso_x,perso_y))
				if val == 'B':
					self.screen.blit(self.blowpipe,(perso_x,perso_y))
				if val == 'S':
					self.screen.blit(self.syringe,(perso_x,perso_y))
				if val == 'P':
					self.screen.blit(self.poison,(perso_x,perso_y))
		pygame.display.flip()

	def display_text(self,chain):
		""" open text file recovered in chain, define a font and display text line by line.

			chain: string, name of the text file

			raise an exception if file is not found
		"""

		pygame.font.init()
		# counter to space out text after each line
		i = 10
		try:
			with open(chain, 'r') as textfich:
				for sentence in textfich:
					sentence = sentence.rstrip('\n')
					font = pygame.font.SysFont('Comic Sans MS', 15)
					text = font.render(sentence, True,(255,255,255))
					self.screen.blit(text,(10,750+i))
					i += 20
		except OSError:
			print('cannot open file ',chain)
			sys.exit()
		else:
			pygame.display.flip()
			continuer = True
			while continuer:
				event = pygame.event.wait()
				if event.type == KEYDOWN:
					continuer = False
			self.screen.fill(0)


		
	