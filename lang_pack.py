def messages(pack, i):
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
    return messages_dic[pack][i]
