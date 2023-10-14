from nim_logic import Setup


def main():
    s = Setup()
    s.setup_language()
    type_of_game = s.setup_game()
    computer_score = 0
    player_score = 0
    if type_of_game == 1:
        winner = s.game()
        if winner == 2:
            print(s.messages(19))  # Tells who won
        elif winner == 1:
            print(s.messages(20))  # Tells who won
    else:
        match = 1
        while match < 4:
            winner = s.game()
            if winner == 2:
                print(s.messages(19))  # Tells who won this match
                computer_score += 1
            elif winner == 1:
                print(s.messages(20))  # Tells who won this match
                player_score += 1
            match += 1
            if computer_score == 2:
                print(s.messages(21))  # Tells who won the Bo3
                break
            elif player_score == 2:
                print(s.messages(22))  # Tells who won the Bo3
                break
            print(match, s.messages(23))  # Informs next match will start soon


if __name__ == "__main__":
    main()
