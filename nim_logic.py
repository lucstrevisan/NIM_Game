class Setup:
    def __init__(self):
        self.lang = 0
        self.d_lang = 0

    def setup_language(self):
        while self.lang not in [1, 2]:
            self.lang = int(
                input(
                    (
                        "Choose your language/Escolha seu idioma \n 1. English \n 2. Português (Brasil) "
                    )
                )
            )
            if self.lang in [1, 2]:
                self.d_lang = self.language(self.lang)
                return self.lang
            else:
                print("Type a valid number (1. for English, 2. for Português (Brasil))")
                print(
                    "Digite um número válido (1 para English, 2. para Português (Brasil))"
                )

    def language(self, pack):
        if pack == 1:
            return "en_us"
        elif pack == 2:
            return "pt_br"

    def setup_game(
        self,
    ):  # This function will ask if it will be a single match or a best of three
        print(self.messages(0))  # This will welcome player
        print(self.messages(1))
        type_of_game = 0
        while type_of_game not in [1, 2]:
            type_of_game = int(input(self.messages(2)))  # Ask if want best of 1 or 3
            if type_of_game == 1:
                print(self.messages(3))  # Indicates the type chosen
                return type_of_game
            elif type_of_game == 2:
                print(self.messages(4))  # Indicates the type chosen
                return type_of_game
            else:
                print(self.messages(5))  # Error message

    def computer_move(
        self, pieces, pieces_per_round, order
    ):  # This function will calculate computer's move
        n_now = pieces  # Verify how many pieces are in game at the moment
        if n_now >= pieces_per_round:
            play = pieces_per_round  # If there's no good number, the max one will be played
        else:
            play = n_now
            print(
                self.messages(6),
                play,
                self.messages(7),
                n_now - play,
                self.messages(8),
            )  # Tells computer's move
            next_player = self.next_to_play(order)
            return play, next_player
        trick_to_win = n_now - play
        verify_trick = trick_to_win % (pieces_per_round + 1)
        while (verify_trick != 0) and (
            play > 1
        ):  # This while-loop will try to find the best number to play
            trick_to_win = n_now - play
            verify_trick = trick_to_win % (pieces_per_round + 1)
            if verify_trick == 0:
                print(
                    self.messages(6),
                    play,
                    self.messages(7),
                    n_now - play,
                    self.messages(8),
                )  # Tells computer's move
                next_player = self.next_to_play(order)
                return play, next_player
            else:
                play -= 1
            if play == 1:
                if n_now >= pieces_per_round:
                    play = pieces_per_round
                    print(
                        self.messages(6),
                        play,
                        self.messages(7),
                        n_now - play,
                        self.messages(8),
                    )  # Tells computer's move
                    next_player = self.next_to_play(order)
                    return play, next_player
                else:
                    play = pieces_per_round
                    print(
                        self.messages(6),
                        play,
                        self.messages(7),
                        n_now - play,
                        self.messages(8),
                    )  # Tells computer's move
                    next_player = self.next_to_play(order)
                    return play, next_player
        next_player = self.next_to_play(order)
        print(
            self.messages(6),
            play,
            self.messages(7),
            n_now - play,
            self.messages(8),
        )  # Tells computer's move
        return play, next_player

    def player_move(
        self, pieces, pieces_per_round, order
    ):  # This function will validate player's move
        play = 0
        next_player = self.next_to_play(order)
        while (play <= 0) or (play > pieces_per_round):
            play = int(input(self.messages(9)))  # Ask for player's move
            if (play != 0) and (play <= pieces_per_round):
                print(
                    self.messages(10), pieces - play, self.messages(8)
                )  # Tells board state
                return play, next_player
            elif (pieces - play) < 0:
                print(self.messages(11))  # Error message
            else:
                print(self.messages(12))  # Error message

    def board_now(
        self, pieces, play
    ):  # This function will calculate the state of the board
        n_after = pieces - play
        return n_after

    def next_to_play(self, order):  # This function will calculate next person to play
        if order == 1:
            next_player = 2
        elif order == 2:
            next_player = 1
        return next_player

    def game(self):
        print(self.messages(13))
        pieces = 0  # Number of pieces in NIM game
        pieces_per_round = 0  # Max number each player can remove per play
        while (pieces_per_round > pieces) or (pieces < 3) or (pieces_per_round == 0):
            pieces = int(input(self.messages(14)))  # Asks for N number
            pieces_per_round = int(input(self.messages(15)))  # Asks for M number
            if (pieces_per_round > pieces) or (pieces < 3) or (pieces_per_round == 0):
                print(self.messages(16))  # Error message
            else:
                break
        board = pieces
        if (
            pieces % (pieces_per_round + 1) == 0
        ):  # Computer will be using this trick to try to always win
            print(self.messages(17))  # Says players will be first to play
            order = 1  # Player number will be 1
        else:
            print(self.messages(18))  # Says computer will be first to play
            order = 2  # Computer number will be 2

        while board > 0:
            if order == 2:
                play, order = self.computer_move(board, pieces_per_round, order)
                board = self.board_now(board, play)
                if board == 0:
                    winner = 2
                    return winner
            else:
                play, order = self.player_move(board, pieces_per_round, order)
                board = self.board_now(board, play)
                if board == 0:
                    winner = 1
                    return winner

    def messages(self, i):
        messages_dic = {
            "en_us": [
                "Hello, this is a Nim Game!",
                "First choose what kind of game you want:\n 1. Single match.\n 2. Best of three",
                "Type the kind of game you want: ",
                "You chose Single match!",
                "You chose Best of three",
                "Please type a valid number (1 or 2).",
                "Computer removed",
                "pieces. Now there is",
                "in game!",
                "Type your play: ",
                "Now there is",
                "Type a valid number (Board cannot be lower than 0)",
                "Type a valid number (1 or higer, M or lower).",
                "This match will start now, think carefully and good luck!",
                "Now choose how many pieces: ",
                "Now choose pieces limit per player: ",
                "Please type a valid number (Minimal 3 pieces (N) and pieces limit per player (M) must be 1 or higher, M must not be higher than N)",
                "You can start playing!",
                "Computer starts!",
                "Computer won! Good luck next time!",
                "Congratulations, you won!",
                "Computer won Best of three! Try harder next time",
                "Congratulaions, you won the Best of three!",
                "º match will be starting soon!",
            ],
            "pt_br": [
                "Olá, este é um jogo do Nim!",
                "Primeiro escolha o tipo de jogo que você quer :\n 1. Melhor de 1.\n 2. Melhor de 3",
                "Digite o tipo de jogo que você quer: ",
                "Você escolheu melhor de 1!",
                "Você escolheu melhor de 3!",
                "Por favor digite um número válido (1 ou 2)",
                "O computador removeu",
                "peças. Agora há",
                "no jogo!",
                "Digite sua jogada: ",
                "Agora há",
                "Digite um número válido (A mesa não pode ser menor que 0)",
                "Digite um número válido (1 ou maior, M ou menor).",
                "A partida iniciará agora, pense com cuidado e boa sorte!",
                "Agora escolha quantas peças: ",
                "Agora escolha o limite de peças removidas por jogador: ",
                "Digite um número válido (Mínimo de 3 peças (N) e limite de peças por jogador (M) deve ser 1 or maior, M não pode ser maior que N)",
                "Você pode começar jogando!",
                "O computador inicia!",
                "O computador ganhou! Boa sorte na próxima!",
                "Parabéns, você ganhou!",
                "O computador venceu a melhor de 3! Jogue melhor na próxima!",
                "Parabéns, você ganhou a melhor de #!",
                "º partida iniciará em instantes!",
            ],
        }
        return messages_dic[self.d_lang][i]
