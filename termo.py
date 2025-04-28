# Esse jogo é uma versão do jogo termo em python

import random  

#Para iniciar vou utilizar os prints, mostrando as regras do jogo, e pedindo o nome do jogador também
nome = input("Digite seu nome para iniciarmos o jogo: ")
print(f"Bem vindo {nome} antes de iniciar o jogo vamos lhe mostrar as regras: ")
print("- Você deve escolher a dificuldade do jogo, se serão palavras de 5, 6 ou 7 letras; ")
print("- As tentativas são relacionadas com a quantidade de letras, ou seja, 5, 6 ou 7 tentativas; ")
print("- Após o palpite o jogo irá mostrar onde ocorreram acertos e se as letras existem na palavra; ")
print("- O jogo terminará quando você acertar ou quando não houver mais tentativas. ")
print("Vamos iniciar o jogo termo.py!")

# Para começar o jogo o jogador deve decidir qual a quantidade de letras a palavra secreta deve conter
quantidade_letras = int(input("Qual a dificuldade você gostaria de jogar, 5, 6 ou 7 letras? "))
# A quantidade de letras escolhida pelo jogador será armazenada na variavel quantidade_letras

if quantidade_letras == 5:
    tentativa = 1
    # Variavel para conseguir contar as tentativas do jogador
    CINCO_LETRAS = ["nuvem", "poder", "diabo", "nesta", "nariz"]
    #Cinco letras é uma lista com palavras de 5 letras, que serão utilizadas para o jogo
    palavra_secreta = random.choice(CINCO_LETRAS)
    # A palavra secreta será sorteada através do random.choice
    letras_descobertas = ['_'] * 5
    # Essa variavel é uma lista que irá armazenar as letras que o jogador já acertou, e o '_' será utilizado para mostrar ao jogador as letras que ele ainda não acertou
    
    
    while tentativa <= 5:
        # Esse while é para funcionar até que o jogador atinja o número maximo de tentativas

         
        palpite = input("Digite seu palpite para adivinhar a palavra secreta: ").lower()
        # O palpite do jogador será armazenado na variavel palpite, e o .lower() serve para deixar a palavra em minusculo, caso o jogador digite em maiusculo

        if len(palpite) != 5:
            # O len serve para contar a quantidade de letras que o jogador digitou 
            print("A palavra nao se encaixa em cinco letras, tente novamente.")
            palpite = input("Digite seu primeiro palpite para adivinhar a palavra secreta: ")
        # Este if servirá caso o jogador digite uma palavra menor ou maior que a quantidade de letras escolhida e pede para digitar o palpite novamente para atualizar a variável

        if palpite == palavra_secreta:
            print("Parabéns você acertou a palavra secreta!")
        # Caso o jogador acerte de primeira
            break
        # O break serve para parar o loop, caso o jogador acerte a palavra secreta de primeira
        
        # Não coloquei if novamente, porque se não ocorrer de o jogador acertar de primeira já vai seguir o código
        resultado = ""
        # Variavel resultado será utilizada para armazenar o resultado do palpite do jogador, e depois imprimir na tela
        for i in range(5):
            if palpite[i] == palavra_secreta[i]:
                letras_descobertas[i] = palpite[i]
        # Essa linha irá verificar se a letra do palpite é igual a letra da palavra secreta, e se for igual irá armazenar na variavel palavra_vazia, que é uma lista que armazena as letras que o jogador já acertou

         # Mostrar letras que existem na palavra (mesmo se estiverem na posição errada)
        letras_ja_mostradas = set()
        # Essa linha irá criar um conjunto vazio, que será utilizado para armazenar as letras que já foram mostradas ao jogador, para não repetir as letras que já foram mostradas
        for letra in palpite:
            if letra in palavra_secreta and letra not in letras_ja_mostradas:
                # Essa linha irá verificar se a letra do palpite está na palavra secreta e se a letra não foi mostrada antes
                print(f'A palavra contém a letra "{letra}". ')
                # Essa linha irá imprimir na tela que a letra está na palavra secreta, mas no lugar errado
                letras_ja_mostradas.add(letra)
                # Essa linha irá adicionar a letra no conjunto de letras já mostradas, para não repetir as letras que já foram mostradas

        print("Palavra até agora: ", "".join(letras_descobertas))
        # Essa linha irá imprimir na tela a palavra até agora, utilizando o join para juntar as letras da lista palavra_vazia em uma string
        tentativa += 1
        # Essa linha irá adicionar 1 na variavel tentativa, para contar as tentativas do jogador

    if tentativa > 5:
        print(f"Você perdeu! A palavra secreta era {palavra_secreta}")
        # Essa linha irá imprimir na tela que o jogador perdeu, e mostrar a palavra secreta, caso o jogador não acerte a palavra secreta até o número máximo de tentativas


       
if quantidade_letras == 6:
    tentativa = 1
    # Variavel para conseguir contar as tentativas do jogador
    SEIS_LETRAS = ["utopia", "casual", "hostil", "anseio", "gentil"]
    # Seis letras é uma lista com palavras de 6 letras, que serão utilizadas para o jogo
    palavra_secreta = random.choice(SEIS_LETRAS)
    # A palavra secreta será sorteada através do random.choice
    letras_descobertas = ['_'] * 6
    # Essa variavel é uma lista que irá armazenar as letras que o jogador já acertou, e o '_' será utilizado para mostrar ao jogador as letras que ele ainda não acertou
    while tentativa <= 6:
        # While para funcionar até que o jogador utilize o número máximo de tentativas

        palpite = input("Digite seu primeiro palpite para adivinhar a palavra secreta: ")
        # O palpite do jogador será armazenado na variavel palpite, e o .lower() serve para deixar a palavra em minusculo, caso o jogador digite em maiusculo

        if len(palpite) != 6:
            # O len serve para contar a quantidade de letras que o jogador digitou
            print("A palavra nao se encaixa em seis letras, tente novamente.")
            palpite = input("Digite seu primeiro palpite para adivinhar a palavra secreta: ")
        # Este if servirá caso o jogador digite uma palavra menor ou maior que a quantidade de letras escolhida
        # E pede para digitar o palpite novamente para atualizar a variável

        if palpite == palavra_secreta:
            print("Parabéns você acertou a palavra secreta!")
        # Caso o jogador acerte de primeira
            break
        # O break serve para parar o loop, caso o jogador acerte a palavra secreta de primeira  
       
        # Não coloquei if novamente, porque se não ocorrer de o jogador acertar de primeira já vai seguir o código
        resultado = ""
        # Variavel resultado será utilizada para armazenar o resultado do palpite do jogador, e depois imprimir na tela
        for i in range(6):
            if palpite[i] == palavra_secreta[i]:
                letras_descobertas[i] = palpite[i]
        # Essa linha irá verificar se a letra do palpite é igual a letra da palavra secreta, e se for igual irá armazenar na variavel palavra_vazia, que é uma lista que armazena as letras que o jogador já acertou

        letras_ja_mostradas = set()
        # Essa linha irá criar um conjunto vazio, que será utilizado para armazenar as letras que já foram mostradas ao jogador, para não repetir as letras que já foram mostradas
        for letra in palpite:
            if letra in palavra_secreta and letra not in letras_ja_mostradas:
                # Essa linha irá verificar se a letra do palpite está na palavra secreta e se a letra não foi mostrada antes
                print(f'A palavra contém a letra "{letra}".')
                # Essa linha irá imprimir na tela que a letra está na palavra secreta, mas no lugar errado
                letras_ja_mostradas.add(letra)
                # Essa linha irá adicionar a letra no conjunto de letras já mostradas, para não repetir as letras que já foram mostradas

        print("Palavra até agora: ", "".join(letras_descobertas))
        # Essa linha irá imprimir na tela a palavra até agora, utilizando o join para juntar as letras da lista palavra_vazia em uma string
        tentativa += 1
        # Essa linha irá adicionar 1 na variavel tentativa, para contar as tentativas do jogador

    if tentativa >= 6:
        print(f"Você perdeu! A palavra secreta era {palavra_secreta}")
        # Essa linha irá imprimir na tela que o jogador perdeu, e mostrar a palavra secreta, caso o jogador não acerte a palavra secreta até o número máximo de tentativas


if quantidade_letras == 7:
    tentativa = 0
    # Variavel para conseguir contar as tentativas do jogador
    SETE_LETRAS = ["mochila", "lasanha", "cozinha", "atacado", "alergia"]
    # Sete letras é uma lista com palavras de 7 letras, que serão utilizadas para o jogo
    palavra_secreta = random.choice(SETE_LETRAS)
    # A palavra secreta será sorteada através do random.choice
    letras_descobertas = ['_'] * 7
    # Essa variavel é uma lista que irá armazenar as letras que o jogador já acertou, e o '_' será utilizado para mostrar ao jogador as letras que ele ainda não acertou

    while tentativa <= 7:
        # While para funcionar até que o jogador utilize o número máximo de tentativas

        palpite = input("Digite seu primeiro palpite para adivinhar a palavra secreta: ")

        if len(palpite) != 7:
            print("A palavra nao se encaixa em sete letras, tente novamente.")
            palpite = input("Digite seu primeiro palpite para adivinhar a palavra secreta: ")
        # Este if servirá caso o jogador digite uma palavra menor ou maior que a quantidade de letras escolhida
        # E pede para digitar o palpite novamente para atualizar a variável
        if palpite == palavra_secreta:
            print("Parabéns você acertou a palavra secreta!")
        # Caso o jogador acerte de primeira
            break
        # O break serve para parar o loop, caso o jogador acerte a palavra secreta de primeira  
       
        # Não coloquei if novamente, porque se não ocorrer de o jogador acertar de primeira já vai seguir o código
        resultado = ""
        # Variavel resultado será utilizada para armazenar o resultado do palpite do jogador, e depois imprimir na tela
        for i in range(7):
            if palpite[i] == palavra_secreta[i]:
                letras_descobertas[i] = palpite[i]
        # Essa linha irá verificar se a letra do palpite é igual a letra da palavra secreta, e se for igual irá armazenar na variavel palavra_vazia, que é uma lista que armazena as letras que o jogador já acertou

        letras_ja_mostradas = set()
        # Essa linha irá criar um conjunto vazio, que será utilizado para armazenar as letras que já foram mostradas ao jogador, para não repetir as letras que já foram mostradas
        for letra in palpite:
            if letra in palavra_secreta and letra not in letras_ja_mostradas:
                # Essa linha irá verificar se a letra do palpite está na palavra secreta e se a letra não foi mostrada antes
                print(f'A palavra contém a letra "{letra}". ')
                # Essa linha irá imprimir na tela que a letra está na palavra secreta, mas no lugar errado
                letras_ja_mostradas.add(letra)
                # Essa linha irá adicionar a letra no conjunto de letras já mostradas, para não repetir as letras que já foram mostradas

        print("Palavra até agora: ", "".join(letras_descobertas))
        # Essa linha irá imprimir na tela a palavra até agora, utilizando o join para juntar as letras da lista palavra_vazia em uma string
        tentativa += 1
        # Essa linha irá adicionar 1 na variavel tentativa, para contar as tentativas do jogador

    if tentativa >= 7:
        print(f"Você perdeu! A palavra secreta era {palavra_secreta}")
        # Essa linha irá imprimir na tela que o jogador perdeu, e mostrar a palavr
