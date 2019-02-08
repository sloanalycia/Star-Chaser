
import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
#a class to manage bullets fired by nova character	

	def __init__(self,ai_settings,screen,nova):
		#create a bullet object at the characters position
		super().__init__()
		self.screen = screen
	
		#create a bullet rect at 0,0 and then correct the position
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.right = nova.rect.right
		self.rect.center = nova.rect.center
	
		#store the bullets as a decimal
		self.x = float(self.rect.x)
	
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		#move bullets across the screen
		#update decimal position of bullet
		self.x += self.speed_factor
		
		#update rect position
		self.rect.x = self.x
		
		
	def draw_bullets(self):
		#draw bullets to the screen
		pygame.draw.rect(self.screen,self.color,self.rect)
		
	
		
