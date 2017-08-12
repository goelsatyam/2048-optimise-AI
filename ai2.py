import numpy as np 
from moves import *

def mainAI(board, leftdp, rightdp, leftscores, rightscores, tposedp, monoticity, totalscore):
	empty = len(emptyCells(board))
	depth = 4
	maxscore = -1
	key = None
	move, score = leftMove(board, leftdp, leftscores)
	if move != board:
		score = bestMove(move, depth, leftdp, rightdp, leftscores, rightscores, tposedp, totalscore+score,False)
		if score > maxscore:
			maxscore = score
			key = 275

	move, score = rightMove(board, rightdp, rightscores)
	if move != board:
		score = bestMove(move, depth, leftdp, rightdp, leftscores, rightscores, tposedp, totalscore+score,False)
		if score > maxscore:
			maxscore = score
			key = 276

	move, score = upMove(board, tposedp, rightdp, rightscores)
	if move != board:
		score = bestMove(move, depth, leftdp, rightdp, leftscores, rightscores, tposedp, totalscore+score,False)
		if score > maxscore:
			maxscore = score
			key = 273

	move, score = downMove(board, tposedp, leftdp, leftscores)
	if move != board:
		score = bestMove(move, depth, leftdp, rightdp, leftscores, rightscores, tposedp, totalscore+score,False)
		if score > maxscore:
			maxscore = score
			key = 274

	print maxscore,		
	return key		

def bestMove(board, depth, leftdp, rightdp, leftscores, rightscores, tposedp, totalscore, prun):
	if depth == 0:
		return totalscore + len(emptyCells(board))*10000

	
	if prun == False:	
		empty = emptyCells(board)	
		if len(empty) == 0:
			return 0

		score = 0.0	
		for i in empty:
			new = setTile(board,2,i)
			score+=bestMove(new, depth-1, leftdp, rightdp, leftscores, rightscores, tposedp, totalscore, True)*0.9*(1.0/len(empty))
			new = setTile(board,4,i)
			score+=bestMove(new, depth-1, leftdp, rightdp, leftscores, rightscores, tposedp, totalscore, True)*0.1*(1.0/len(empty))	
		return score		
	else:
		maxscore = 0 
		new,score = leftMove(board, leftdp, leftscores)
		score = bestMove(new, depth-1, leftdp, rightdp, leftscores, rightscores, tposedp, totalscore+score, False)
		maxscore = max(maxscore, score)
		new, score = rightMove(board, rightdp, rightscores)
		score = bestMove(new, depth-1, leftdp, rightdp, leftscores, rightscores, tposedp, totalscore+score, False)
		maxscore = max(maxscore, score)
		new, score = upMove(board, tposedp, rightdp, rightscores)
		score = bestMove(new, depth-1, leftdp, rightdp, leftscores, rightscores, tposedp, totalscore+score, False)
		maxscore = max(maxscore, score)
		new, score = upMove(board, tposedp, rightdp, rightscores)
		score = bestMove(new, depth-1, leftdp, rightdp, leftscores, rightscores, tposedp, totalscore+score, False)
		maxscore = max(maxscore, score)
		return maxscore
	