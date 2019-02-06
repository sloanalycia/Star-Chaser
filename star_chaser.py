

import pygame

from galaxy_settings import Settings

from star_character import Star_Character

import game_functions as gf

def run_game():
	#Initialize the game and create the screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Star Chaser")
	
	#Make the character
	nova = Star_Character(ai_settings,screen)
	
	#make bullet group to store bullets
	bullet = Group()
	
	#Set the background image
	bg_color = (255,255,255)
	
	
	
	
	
	#Start the main loop for the game.
	while True:
		
		gf.check_events(ai_settings, screen,nova,bullets)
		
		nova.update()
		
		bulelts.update()
		
		gf.update_screen(ai_settings,screen,nova,bullets)
		
		#get rid of bullets that have disappeared
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
				
		prin(len(bullets))
		

run_game()
		
