import random

turn = 1
turn_number = 0
game_is_on = True
places = [0, 1, 2, 3, 4, 5, 6, 7, 8]
game_over = False


def check_end_game(board):

    if any(type(spot) == int for spot in board):
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            return True
        elif board[3] == "X" and board[4] == "X" and board[5] == "X":
            return True
        elif board[6] == "X" and board[7] == "X" and board[8] == "X":
            return True
        elif board[0] == "X" and board[3] == "X" and board[6] == "X":
            return True
        elif board[1] == "X" and board[4] == "X" and board[7] == "X":
            return True
        elif board[2] == "X" and board[5] == "X" and board[8] == "X":
            return True
        elif board[0] == "X" and board[4] == "X" and board[8] == "X":
            return True
        elif board[6] == "X" and board[4] == "X" and board[2] == "X":
            return True
        elif board[0] == "O" and board[1] == "O" and board[2] == "O":
            return False
        elif board[3] == "O" and board[4] == "O" and board[5] == "O":
            return False
        elif board[6] == "O" and board[7] == "O" and board[8] == "O":
            return False
        elif board[0] == "O" and board[3] == "O" and board[6] == "O":
            return False
        elif board[1] == "O" and board[4] == "O" and board[7] == "O":
            return False
        elif board[2] == "O" and board[5] == "O" and board[8] == "O":
            return False
        elif board[0] == "O" and board[4] == "O" and board[8] == "O":
            return False
        elif board[6] == "O" and board[4] == "O" and board[2] == "O":
            return False
    else:
        return "draw"


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

    if number_turn > 0:
        ai_plays = []
        player_plays = []
        for ind, spot in enumerate(board):
            if spot == "O":
                ai_plays.append(ind)
        for ind, spot in enumerate(board):
            if spot == "X":
                player_plays.append(ind)

        if all(plays in player_plays for plays in [0, 1]):
            if 2 not in ai_plays:
                board[2] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [0, 2]):
            if 1 not in ai_plays:
                board[1] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [1, 2]):
            if 0 not in ai_plays:
                board[0] = "O"
            else:
                board[random.choice(possible_choices)] = "O"

        elif all(plays in player_plays for plays in [3, 4]):
            if 5 not in ai_plays:
                board[5] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [3, 5]):
            if 4 not in ai_plays:
                board[4] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [4, 5]):
            if 3 not in ai_plays:
                board[3] = "O"
            else:
                board[random.choice(possible_choices)] = "O"

        elif all(plays in player_plays for plays in [6, 7]):
            if 8 not in ai_plays:
                board[8] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [6, 8]):
            if 7 not in ai_plays:
                board[7] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [7, 8]):
            if 6 not in ai_plays:
                board[6] = "O"
            else:
                board[random.choice(possible_choices)] = "O"

        elif all(plays in player_plays for plays in [0, 4]):
            if 8 not in ai_plays:
                board[8] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [0, 8]):
            if 4 not in ai_plays:
                board[4] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [4, 8]):
            if 0 not in ai_plays:
                board[0] = "O"
            else:
                board[random.choice(possible_choices)] = "O"

        elif all(plays in player_plays for plays in [6, 4]):
            if 2 not in ai_plays:
                board[2] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [6, 2]):
            if 4 not in ai_plays:
                board[4] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [2, 4]):
            if 6 not in ai_plays:
                board[6] = "O"
            else:
                board[random.choice(possible_choices)] = "O"

        elif all(plays in player_plays for plays in [0, 3]):
            if 6 not in ai_plays:
                board[6] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [0, 6]):
            if 3 not in ai_plays:
                board[3] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [3, 6]):
            if 6 not in ai_plays:
                board[0] = "O"
            else:
                board[random.choice(possible_choices)] = "O"

        elif all(plays in player_plays for plays in [1, 4]):
            if 7 not in ai_plays:
                board[7] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [1, 7]):
            if 4 not in ai_plays:
                board[4] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [4, 7]):
            if 1 not in ai_plays:
                board[1] = "O"
            else:
                board[random.choice(possible_choices)] = "O"

        elif all(plays in player_plays for plays in [2, 5]):
            if 8 not in ai_plays:
                board[8] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [2, 8]):
            if 5 not in ai_plays:
                board[5] = "O"
            else:
                board[random.choice(possible_choices)] = "O"
        elif all(plays in player_plays for plays in [5, 8]):
            if 2 not in ai_plays:
                board[2] = "O"
            else:
                board[random.choice(possible_choices)] = "O"

        print(ai_plays)
        print(player_plays)


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
            game_over = True
            pass
        elif check_end_game(places) is False:
            print("You lost.")
            game_over = True
            pass
        elif check_end_game(places) == "draw":
            print("That's a draw.")
            game_over = True
            pass
        if turn == 1 and not game_over:
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

        elif turn == -1 and not game_over:
            ia_turn(places, turn_number)
            turn *= -1
            turn_number += 1
