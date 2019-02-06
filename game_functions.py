import sys

import pygame

def check_events(nova):
	#Respond to key presses and mouse events
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					nova.moving_up = True
				
				elif event.key == pygame.K_DOWN:
					nova.moving_down = True
			
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					nova.moving_up = False
					
				elif event.key == pygame.K_DOWN:
					nova.moving_down = False

def update_screen(ai_settings,screen,nova):
	#Update images on the screen and flip to the new screen
	
	#Redraw the screen during each pass through the loop
		screen.fill(ai_settings.bg_color)
		
		screen.blit(ai_settings.bg_image,[0,0])
				
		nova.blitme()
				
		#Make the most recently drawn screen visible
		pygame.display.flip()
