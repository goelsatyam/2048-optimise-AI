import numpy as np
import pygame,sys
from pygame.locals import *

white = (255, 255, 255)
blue = (0,204,204)
darkblue = (0,128,125)
lightBlue = (102, 255, 255)
black= (0,0,0)
darkturqoise = (3,54,73)

bgbox = darkblue
textcolor = white
boxcolor = blue
bgtext = lightBlue
bgcolor = black

windowwidth  = 640
windowheight = 480
boxwidth = 80
boxheight = 80
border = 4
cols = 4
rows = 4

xmargin = int((windowwidth - (boxwidth*cols))/2)
ymargin = int((windowheight - (boxheight*rows))/2)



def printTerminal(board,score):
	count =0 
	for i in range(16):
		print board & np.uint64(15),"  ",
		board = board >> np.uint64(4)
		count +=1
		if count == 4:
			print ""
			count = 0

	print "Score-> %d\n"%(score)

def topCoordinates(x,y):
	left, top = xmargin + y*boxheight, ymargin + x*boxwidth
	return left, top

def displayDigit(left,top,digit,displaysurf):
	pygame.draw.rect(displaysurf,bgtext,(left,top,boxwidth-2,boxheight-2))
	fontObj = pygame.font.Font('freesansbold.ttf', 20)
	textSurfaceObj = fontObj.render(str(digit), True, textcolor,bgtext)
	textRecteObj = textSurfaceObj.get_rect()
	textRecteObj.center = (left+boxwidth/2,top+boxheight/2)
	displaysurf.blit(textSurfaceObj, textRecteObj)
	pygame.display.update()

def showScore(score,displaysurf):
	pygame.draw.rect(displaysurf,black,(90,0,200,40))
	fontObj = pygame.font.Font('freesansbold.ttf', 20)
	textSurfaceObj = fontObj.render('Total Score : %d'%(score), True, white,bgcolor)
	textRecteObj = textSurfaceObj.get_rect()
	textRecteObj.center = (180,20)
	displaysurf.blit(textSurfaceObj,textRecteObj)
	pygame.display.update()

def  startAnimation(displaysurf, board,score):
	pygame.draw.rect(displaysurf,bgbox,(xmargin-border,ymargin-border,(boxwidth)*cols+border*2,(boxheight)*rows+border*2))	
	for i in range(rows):
		for j in range(cols):
			left, top = topCoordinates(i,j)
			digit = board & np.uint64(15)
			board = board >> np.uint64(4)
			pygame.draw.rect(displaysurf,boxcolor,(left,top,boxwidth-2,boxheight-2))
			if digit != 0:
				displayDigit(left,top,int(np.power(2,digit)),displaysurf)
	showScore(score,displaysurf)			
	pygame.display.update()		