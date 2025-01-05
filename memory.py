# Memory Game
from memory_func import *

board_one = ['a','b','c','d','a','b','c','d']

none_board = [f"[{i}]" for i in range(len(board_one))]

player_a_name = input("Enter first player: ")
player_b_name = input("Enter second player: ")
player_a = 0
player_b = 0
pick = None
playerT = True
while len(set(none_board)) != 1: #len(set(none_board)) != 1:

    print_board(none_board)
    if playerT :
        print(f"{player_a_name} turn ")
    else:
        print(f"{player_b_name} turn ")
    score_first, score_second = player_turn(board_one, none_board, playerT,player_a,player_b,pick)
    player_a += score_first
    player_b += score_second
    print(f"player {player_a_name} = {player_a} ")  # {score_first}")
    print(f"player {player_b_name} = {player_b} ")  # {score_second}")
    playerT = not playerT
print(f"player {player_a_name} = {player_a} ")#{score_first}")
print(f"player {player_b_name} = {player_b} ")#{score_second}")
print("game over")





#input 2 players name
# show them the unsolve board card
# player 'a' turn , pick up card and show it
# player 'a' turn , pick up  a second card and show it
# if cards same ,add 1 to score player, give another turn, remove the card from board
# now same player "b"....
# finish when no cards left on board
# count who's player score more