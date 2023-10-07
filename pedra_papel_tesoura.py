from biblioteca import *
#variaveis para o laço
pedra = "pedra"
papel = "papel"
tesoura = "tesoura"
perg = "sS"

#laço de repetição do jogo
while perg in "sS":
    jogada1 = input("jogador 1 insira a sua jogada (pedra , papel ou tesoura:)")

    #laço caso a jogada1 seja escrita errada
    while jogada1 != pedra and jogada1 != papel and jogada1 != tesoura:
        jogada1 = input("error na digitação da jogada 1. insira pedra , papel ou tesoura:")

    jogada2 = input("jogador 2 insira a sua jogada (pedra papel ou tesoura:)")

    #laço caso a jogada2 seja escrita errada
    while jogada2 != pedra and jogada2 != papel and jogada2 != tesoura:
        jogada2 = input("error na digitação da jogada 2. insira pedra , papel ou tesoura:")

    #resultado para cada variação do jogo, importado da função dentro da biblioteca
    pedra_papel_tesoura(jogada1=jogada1, jogada2=jogada2)

    #pergunta se usuario quer jogar novamente
    perg = input("Deseja (digite 's' para) jogar novamente ? ")
    print()
else:
    #caso o usuario nao queira mais jogar
    print("Jogo Finalizado. Obrigado por jogar")
