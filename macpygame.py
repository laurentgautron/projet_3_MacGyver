
import pygame
from pygame.locals import *
import sys
import json

#from textdescription import Textdescription

class Macpygame:
	""" three functions in this class: __init__ to create person and items,  display to display labyrinth with pygame and display_text to write text on the screen """
	def __init__(self): #  conten pictures for items, Macgyver and Guardian for pygame
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
		perso_x = 0
		perso_y = 0
		continuer = True
		for indices, values in enumerate(lab):
			for ind, val in enumerate(values):
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

	def display_text(self,chain): # display according to the situation with text planned in a fich
		pygame.font.init()
		i = 10
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


		
	