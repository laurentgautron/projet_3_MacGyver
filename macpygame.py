#! /usr/bin/env python3
# coding: utf-8
import pygame
from pygame.locals import *

class Macpygame:
	def __init__(self): #  conten pictures for items, Macgyver and Guardian for pygame
		self.ecran = pygame.display.set_mode((600,600), RESIZABLE)
		self.mur = pygame.image.load('carre.bmp').convert()
		self.joueurmac = pygame.image.load('carreb.bmp').convert()
		self.guard = pygame.image.load('carrer.bmp').convert()
		self.blowpipe = pygame.image.load('carrej.bmp').convert()
		self.syringe = pygame.image.load('carrem.bmp').convert()
		self.poison = pygame.image.load('carreg.bmp').convert()

	