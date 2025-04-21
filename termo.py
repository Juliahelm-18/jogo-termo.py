#Para iniciar vou utilizar os prints, mostrando as regras

nome = input("Digite seu nome para iniciarmos o jogo: ")
print(f"Bem vindo {nome} antes de iniciar o jogo vamos lhe mostrar as regras: ")
print("- Você deve escolher a dificuldade do jogo, se serão palavras de 5, 6 ou 7 letras; ")
print("- As tentativas são relacionadas com a quantidade de letras, ou seja, 5, 6 ou 7 tentativas; ")
print("- Após o palpite o jogo irá mostrar onde ocorreram acertos e se as letras existem na palavra; ")
print("- O jogo terminará quando você acertar ou quando não houver mais tentativas. ")
print("Vamos iniciar o jogo termo.py!")

#Para começar o jogo o jogador deve decidir qual a quantidade de letras a palavra secreta deve conter

quantidade = int(input("Qual a dificuldade você gostaria de jogar, 5, 6 ou 7 letras? "))

import random
#O import random serve para conseguir utilizar o random.choice

if quantidade == 5:
    tentativa = 0
    #Variavel para conseguir contar as tentativas do jogador
    while tentativa <= 5:
        #Esse while é para funcionar até que o jogador atinja o maximo de tentativas
        cinco = ["nuvem", "poder", "diabo", "nesta", "arara"]
        palavra_secreta = random.choice(cinco)
        #A palavra secreta será sorteada através do random.choice
        
        palpite = input("Digite seu primeiro palpite para adivinhar a palavra secreta: ")
        
        if len(palpite) > 5 and len(palpite) < 5
            print("A palavra nao se encaixa em cinco letras, tente novamente.")
            palpite = input("Digite seu primeiro palpite para adivinhar a palavra secreta: ")
        #Este if servirá caso o jogador digite uma palavra menor ou maior que a quantidade de letras escolhida

        if palpite == palavra_secreta:
            print("Parabéns você acertou a palavra secreta!")
        #Caso o jogador acerte de primeira



            

import random
#Para o random.choice funcionar
if quantidade == 6:
    tentativa = 0

    while tentativa <= 6:
         #While para funcionar até que o jogador utilize o número máximo de tentativas
         seis = ["utopia", "casual", "hostil", "anseio", "gentil"]
         palavra_secreta = random.choice(seis)
         #A palavra secreta será sorteada através do random.choice
        
        palpite = input("Digite seu primeiro palpite para adivinhar a palavra secreta: ")
        
        if len(palpite) > 6 and len(palpite) < 6
            print("A palavra nao se encaixa em seis letras, tente novamente.")
            palpite = input("Digite seu primeiro palpite para adivinhar a palavra secreta: ")
        #Este if servirá caso o jogador digite uma palavra menor ou maior que a quantidade de letras escolhida

        if palpite == palavra_secreta:
            print("Parabéns você acertou a palavra secreta!")
        #Caso o jogador acerte de primeira
        elif palpite != palavra_secreta:
            tentativa += 1

import random
#Para o random.choice funcionar
if quantidade == 7:
    tentativa = 0

    while tentativa <= 7:
         #While para funcionar até que o jogador utilize o número máximo de tentativas
         sete = ["mochila", "lasanha", "cozinha", "atacado", "alergia"]
         palavra_secreta = random.choice(sete)
         #A palavra secreta será sorteada através do random.choice
        
        palpite = input("Digite seu primeiro palpite para adivinhar a palavra secreta: ")
        
        if len(palpite) > 7 and len(palpite) < 7
            print("A palavra nao se encaixa em sete letras, tente novamente.")
            palpite = input("Digite seu primeiro palpite para adivinhar a palavra secreta: ")
        #Este if servirá caso o jogador digite uma palavra menor ou maior que a quantidade de letras escolhida

        if palpite == palavra_secreta:
            print("Parabéns você acertou a palavra secreta!")
        #Caso o jogador acerte de primeira
        elif palpite != palavra_secreta:
            tentativa += 1


    