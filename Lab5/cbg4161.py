import common

#helpful, but not needed
class variables:
	counter=0


def sudoku_backtracking(sudoku):
	variables.counter = 0

	recursive_backtracking(sudoku)
	return variables.counter


def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	#intialize domain
	domain = [[[ 1 for i in range(10)] for j in range(9)] for k in range(9)] #is this correct 0-8, 0-8, 1-9
	for y in range(9):
		for x in range(9):
			for i in range (1,10):
				if common.can_yx_be_z(sudoku, y, x, i):
					domain[y][x][i] = 1
				else:
					domain[y][x][i] = 0

	recursive_forwardchecking(sudoku, domain)
	return variables.counter


def recursive_backtracking(sudoku):
	variables.counter += 1

	if isboardfull(sudoku):
		return True

	else:
		for y in range(9):
			for x in range(9):
				#find empty space
				if sudoku[y][x] == 0:
					for value in range(1,10):
						if common.can_yx_be_z(sudoku, y, x, value):
							sudoku[y][x] = value
							#if theres is a solution with that value
							if recursive_backtracking(sudoku):
								return True;
							else:
								#reset to original
								sudoku[y][x] = 0
					return False


def recursive_forwardchecking(sudoku,domain):
	variables.counter += 1

	if isboardfull(sudoku):
		return True

	else:
		for y in range(9):
			for x in range(9):
				#find empty space
				if sudoku[y][x] == 0:
					for value in range(1,10):
						if common.can_yx_be_z(sudoku, y, x, value):
							old_domain = copy_of(domain)
							#check domain
							sudoku[y][x] = value
							if update_domain(domain, sudoku, y, x, value):
							#if theres is a solution with that value
								if recursive_forwardchecking(sudoku, domain):
									return True
									#reset to original
							sudoku[y][x] = 0
							domain = copy_of(old_domain)
					return False



def isboardfull(sudoku):
	for y in range(9):
		for x in range(9):
			if sudoku[y][x] == 0:
				return False
	return True

def copy_of(domain):
	copy = [[[ 1 for i in range(10)] for j in range(9)] for k in range(9)]

	for y in range(9):
		for x in range(9):
			for z in range(1,10):
				copy[y][x][z] = domain[x][y][z]

	return copy

def update_domain(domain, sudoku, y, x, value):
	empty = 0
	for j in range(9):
		for i in range(9):
			if j == y or i == x or (int(j/3) == int(y/3) and int(i/3) == int(x/3)):
				if sudoku[j][i] == 0:
					domain[j][i][value] = 0
					domain_size = 0
					for n in range(1,10):
						#theres one valid
						if common.can_yx_be_z(sudoku, j, i, n):
							domain_size += 1
						else:
							domain[j][i][n]=0
					if domain_size == 0:
						empty += 1

	if empty == 0:
		return True
	else:
		return False
