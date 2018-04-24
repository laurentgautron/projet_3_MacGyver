#! /usr/bin/env python3
# coding: utf-8

class Macpygame:
	def __init__(self): #  conten pictures for items, Macgyver and Guardian for pygame
		ecran = pygame.display.set_mode((600,600), RESIZABLE)
		mur = pygame.image.load('carre.bmp').convert()
		joueurmac = pygame.image.load('carreb.bmp').convert()
		guard = pygame.image.load('carrer.bmp').convert()
		blowpipe = pygame.image.load('carrej.bmp');convert()
		syringe = pygame.image.load('carrem.bmp').convert()
		poison = pygame.image.load('carreg.bmp').convert()

	