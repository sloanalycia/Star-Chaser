import sys

import pygame


def check_keydown_events(event,nova):
	
		if event.key == pygame.K_UP:
			nova.moving_up = True
			
		elif event.key == pygame.K_DOWN:
			nova.moving_down = True
	
def check_keyup_events(event,nova):
	
		if event.key == pygame.K_UP:
			nova.moving_up = False
					
		elif event.key == pygame.K_DOWN:
			nova.moving_down = False

def check_events(nova):
	#Respond to key presses and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,nova)
			
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,nova)
			
			

def update_screen(ai_settings,screen,nova):
	#Update images on the screen and flip to the new screen
	
	#Redraw the screen during each pass through the loop
		screen.fill(ai_settings.bg_color)
		
		screen.blit(ai_settings.bg_image,[0,0])
				
		nova.blitme()
				
		#Make the most recently drawn screen visible
		pygame.display.flip()
