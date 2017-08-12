import numpy as np
from moves import *
from animation import *
from preCalculate import allMoves
import pygame,sys
from pygame.locals import *
from ai import *
import random
def main():
	pygame.init()
	board = np.uint64(0)
	board = randomSelection(board)
	board = randomSelection(board)
	totalscore = 0
	print board
	leftdp, rightdp, tposedp, leftscores, rightscores, monoticity =  allMoves()
	#printTerminal(board,totalscore)	

	displaysurf = pygame.display.set_mode((640,480))
	startAnimation(displaysurf,board,totalscore)
	dp = {}
	x= True	
	while True:
		while True:

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()	
			if x:
				key = mainAI(board, leftdp, rightdp, leftscores, rightscores, tposedp, monoticity, totalscore)
				check = board
				print key,mono(board,tposedp,monoticity)*100000
				if key == 273:
					board, score = upMove(board,tposedp,rightdp,rightscores)
				elif key == 274:
					board, score = downMove(board,tposedp,leftdp,leftscores)	
				elif key == 275:
					board, score = leftMove(board,leftdp,leftscores)	
				elif key == 276:
					board, score = rightMove(board,rightdp,rightscores)	
				else:
					x = False

				if check!=board	:
					totalscore = totalscore + score	
					board = randomSelection(board)
					startAnimation(displaysurf,board,totalscore)
					



if __name__ == '__main__':
		main()	