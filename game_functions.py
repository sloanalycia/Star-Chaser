import sys

import pygame

from bullet import Bullet



def check_keydown_events(event,ai_settings,screen,nova,bullets):
	
	if event.key == pygame.K_UP:
		nova.moving_up = True
			
	elif event.key == pygame.K_DOWN:
		nova.moving_down = True
			
			
	elif event.key == pygame.K_SPACE:
		fire_bullets(ai_settings,screen,nova,bullets)
		
	elif event.key == pygame.K_q:
		sys.exit()
		
def fire_bullets(ai_settings,screen,nova,bullets):
		if len(bullets) < ai_settings.bullets_allowed:
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
			
			

def update_screen(ai_settings,screen,nova,alien_1,bullets):
	#Update images on the screen and flip to the new screen
	
	#Redraw the screen during each pass through the loop
		screen.fill(ai_settings.bg_color)
		
		screen.blit(ai_settings.bg_image,[0,0])
		
		#redraw all bullets behind nova and other features
		for bullet in bullets.sprites():
			bullet.draw_bullets()
		
		nova.blitme()
		alien_1.blitme()
				
		#Make the most recently drawn screen visible
		pygame.display.flip()
		
def update_bullets(bullets):
	
	bullets.update()

	#get rid of bullets that have disappeared
	for bullet in bullets.copy():
		if bullet.rect.left >= 1200:
			bullets.remove(bullet)
	print(len(bullets))
