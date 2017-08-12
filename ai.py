import numpy as np 
from moves import *

def mainAI(board, leftdp, rightdp, leftscores, rightscores, tposedp, monoticity, totalscore):
	depth = 3
	maxscore = -1
	key = None

	move, score = leftMove(board, leftdp, leftscores)
	if move != board:
		score = bestMove(move, depth, leftdp, rightdp, leftscores, rightscores, tposedp, monoticity, totalscore+score)
		if score > maxscore:
			maxscore = score
			key = 275

	move, score = rightMove(board, rightdp, rightscores)
	if move != board:
		score = bestMove(move, depth, leftdp, rightdp, leftscores, rightscores, tposedp, monoticity, totalscore+score)
		if score > maxscore:
			maxscore = score
			key = 276

	move, score = upMove(board, tposedp, rightdp, rightscores)
	if move != board:
		score = bestMove(move, depth, leftdp, rightdp, leftscores, rightscores, tposedp, monoticity, totalscore+score)
		if score > maxscore:
			maxscore = score
			key = 273

	move, score = downMove(board, tposedp, leftdp, leftscores)
	if move != board:
		score = bestMove(move, depth, leftdp, rightdp, leftscores, rightscores, tposedp, monoticity, totalscore+score)
		if score > maxscore:
			maxscore = score
			key = 274

	print maxscore,		
	return key		

def bestMove(board, depth, leftdp, rightdp, leftscores, rightscores, tposedp, monoticity, totalscore):
	if depth == 0:
		return  len(emptyCells(board))*100000 +mono(board,tposedp,monoticity)*100000

	board = randomSelection(board)
	maxscore = -1

	move, score = leftMove(board, leftdp, leftscores)
	score = bestMove(move, depth-1, leftdp, rightdp, leftscores, rightscores, tposedp, monoticity, totalscore+score)
	maxscore = max(maxscore, score)

	move, score = rightMove(board, rightdp, rightscores)
	score = bestMove(move, depth-1, leftdp, rightdp, leftscores, rightscores, tposedp, monoticity, totalscore+score)
	maxscore = max(maxscore, score)

	move, score = upMove(board, tposedp, rightdp, rightscores)
	score = bestMove(move, depth-1, leftdp, rightdp, leftscores, rightscores, tposedp, monoticity, totalscore+score)
	maxscore = max(maxscore, score)

	move, score = downMove(board, tposedp, leftdp, leftscores)
	score = bestMove(move, depth-1, leftdp, rightdp, leftscores, rightscores, tposedp, monoticity, totalscore+score)
	maxscore = max(maxscore, score)

	return maxscore