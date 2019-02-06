
import pygame

class Star_Character():
	
	def __init__(self,ai_settings,screen):
	
		#Initialize the character onto the screen in its starting position
		#We will call the character Nova
		self.screen = screen
		
		self.ai_settings = ai_settings
	
		#load the character image to the screen
		self.image = pygame.image.load('images/nova_char.png').convert()
		self.image.set_colorkey((255,255,255))
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		#start each character at the center of the left of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.midleft = self.screen_rect.midleft
		
		#Store a decimal value for the characters center
		self.center = float(self.rect.centery)
		
		#Movement Flag
		self.moving_up = False
		self.moving_down = False
		
	def update(self):
		#Update the character's position based on the movement flag
		if self.moving_up and self.rect.top>0:
			self.center -= self.ai_settings.nova_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.center += self.ai_settings.nova_speed_factor
		
		self.rect.centery = self.center
		
	
		
	
	def blitme(self):
		#Draw the character at its current location
		self.screen.blit(self.image,self.rect)
		
		
	
