import numpy as np

def left(a):
	curr = 12
	flag = 0
	last = 0
	ans = np.uint64(0)
	score = 0
	flag
	for i in range(4):
		if a[i]!=0:
			if flag == 0:
				flag = 1
				last = a[i]
			else:
				if a[i] == last:
					flag = 0
					ans = ans | (np.uint64(a[i]+1) << np.uint64(curr))
					score+=np.power(2,a[i]+1)
					#print a[i]+1,
					curr-=4
				else:
					#print last,
					ans = ans | (np.uint64(last) << np.uint64(curr))
					last = a[i]
					curr-=4
	if flag == 1:
		#print last,
		ans = ans | (np.uint64(last) << np.uint64(curr))

	return ans,score						

def right(a):
	curr = 0
	flag = 0
	last = 0
	ans = np.uint64(0)
	score = 0
	for i in range(3,-1,-1):
		if a[i]!=0:
			if flag == 0:
				flag = 1
				last = a[i]
			else:
				if a[i] == last:
					flag = 0
					ans = ans | (np.uint64(a[i]+1) << np.uint64(curr))
					score+=np.power(2,a[i]+1)
					#print a[i]+1,
					curr+=4
				else:
					#print last,
					ans = ans | (np.uint64(last) << np.uint64(curr))
					last = a[i]
					curr+=4
	if flag == 1:
		#print last,
		ans = ans | (np.uint64(last) << np.uint64(curr))

	return ans,score						

def transpose(board):

	ans = np.uint64(0)
	for i in range(4):
		for j in range(4):
			value = board & (np.uint64(15))
			board = board >> np.uint64(4)
			ans = ans | (value << np.uint64((j*4+i)*4))
	return ans	

def prrint(a):
	curr = 16
	for i in range(4):
		curr-=4
		print a & np.uint64(15),
		a = a >> np.uint64(4)

def isSorted(a):
	b = a
	flag = 0		

	for i in range(0,len(b)-1):
		if b[i]>=b[i+1]:
			continue
		else:
			flag = 1
			break

	if not flag:
		return 1	

	flag = 0		
	for i in range(0,len(b)-1):
		if b[i]<=b[i+1]:
			continue
		else:
			flag = 1
			break
	if not flag:
		return 1	
	
	return 0	

def allMoves():

	leftmoves = {}
	rightmoves = {}
	tpose = {}
	leftscores = {}
	rightscores = {}
	leftscores = {}
	monoticity = {}
	key = np.uint64(0)
	test = []
	for i in range(15):
		for j in range(15):
			for k in range(15):
				for l in range(15):
						key = np.uint64(0)
						key = key | (np.uint64(l))
						key = key | (np.uint64(k) << np.uint64(4))
						key = key | (np.uint64(j) << np.uint64(8))
						key = key | (np.uint64(i) << np.uint64(12))
						#print i,j,k,l,"--->",
						value,score = left([i,j,k,l])
						leftmoves[key] = value
						leftscores[key] = score
						monoticity[key] = isSorted([i,j,k,l])
						#print monoticity[key]
						value,score = right([i,j,k,l])
						rightmoves[key] = value
						rightscores[key] = score
						#print score
						tpose[key] = transpose(key)



	return leftmoves,rightmoves,tpose,leftscores,rightscores,monoticity
			