x = "x"
circle = "O"
none = "_"
game_is_on = True
places = [0, 1, 2, 3, 4, 5, 6, 7, 8]
game_over = False


def print_table(table):
    print(f"""
         {table[0]} | {table[1]} | {table[2]} 
        ___|___|___
         {table[3]} | {table[4]} | {table[5]}  
        ___|___|___
         {table[6]} | {table[7]} | {table[8]} 
           |   |       
    """)


while game_is_on:
    print_table(places)
    choice = input(f"Choose your play:\n{places}\n")
    for i, place in enumerate(places):
        if place == int(choice):
            places[i] = "X"
        elif choice == "O":
            print("your choice is not valid, choose another one.")

    if places[0] == "X" and places[1] == "X" and places[2] == "X":
        print("You won!")
        game_over = True
    elif places[3] == "X" and places[4] == "X" and places[5] == "X":
        print("You won!")
        game_over = True
    elif places[6] == "X" and places[7] == "X" and places[8] == "X":
        print("You won!")
        game_over = True
    elif places[0] == "X" and places[3] == "X" and places[6] == "X":
        print("You won!")
        game_over = True
    elif places[1] == "X" and places[4] == "X" and places[7] == "X":
        print("You won!")
        game_over = True
    elif places[2] == "X" and places[5] == "X" and places[8] == "X":
        print("You won!")
        game_over = True
    elif places[0] == "X" and places[4] == "X" and places[8] == "X":
        print("You won!")
        game_over = True
    elif places[6] == "X" and places[4] == "X" and places[2] == "X":
        print("You won!")
        game_over = True
    if game_over:
        play_again = input("Would you like to play again? Y/N\n")
        if play_again.lower() == "n":
            game_is_on = False
