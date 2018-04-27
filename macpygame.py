#! /usr/bin/env python3
# coding: utf-8
import pygame
from pygame.locals import *
import sys
import json

#from textdescription import Textdescription

class Macpygame:
	""" three functions in this class: __init__ to create person and items,  display to display labyrinth with pygame and display_text to write text on the screen """
	def __init__(self): #  conten pictures for items, Macgyver and Guardian for pygame
		pygame.init()
		self.ecran = pygame.display.set_mode((750,950))
		self.mur = pygame.image.load('carre.bmp').convert()
		self.joueurmac = pygame.image.load('carreb.bmp').convert()
		self.guard = pygame.image.load('carrer.bmp').convert()
		self.blowpipe = pygame.image.load('carrej.bmp').convert()
		self.syringe = pygame.image.load('carrem.bmp').convert()
		self.poison = pygame.image.load('carreg.bmp').convert()

	def display(self,lab):
		perso_x = 0
		perso_y = 0
		continuer = True
		for indices, values in enumerate(lab):
			for ind, val in enumerate(values):
				perso_x = ind * 50
				perso_y = indices * 50
				if val == '*':
					self.ecran.blit(self.mur,(perso_x,perso_y))
				if val == 'M':
					self.ecran.blit(self.joueurmac,(perso_x,perso_y))
				if val == 'G':
					self.ecran.blit(self.guard,(perso_x,perso_y))
				if val == 'B':
					self.ecran.blit(self.blowpipe,(perso_x,perso_y))
				if val == 'S':
					self.ecran.blit(self.syringe,(perso_x,perso_y))
				if val == 'P':
					self.ecran.blit(self.poison,(perso_x,perso_y))
		pygame.display.flip()

	def display_text(self,chain): # display according to the situation with text planned in a fich
		pygame.font.init()
		i = 10
		with open(chain, 'r') as textfich:
			for sentence in textfich:
				font = pygame.font.SysFont('Comic Sans MS', 15)
				text = font.render(sentence, True,(255,255,255))
				self.ecran.blit(text,(10,750+i))
				i += 20
		pygame.display.flip()
		continuer = True
		while continuer:
			event = pygame.event.wait()
			if event.type == KEYDOWN:
				continuer = False


		
	