import pygame

class Settings():
	
	"""This is a class to store all settings for Star Chaser"""
	
	def __init__(self):
		#Initialize the game's settings
		#Screen Settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255,255,255)
		
		#Set the background image
		self.bg_image = pygame.image.load("images/galaxy_bg.bmp")
		
		#character settings
		self.nova_speed_factor = 3.5
		
		#bullet settings
		self.bullet_speed_factor = 1 
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (233,233,233)
