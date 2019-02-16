import pygame
from pygame.sprite import Sprite
from random import randint

#import time?

class Alien1(Sprite):
	#this class represents this alien as generated randomly
	
	def __init__(self,ai_settings,screen):

		super(Alien1,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		
		self.image = pygame.image.load('images/alien_1.bmp')
		self.image.set_colorkey((255,255,255))
		self.rect = self.image.get_rect()
		
		clock = pygame.time.Clock()
		
		alien_1_random = randint(20,600)
		
		
		self.rect.x = 1100
		self.rect.y = alien_1_random
		
		
		self.x = float(self.rect.x)
		
		rand_alien_spot = (self.rect.x, self.rect.y)
		
			
		dt = clock.tick(30)/1000
	
		timer = 1
		
		timer -= dt	
			
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
	def update(self):
		
		if timer >=0:
			alien_1_group.add(Block(rand_alien_spot))
			self.x -= self.ai_settings.alien_1_speed
			self.rect.x = self.x
			timer = 1
		
		
	
		
		
		
		
		
		
		
		
	'''
	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.left >= screen_rect.left:
			return True
		elif self.rect.left <=0:
			return True
	'''
			
