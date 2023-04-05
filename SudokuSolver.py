import numpy as np

data  = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


def possible(x,y, n):
	global data

	for i in range(0,9):
		if data[i][y]==n:
			return False
	for j in range (9):
		if data[x][j]==n:
			return False

	x0 = (x//3)*3
	y0 = (y//3)*3

	for i in range(3):
		for j in range(3):
			if data[x0+i][y0+1] == n:
				return False
	return True



new_b = []
flag = True
def solve():
	global new_b
	global data
	global flag
	for i in range(9):
		for j in range(9):
			if data[i][j] == 0:
				for g in range(1,10):
					if possible(i,j,g):
						#sck()
						data[i][j] = g
						if solve():
							return(True)
						else:
							data[i][j] = 0
				return()
	#print(np.matrix(data))
	return(True)


squares = []
w = 500


import pygame
pygame.init()
screen = pygame.display.set_mode([w, w])

font = pygame.font.Font('freesansbold.ttf', 32)

numbers_to_disp = [1,2,3,4]

running = True
pos= 0 
draw=True
test = 0
added = 0
def sck():
	for i in range(len(data)):
		for j in range(len(data)):
			text = font.render(str(data[i][j]), True, (0,0,0))
			textRect = text.get_rect()
			textRect.center = ((55*j)+27,((55)*i)+27)
			screen.blit(text, textRect)
			

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
        	pos = pygame.mouse.get_pos()
        	x = pos[0]//(w//9)*(w//9)
        	y = pos[1]//(w//9)*(w//9)
        	if (x, y) in squares:
        		squares.remove((x, y))
        	else:
        		squares.append((x, y))
        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_SPACE:
        		print("SOLVING")
        		solve()
        		print("solved", data)
    screen.fill((255, 255, 255))
    x = w//9
    for i in range(9):
    	pygame.draw.line(screen,(0,0,0), (0, x*i), (500,x*i))
    	pygame.draw.line(screen,(0,0,0), (x*i, 0), (x*i,500))
    for s in squares:
    	x= s[0]
    	y= s[1]
    	pygame.draw.rect(screen, (0,0,0), (x//(w//9)*(w//9), y//(w//9)*(w//9), 55, 55))
    sck()
#    for i in range(len(data)):
#    	for j in range(len(data)):
#    		text = font.render(str(data[i][j]), True, (0+test,0+test,0+test))
#    		textRect = text.get_rect()
#   		textRect.center = ((55*j)+27,((55)*i)+27)
#    		screen.blit(text, textRect)

    #screen.blit(text, textRect)

    pygame.display.flip()

pygame.quit()
