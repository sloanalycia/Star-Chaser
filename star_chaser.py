

import pygame

from pygame.sprite import Group

from galaxy_settings import Settings

from star_character import Star_Character

from alien_1 import Alien1

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
	bullets = Group()
	
	#Set the background image
	bg_color = (255,255,255)
	
	alien_1 = Alien1(ai_settings,screen)
	
	
	
	#Start the main loop for the game.
	while True:
		
		gf.check_events(ai_settings, screen,nova,bullets)
		
		nova.update()
		
		gf.update_bullets(bullets)
		
		#gf.update_alien(alien1)		
		
		gf.update_screen(ai_settings,screen,nova,alien_1,bullets)

run_game()
		
