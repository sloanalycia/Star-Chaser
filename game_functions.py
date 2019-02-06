import sys

import pygame

from bullet import Bullet



def check_keydown_events(event,nova,bullets):
	
		if event.key == pygame.K_UP:
			nova.moving_up = True
			
		elif event.key == pygame.K_DOWN:
			nova.moving_down = True
			
			
		elif event.key == pygame.K_SPACE:
			new_bullet = Bullet(ai_settings,screen,nova)
			bullets.add(new_bullet)
	
def check_keyup_events(event,nova):
	
		if event.key == pygame.K_UP:
			nova.moving_up = False
					
		elif event.key == pygame.K_DOWN:
			nova.moving_down = False

def check_events(ai_settings,screen,nova,bullets):
	#Respond to key presses and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,nova,bullets)
			
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,nova)
			
			

def update_screen(ai_settings,screen,nova,bullets):
	#Update images on the screen and flip to the new screen
	
	#Redraw the screen during each pass through the loop
		screen.fill(ai_settings.bg_color)
		
		screen.blit(ai_settings.bg_image,[0,0])
		
		#redraw all bullets behind nova and other features
		for bullet in bullets.sprites():
			bullet.draw_bullet()
		
		nova.blitme()
				
		#Make the most recently drawn screen visible
		pygame.display.flip()
