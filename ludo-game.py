import random

#Board size
board = [" "] * 52

player1 = input("Enter a name of player 1: ")
player2 = input("Enter a name of player 2: ")

player1_position = 0
player2_position = 0

def roll_dice():
    return random.randint(1,6)

def move_player(player_position, steps):
    player_position += steps
    if player_position > 51:
        player_position -=52
    return player_position

#while loop
while True:
    input(f"{player1}, press enter to roll the dice: ")
    result =roll_dice()    
    print(f"{player1} rolled a , {result}") 



