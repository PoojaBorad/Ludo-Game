import random

#Board size
board = [" "] * 52

player1 = input("Enter a name of player 1: ").capitalize()
player2 = input("Enter a name of player 2: ").capitalize()

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
    result = roll_dice()   
    print(f"{player1} rolled a : {result}")
    player1_position = move_player(player1_position, result)
    print(f"{player1} moved from {player1_position - result} to {player1_position} steps.")

    input(f"{player2}, press enter to roll the dice: ")
    result = roll_dice()    
    print(f"{player2} rolled a: {result} ")
    player2_position = move_player(player2_position, result) 
    print(f"{player2} moved from {player2_position - result} to {player2_position} steps.")

#Declare Winner
    if player1_position == 51:
      print(f"{player1} is a Winner!")
      break
    elif player2_position ==51:
      print(f"{player2} is a Winner!")
      break





