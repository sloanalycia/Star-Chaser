import pygame

class Star_Character():
	def __init__(self,screen,bg_image):
	
		#Initialize the character onto the screen in its starting position
		#We will call the character Nova
		self.screen = screen
	
		#load the character image to the screen
		self.image = pygame.image.load('image/nova_char.bmp')
		self.rect = self.image.get_rect
		self.screen_rect = self.screen.get_rect
	
		#start each character at the center of the left of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.left = self.screen_rect.left
	
	def blitme(self):
		#Draw the character at its current location
		self.screen.blit(self.image,self.rect)
	
