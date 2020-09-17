QUEENS = 10

def gradient_search(board):
    best_attack = (1000,1000)
    better = True
    best_board = []
    new_board =[]

    while better:
        #find best board with fewest attacks
        for queen in range(QUEENS):
            new_board = copy_board(board)
            new_attack = best_permutations(queen, new_board) #gives you new board

            if new_attack[1] < best_attack[1]:
                best_attack = new_attack
                best_board = new_board

        if best_attack[1] < calc_attacks(board):
            #update board
            for i in range(QUEENS):
                for g in range(QUEENS):
                    board[i][g] = best_board[i][g]

            better = True
        else:
            better = False

    if calc_attacks(board) == 0:
        return True
    else:
        return False


def best_permutations(queen_num, new_board):
    best_attack = 1000
    best_row = 0

    #find queen and reset
    for y in range(QUEENS):
        if new_board[y][queen_num] == 1:
            new_board[y][queen_num] = 0
            original = y
            break

    #try every row and get best row for queen
    for y in range(QUEENS):
        new_board[y][queen_num] = 1
        curr_attack = calc_attacks(new_board)

        if curr_attack < best_attack:
            best_attack = curr_attack
            best_row = y
        elif best_attack == curr_attack:
            best_row = min(y,best_row)

        new_board[y][queen_num] = 0


    new_board[best_row][queen_num] = 1

    best = (best_row,best_attack)
    return best


def calc_attacks(some_board):
    num_attacks = 0
    for x in range(QUEENS):
        #find queen in that column
        for y in range(QUEENS):
            if some_board[y][x] == 1:

                #check ROW
                for i in range(QUEENS):
                        if some_board[y][i] == 1 and i != x:
                            num_attacks = num_attacks + 1

                #check DIAGONALS
                for i in range(QUEENS):
                        if x+i < 10 and y+i < 10 and i != 0 and some_board[y+i][x+i] == 1:
                            num_attacks = num_attacks + 1
                        if x-i >= 0 and y+i < 10 and i != 0 and some_board[y+i][x-i] == 1:
                            num_attacks = num_attacks + 1
                        if x-i >= 0 and y-i >= 0 and i != 0 and some_board[y-i][x-i] == 1:
                            num_attacks = num_attacks + 1
                        if x+i < 10 and y-i >= 0 and i != 0 and some_board[y-i][x+i] == 1:
                            num_attacks = num_attacks + 1
    return num_attacks

def copy_board(board):
    copied_board = [[4 for i in range(QUEENS)] for j in range(QUEENS)]
    for x in range(QUEENS):
        for y in range(QUEENS):
            copied_board[y][x] = board[y][x]

    return copied_board
