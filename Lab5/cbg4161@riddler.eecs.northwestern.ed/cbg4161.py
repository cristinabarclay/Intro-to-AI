import common

def minmax_tictactoe(board, turn):

	if turn == common.constants.X:
		result = max_value(board)
		if result == 1:
			return 1
		elif result == -1:
			return 2
		else:
			return 0

	else:
		result = min_value(board)
		if result == 1:
			return 1
		elif result == -1:
			return 2
		else:
			return 0



def abprun_tictactoe(board, turn):

	if turn == common.constants.X:
		result = AB_max(board, float('-inf'), float('inf'))
		if result == 1:
			return 1
		elif result == -1:
			return 2
		else:
			return 0


	else:
		result = AB_min(board, float('-inf'), float('inf'))
		if result == 1:
			return 1
		elif result == -1:
			return 2
		else:
			return 0



#HELPERS
#ALPHA BETA PRUNING

def AB_max(board, alpha, beta):
	check = common.game_status(board)
	if check == 0 and isboardfull(board) == False:
		v = float('-inf')
		for y in range(3):
			for x in range(3):
				if common.get_cell(board, y ,x) == 0:
					common.set_cell(board,y, x, 1)
					v = max(v,AB_min(board, alpha, beta))
					common.set_cell(board,y, x, 0)
					if v >= beta:
						return v
					alpha = max(alpha,v)
		return v

	#gameover
	else:
		if check == 1:
			return 1
		elif check == 2:
			return -1
		else:
			return 0



def AB_min(board, alpha, beta):
	check = common.game_status(board)
	if check == 0 and isboardfull(board) == False:
		v = float('inf')
		for y in range(3):
			for x in range(3):
				if common.get_cell(board, y ,x) == 0:
					common.set_cell(board,y, x, 2)
					v = min(v,AB_max(board, alpha, beta))
					common.set_cell(board,y, x, 0)
					if v <= alpha:
						return v
					beta = min(beta,v)
		return v

	#gameover
	else:
		if check == 1:
			return 1
		elif check == 2:
			return -1
		else:
			return 0


#MINIMAX

def max_value(board):
	check = common.game_status(board)
	if check == 0 and isboardfull(board) == False:
		v = float('-inf')
		for y in range(3):
			for x in range(3):
				if common.get_cell(board, y ,x) == 0:
					common.set_cell(board,y, x, 1)
					v = max(v,min_value(board))
					common.set_cell(board,y, x, 0)

		return v

	#gameover
	else:
		if check == 1:
			return 1
		elif check == 2:
			return -1
		else:
			return 0

def min_value(board):
	check = common.game_status(board)
	if check == 0 and isboardfull(board) == False:
		v = float('inf')
		for y in range(3):
			for x in range(3):
				if common.get_cell(board, y ,x) == 0:
					common.set_cell(board,y, x, 2)
					v = min(v,max_value(board))
					common.set_cell(board,y, x, 0)
		return v

	#gameover
	else:
		if check == 1:
			return 1
		elif check == 2:
			return -1
		else:
			return 0

def isboardfull(board):
	for i in board:
		if i == 0:
			return False
	return True

def check(board):
	if common.game_status(board) == 1:
		return 1
	elif common.game_status(board) == 2:
		return -1
	else:
		return 0



#put your code here:
#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
#use the function common.game_status(board), to evaluate a board
#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
#the program will keep track of the number of boards evaluated
#result = common.game_status(board);
