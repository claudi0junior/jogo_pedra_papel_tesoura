def pedra_papel_tesoura(jogada1,jogada2):
    pedra = "pedra"
    papel = "papel"
    tesoura = "tesoura"
    if jogada1 == pedra and jogada2 == pedra or jogada1 == papel and jogada2 == papel or jogada1 == tesoura and jogada2 == tesoura:
        print("Jogo Empatado para ambas as jogadas ")
    elif jogada1 == pedra and jogada2 == papel:
        print("Jogador 2 venceu")
    elif jogada1 == pedra and jogada2 == tesoura:
        print("Jogador 1 venceu")
    elif jogada1 == papel and jogada2 == pedra:
        print("Jogador 1 venceu")
    elif jogada1 == papel and jogada2 == tesoura:
        print("Jogador 2 venceu ")
    elif jogada1 == tesoura and jogada2 == pedra:
        print("Jogador 2 venceu")
    elif jogada1 == tesoura and jogada2 == papel:
        print("Jogador 1 venceu")