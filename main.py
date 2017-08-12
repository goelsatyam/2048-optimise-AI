import numpy as np
from moves import *
from animation import *
from preCalculate import allMoves
import pygame,sys
from pygame.locals import *

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

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == KEYUP:
				key = event.key
				check = board
				if key == 273:
					board, score = upMove(board,tposedp,rightdp,rightscores)
				elif key == 274:
					board, score = downMove(board,tposedp,leftdp,leftscores)	
				elif key == 275:
					board, score = leftMove(board,leftdp,leftscores)	
				elif key == 276:
					board, score = rightMove(board,rightdp,rightscores)	

				if check!=board	:
					totalscore = totalscore + score	
					board = randomSelection(board)
					startAnimation(displaysurf,board,totalscore)
					printTerminal(board,totalscore)	



if __name__ == '__main__':
		main()	