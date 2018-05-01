import sys
import json

import pygame
from pygame.locals import *

class Macpygame:
	""" """
	def __init__(self):
		""" create screen for the game loading image for wall, gaurdian, poison, syringe, blowpipe and empty square"""
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
		item , person or wall and ten display it"""
		perso_x = 0 # squares indices
		perso_y = 0
		continuer = True
		for indices, values in enumerate(lab): # two loop to get square indices
			for ind, val in enumerate(values):
				perso_x = ind * 50 # square indices on the screen 
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
		""" open text file recover in chain, define a font and display text line by line """
		pygame.font.init()
		i = 10 # counter to space out text after each line
		with open(chain, 'r') as textfich:
			for sentence in textfich:
				font = pygame.font.SysFont('Comic Sans MS', 15)
				text = font.render(sentence, True,(255,255,255))
				self.screen.blit(text,(10,750+i))
				i += 20
		pygame.display.flip()
		continuer = True
		while continuer:
			event = pygame.event.wait()
			if event.type == KEYDOWN:
				continuer = False
		self.screen.fill(0)


		
	