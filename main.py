import random

turn = 1
turn_number = 0
game_is_on = True
places = [0, 1, 2, 3, 4, 5, 6, 7, 8]
game_over = False


def check_end_game(check):
    if check[0] == "X" and check[1] == "X" and check[2] == "X":
        return True
    elif check[3] == "X" and check[4] == "X" and check[5] == "X":
        return True
    elif check[6] == "X" and check[7] == "X" and check[8] == "X":
        return True
    elif check[0] == "X" and check[3] == "X" and check[6] == "X":
        return True
    elif check[1] == "X" and check[4] == "X" and check[7] == "X":
        return True
    elif check[2] == "X" and check[5] == "X" and check[8] == "X":
        return True
    elif check[0] == "X" and check[4] == "X" and check[8] == "X":
        return True
    elif check[6] == "X" and check[4] == "X" and check[2] == "X":
        return True
    elif check[0] == "O" and check[1] == "O" and check[2] == "O":
        return False
    elif check[3] == "O" and check[4] == "O" and check[5] == "O":
        return False
    elif check[6] == "O" and check[7] == "O" and check[8] == "O":
        return False
    elif check[0] == "O" and check[3] == "O" and check[6] == "O":
        return False
    elif check[1] == "O" and check[4] == "O" and check[7] == "O":
        return False
    elif check[2] == "O" and check[5] == "O" and check[8] == "O":
        return False
    elif check[0] == "O" and check[4] == "O" and check[8] == "O":
        return False
    elif check[6] == "O" and check[4] == "O" and check[2] == "O":
        return False


def print_table(table):
    print(f"""
         {table[0]} | {table[1]} | {table[2]} 
        ___|___|___
         {table[3]} | {table[4]} | {table[5]}  
        ___|___|___
         {table[6]} | {table[7]} | {table[8]} 
           |   |       
    """)


def ia_turn(board, number_turn):
    print("AI's turn:")

    possible_choices = []
    for spot in board:
        if spot != "X" and spot != "O":
            possible_choices.append(spot)
    if number_turn == 0:
        print("turn = 0")
        ia_choice = random.choice(possible_choices)
        for spot in board:
            if spot == ia_choice:
                board[spot] = "O"

    if turn > 0:
        ai_plays = []
        for i, spot in enumerate(board):
            if spot == "O":
                ai_plays.append(spot)


while game_is_on:

    if game_over:
        play_again = input("Would you like to play again? Y/N\n")
        if play_again.lower() == "n":
            game_is_on = False
        elif play_again.lower() == "y":
            places = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            turn_number = 0
            turn = 1
            game_over = False

    else:
        print_table(places)
        if check_end_game(places):
            print("You won.")
        elif check_end_game(places) is False:
            print("You lost.")
        if turn == 1:
            choice = input(f"Choose your play:\n{places}\n")
            if not choice.isdigit():
                print("your choice is not valid, choose another one.")
            elif int(choice) >= 9:
                print("your choice is not valid, choose another one.")
            elif int(choice) not in places:
                print("your choice is not valid, choose another one.")
            else:
                for i, place in enumerate(places):
                    if place == int(choice):
                        places[i] = "X"
                        turn *= -1

        elif turn == -1:
            ia_turn(places, turn_number)
            turn *= -1
            turn_number += 1
