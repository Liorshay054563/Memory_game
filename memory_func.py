


def print_board(none_board):

    print(none_board[0:4])
    print(none_board[4:8])

def player_turn(board_one,none_board,playerT,player_a,player_b,pick):
    while len(set(none_board)) != 1:

        #player_pic(board_one,playerT,none_board)
        #pick1, pick2 = player_pic(board_one)
        pick1 = valid_input(pick, board_one,none_board)
        print(board_one[pick1])
        pick2 = valid_input(pick, board_one,none_board)
        print(board_one[pick2])
        if board_one[pick1] == board_one[pick2]:
            print("Well play, go again")
            none_board[pick1] = "[]"
            none_board[pick2] = "[]"
            print_board(none_board)
            if playerT:
                player_a += 1
                player_b += 0
            else:
                player_b += 1
                player_a += 0
            player_turn(board_one, none_board, playerT, player_a, player_b, pick)
            return player_a , player_b

        print_board(none_board)
        break



def valid_input(pick,board,none_board):
    while True:
        pick = int(input("Choose your [card] in the board by pick a number: "))
        if pick > len(board) or pick < 0 or none_board[pick] == "[]" :
            print("your choose is not on board, please choose again")
        else:
            return pick

def check_cards():
    pass
# def player_pic(board_one):
#     pick1 = int(input("Choose cARD in board: "))
#     valid_input(pick1, board_one)
#     pick2 = int(input("Choose second cARD in board: "))
#     valid_input(pick2, board_one)
#     print(board_one[pick1], board_one[pick2])
#     return pick1,pick2




