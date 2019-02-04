import sys

import pygame

from galaxy_settings import Settings


def run_game():
	#Initialize the game and create the screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Star Chaser")
	
	#Set the background image
	bg_color = (255,255,255)
	
	
	
	
	
	#Start the main loop for the game.
	while True:
		
		#Watching for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		#Redraw the screen during each pass through the loop
		screen.fill(ai_settings.bg_color)
		
		#screen.blit(bg_image, [0,0])
				
		#Make the most recently drawn screen visible
		pygame.display.flip()
	

run_game()
		
