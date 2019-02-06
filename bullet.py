import Pygame

from pygame.sprite import Sprite

class Bullet(sprite):
#a class to manage bullets fired by nova character	
	def __ini__(self,ai_settings,screen,nova):
		#create a bullet object at the characters position
		super(Bullet,self).__init__()
		self.screen = screen
	
		#create a bullet rect at 0,0 and then correct the position
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centery = nova.rect.centery
		self.rect.top = nova.rect.top
	
		#store the bullets as a decimal
		self.y = float(self.rect.y)
	
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		#move bullets across the screen
		#update decimal position of bullet
		self.y -= self.speed_factor
		
		#update rect position
		self.rect.y = self.y
		
		
	def draw_bullets(self):
		#draw bullets to the screen
		pygame.draw.rects(self.screen,self.color,self.rect)
		
	
		
