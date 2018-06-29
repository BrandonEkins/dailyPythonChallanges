def blankboard(size):
	board = []
	for i in range(size):
		board.append([])
		for t in range(size):	
			board[i].append(0)	
	return board
 
def checkConstraints(x,y,number,board):
	if x < 0 or x > 8 or y < 0 or y > 8:
		return False
	if number in board[x]:
		return False
	if number in board[:][y]:
		return False
	if board[x][y] != 0:
		return False
	if x < 4:
		if y < 4:
			for l in board[:3]:
				if number in l[:3]:
					return False
		elif y > 4 and y < 7:
			for l in board[:3]:
				if number in l[3:-3]:
					return False
		elif y > 6:
			for l in board[:3]:
				if number in l[6:]:
					return False
	elif x > 4 and x < 7:
		if y < 4:
			for l in board[:3]:
				if number in l[:3]:
					return False
		elif y > 4 and y < 7:
			for l in board[:3]:
				if number in l[3:-3]:
					return False
		elif y > 6:
			for l in board[:3]:
				if number in l[6:]:
					return False
	elif x > 6:
		if y < 4:
			for l in board[:3]:
				if number in l[:3]:
					return False
		elif y > 4 and y < 7:
			for l in board[:3]:
				if number in l[3:-3]:
					return False
		elif y > 6:
			for l in board[:3]:
				if number in l[6:]:
					return False
	return True
def recurse(x,y,number,board):
	
	if(checkConstraints(x+1,y+2,number,board)):
		board[x+1][y+2]=number
		print board
		recurse(x+1,y+2,9,board)
	if(checkConstraints(x+2,y+1,number,board)):
		board[x+2][y+1]=number
		recurse(x+2,y+1,9,board)
	if(checkConstraints(x-1,y+2,number,board)):
		board[x-1][y+2]=number
		recurse(x-1,y+2,9,board)
	if(checkConstraints(x-2,y+1,number,board)):
		board[x-2][y+1]=number
		recurse(x-2,y+1,9,board)
	if(checkConstraints(x-1,y-2,number,board)):
		board[x-1][y-2]=number
		recurse(x-1,y-2,9,board)
	if(checkConstraints(x-2,y-1,number,board)):
		board[x-2][y-1]=number
		recurse(x-2,y-1,9,board)
	if(checkConstraints(x+2,y-1,number,board)):
		board[x+2][y-1]=number
		recurse(x+2,y-1,9,board)	
	if(checkConstraints(x+1,y-2,number,board)):
		board[x+1][y-2]=number
		recurse(x+1,y-2,9,board)
	if(number-1 < 0):
		return board
	else:
		recurse(x,y,number-1,board)
		
def main():
	board = blankboard(9)
	board[1][1] = 9
	board = recurse(1,1,9,board)
	print(board)
main()
