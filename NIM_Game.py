def setup_game():  # This function will ask if it will be a single match or a best of three
    print("Hello, this is a NIM Game")
    print(
        "First choose what kind of game you want:\n 1. Single match.\n 2. Best of three"
    )
    type_of_game = None
    while type_of_game != 1 or 2:
        type_of_game = int(input("Type the kind of game you want: "))
        if type_of_game == 1:
            print("You chose Single match!")
            return type_of_game
        elif type_of_game == 2:
            print("You chose Best of three!")
            return type_of_game
        else:
            print("Please type a valid number (1 or 2).")


def computer_move(n, m, order):  # This function will calculate computer's move
    n_now = n  # Verify how many pieces are in game at the moment
    if n_now >= m:
        play = m  # If there's no good number, the max one will be played
    else:
        play = n_now
        print(
            "Computer removed", play, "pieces. Now there is", n_now - play, "in game!"
        )
        next_player = next_to_play(order)
        return play, next_player
    trick_to_win = n_now - play
    verify_trick = trick_to_win % (m + 1)
    while (verify_trick != 0) and (
        play > 1
    ):  # This while-loop will try to find the best number to play
        trick_to_win = n_now - play
        verify_trick = trick_to_win % (m + 1)
        if verify_trick == 0:
            print(
                "Computer removed",
                play,
                "pieces. Now there is",
                n_now - play,
                "in game!",
            )
            next_player = next_to_play(order)
            return play, next_player
        else:
            play -= 1
    next_player = next_to_play(order)
    print("Computer removed", play, "pieces. Now there is", n_now - play, "in game!")
    return play, next_player


def player_move(n, m, order):  # This function will validate player's move
    play = 0
    next_player = next_to_play(order)
    while (play <= 0) or (play > m):
        play = int(input("Type your play: "))
        if ((play != 0) or (play <= m)) and not (play < 0) and not (play > m):
            print("Now there is", n - play, "in game!")
            return play, next_player
        elif (n - play) < 0:
            print("Type a valid number (Board cannot be lower than 0)")
        else:
            print("Type a valid number (1 or higer, M or lower).")


def board_now(n, play):  # This function will calculate the state of the board
    n_after = n - play
    return n_after


def next_to_play(order):  # This function will calculate next person to play
    if order == 1:
        next_player = 2
    elif order == 2:
        next_player = 1
    return next_player


def game():
    print("This match will start now, think carefully and good luck!")
    n = 0
    m = 0
    while (m > n) or (n < 3) or (m == 0):
        n = int(
            input("Now choose how many pieces: ")
        )  # "N" is the number of pieces in NIM game
        m = int(
            input("Now choose pieces limit per player: ")
        )  # "M" is the max number each player can remove per play
        if (m > n) or (n < 3) or (m == 0):
            print(
                "Please type a valid number (Minimal 3 pieces (N) and pieces limit per player (M) must be 1 or higher, M must not be higher than N)"
            )
        else:
            break
    board = n
    if n % (m + 1) == 0:  # Computer will be using this trick to try to always win
        print("You can start playing!")
        order = 1  # Player number will be 1
    else:
        print("Computer starts!")
        order = 2  # Computer number will be 2

    while board > 0:
        if order == 2:
            play, order = computer_move(board, m, order)
            board = board_now(board, play)
            if board == 0:
                winner = 1
                return winner
        elif order == 1:
            play, order = player_move(board, m, order)
            board = board_now(board, play)
            if board == 0:
                winner = 2
                return winner


type_of_game = setup_game()
computer_score = 0
player_score = 0
if type_of_game == 1:
    winner = game()
    if winner == 1:
        print("Computer won! Good luck next time!")
    elif winner == 2:
        print("Congratulations, you won!")
else:
    match = 1
    while match < 4:
        winner = game()
        if winner == 1:
            print("Computer won! Good luck next time!")
            computer_score += 1
        elif winner == 2:
            print("Congratulations, you won!")
            player_score += 1
        match += 1
        if computer_score == 2:
            print("Computer won Best of three! Try harder next time")
            break
        elif player_score == 2:
            print("Congratulaions, you won the Best of three!")
            break
        print(match, "º match will be starting soon!")
