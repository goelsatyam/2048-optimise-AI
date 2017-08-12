import numpy as np
import random 

def toExp(number):
	return np.int(np.log(number)/np.log(2))

def getTile():
	''' This will generate 2 90% of the times and 4 10% times'''
	if random.random() <= 0.9:
		return 2
	else:
		return 4	

def emptyCells(board):
	''' This will generate list of empty cells'''
	empty = []
	for i in range(16):
		x = board & np.uint64(15)
		board = board >> np.uint64(4)
		if x == 0:
			empty.append((i))

	return empty		

def randomTile(board):
	''' Select random tile from list of empty tiles'''
	empty = emptyCells(board)
	return empty[random.randint(0,len(empty)-1)]

def setTile(board,digit,tile):
	'''Set value of tile in the board'''
	return (board | ( np.uint64(digit) << np.uint64(tile*4) ))

def	randomSelection(board):
	try:
		tile = randomTile(board)
		digit = getTile()
		digit = toExp(digit)
		return setTile(board,digit,tile)
	except:
		return board	


def leftMove(board,leftdp,leftscores):
	ans = np.uint64(0)
	x = np.power(2,16)-1
	score = np.uint64(0)
	for i in range(4):
		value = board & np.uint64(x)
		board = board >> np.uint64(16)
		ans = ans | (leftdp[value] << np.uint64(16*i))
		score+=leftscores[value]

	return ans, score	

def rightMove(board,rightdp,rightscores):
	ans = np.uint64(0)
	x = np.power(2,16)-1
	score = np.uint64(0)
	for i in range(4):
		value = board & np.uint64(x)
		board = board >> np.uint64(16)
		ans =  ans | (rightdp[value] << np.uint64(16*i))
		score+=rightscores[value]

	return ans, score		

def transpose(board,tposedp):
	ans = np.uint64(0)
	x = np.power(2,16)-1
	for i in range(4):
		value = board & np.uint64(x)
		board = board >> np.uint64(16)
		ans = ans | (tposedp[value] << np.uint64(4*i))
	return ans	

def upMove(board,tposedp,rightdp,rightscores):
	board = transpose(board,tposedp)
	board,score = rightMove(board,rightdp,rightscores)
	board = transpose(board,tposedp)
	return board, score

def downMove(board,tposedp,leftdp,leftscores):
	board = transpose(board,tposedp)
	board, score = leftMove(board,leftdp,leftscores)
	board = transpose(board,tposedp)
	return board,score	

def mono(board, tdpose, monoticity):
	t = transpose(board, tdpose)
	ans = 0
	for i in range(4):
		key = board & np.uint64(65535)
		ans+=monoticity[key]
		key = t & np.uint64(65535)
		ans+=monoticity[key]
		board = board >> np.uint64(16)
		t = t >> np.uint64(16)

	return ans

