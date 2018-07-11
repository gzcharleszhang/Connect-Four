import numpy as np

# Set starting conditions
board = np.zeros((6, 7))
game_on = True
player = 1
pieces_in_board = 0
FULL = 42 # 6 rows x 7 cols

def check_horizontals(player):
    for y in range(6):
        for x in range(4):
            if all(z == player for z in board[y][x: (x + 4)]):
                return False
    return True


def check_verticals(player):
    for y in range(6):
        for x in range(3):
            k = [board[x][y], board[x + 1][y], board[x + 2][y], board[x + 3][y]]
            if all(z == player for z in k):
                return False
    return True

def check_diagonals(player):
    reverse_board = board.copy()
    for y in range(2):
        if y == 0:
            for i in range(3):
                for x in range(4):
                    diagonals = [board[i][x], board[i+1][x+1],board[i+2][x+2], board[i+3][x+3]]
                    if all(z == player for z in diagonals):
                        return False

        elif y == 1:
            for i in range(len(reverse_board)):
                reverse_board[i] = list(reversed(reverse_board[i]))
            for i in range(3):
                for x in range(4):
                    diagonals = [reverse_board[i][x], reverse_board[i+1][x+1],reverse_board[i+2][x+2], reverse_board[i+3][x+3]]
                    if all(z == player for z in diagonals):
                        return False

    return True

def check_win(player):
    return check_horizontals(player) and check_verticals(player) and check_diagonals(player)


def insert_piece(player, y):
    global pieces_in_board
    done = False
    if pieces_in_board == FULL:
        return False, 0
    elif board[0][y] != 0:
        print("Column " + str(y + 1) + " is already filled")
        return True, player
    for x in range(5, -1, -1):
        if not done and (board[x, y] != 1 and board[x, y] != 2):
            if player == 1:
                board[x][y] = 1
                condition = check_win(player)
                if condition:
                    player = 2
            else:
                board[x][y] = 2
                condition = check_win(player)
                if condition:
                    player = 1

            pieces_in_board += 1
            #print(pieces_in_board)
            return condition, player


def main(player, game_on):
    while game_on:
        print(board,end="\n")
        user_input = eval(input("Player " + str(player) + "'s Turn. Enter a number from 1 to 7.\n"))
        while type(user_input) != int or user_input - 1 > 6 or user_input - 1 < 0:
            user_input = eval(input("INVALID INPUT: Enter a integer between 1 and 7\n"))

        update_status = insert_piece(player, user_input - 1)
        player = update_status[1]
        game_on = update_status[0]
    print(board, end="\n")
    if player == 0:
        print("It's a tie!")
    else:
        print("Player " + str(player) + " Wins!")

main(player, game_on)