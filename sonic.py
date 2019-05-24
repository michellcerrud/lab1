import retro
import random
import pygame 
import sys
import csv
import numpy as np
from pygame.locals import *

env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')
x, z, tab, enter, up, down, left, right, c, s, a, d= [0,0,0,0,0,0,0,0,0,0,0,0]
obs = env.reset()
pygame.init()
win = pygame.display.set_mode((800,600))

with open('sonic_Data.csv', 'a') as f:
	data_sonic = csv.writer(f,delimiter=',',quoting=csv.QUOTE_MINIMAL)
	
	while True:
		img = pygame.image.frombuffer(obs.tostring(), obs.shape[1::-1], "RGB")
		img = pygame.transform.scale(img, (800,600))
		win.blit(img,(0,0))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_x:
					x = 1
				if event.key == pygame.K_z:
					z = 1
				if event.key == pygame.K_TAB:
					tab = 1
				if event.key == pygame.K_KP_ENTER:
					enter = 1
				if event.key == pygame.K_RIGHT:
					right = 1
				if event.key == pygame.K_LEFT:
					left = 1
				if event.key == pygame.K_UP:
					up = 1
				if event.key == pygame.K_DOWN:
					down = 1
				if event.key == pygame.K_c:
					c = 1
				if event.key == pygame.K_s:
					s = 1
				if event.key == pygame.K_a:
					a = 1
				if event.key == pygame.K_d:
					d = 1
				if event.key == pygame.K_ESCAPE:
					pygame.display.quit()
					break

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_x:
					x = 0
				if event.key == pygame.K_z:
					z = 0
				if event.key == pygame.K_TAB:
					tab = 0
				if event.key == pygame.K_KP_ENTER:
					enter = 0
				if event.key == pygame.K_RIGHT:
					right = 0
				if event.key == pygame.K_LEFT:
					left = 0
				if event.key == pygame.K_UP:
					up = 0
				if event.key == pygame.K_DOWN:
					down = 0
				if event.key == pygame.K_c:
					c = 0
				if event.key == pygame.K_s:
					s = 0
				if event.key == pygame.K_a:
					a = 0	
				if event.key == pygame.K_d:
					d = 0
				if event.type == pygame.K_ESCAPE:
					pygame.display.quit()
					break

		action = [x,z,tab,enter,up,down,left,right,c,s,a,d]
		obs, rew, done, info = env.step(action)
		dataCsv =[rew,done,action,info]
		data_sonic.writerow(dataCsv)
		#csv_obs.writerow(np.append(obs,action))
