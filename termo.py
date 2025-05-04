import random 

nome = input("Digite seu nome para iniciar o jogo:")
# Pergunta o nome do jogador e armazena na variável nome

print(f"Bem vindo {nome} antes de iniciar o jogo vamos lhe mostrar as regras: \n- Você deve escolher a dificuldade do jogo, se serão palavras de 5, 6 ou 7 letras; \n- As tentativas são relacionadas com a quantidade de letras, ou seja, 5, 6 ou 7 tentativas; \n- Após o palpite o jogo irá mostrar onde ocorreram acertos e se as letras existem na palavra; \n- O jogo terminará quando você acertar ou quando não houver mais tentativas. ")
print("Vamos iniciar o jogo termo.py!")
# Mostra as regras para o jogador e inicia o jogo

quantidade_letras = int(input("Digite a quantidade de letras que você deseja que a palavra secreta tenha, se serão 5, 6 ou 7 letras: "))
# Pergunta a quantidade de letras que o jogador deseja e armazena na variável quantidade_letras, assim o jogo poderá saber a dificuldade que o jogador deseja

CINCO_LETRAS = ["nuvem", "poder", "diabo", "nesta", "nariz"]
SEIS_LETRAS = ["utopia", "casual", "hostil", "anseio", "gentil"]
SETE_LETRAS = ["mochila", "lasanha", "cozinha", "atacado", "alergia"]
# Cria listas com palavras de 5, 6 e 7 letras para o jogo, as listas servem para armazenar palavras aleartórias que serão sorteadas no jogo

if quantidade_letras == 5:
    palavra_secreta = random.choice(CINCO_LETRAS)
    letras_descobertas = ['_'] * 5
    # Se a quantidade de letras for 5, sorteia uma palavra da lista de 5 letras e cria uma lista de letras descobertas com 5 espaços em branco para mostrar quais estão no local correto

if quantidade_letras == 6:
    palavra_secreta = random.choice(SEIS_LETRAS)
    letras_descobertas = ['_'] * 6
    # Se a quantidade de letras for 6, sorteia uma palavra da lista de 6 letras e cria uma lista de letras descobertas com 6 espaços em branco para mostrar quais estão no local correto

if quantidade_letras == 7:
    palavra_secreta = random.choice(SETE_LETRAS)
    letras_descobertas = ['_'] * 7
    # Se a quantidade de letras for 7, sorteia uma palavra da lista de 7 letras e cria uma lista de letras descobertas com 7 espaços em branco para mostrar quais estão no local correto


def jogo(quantidade_letras):
    # Inicia o jogo com a quantidade de letras escolhida pelo jogador
    tentativa = 1
    # Cria uma variável nomeada de tentativa que inicia com 1, para contar quantas tentativas o jogador já fez
    # Inicia com o número 1, pois iniciando do 0 daria uma tentativa a mais para o jogador.

    while tentativa <= quantidade_letras:
        # Enquanto o número de tentativas for menor ou igual a quantidade de letras, o jogo continua (caso o jogador não acerte a palavra antes de acabar as tentativas)
        palpite = input("Digite seu palpite para adivinhar a palavra secreta: ").lower()
        # Pergunta ao jogador qual é o palpite e transforma em minúscula para evitar erros de digitação e erros no jogo

        if len(palpite) != quantidade_letras:
            print('Seu palpite tem que estar de acordo com a quantidade de letras!')
            palpite = input("Digite seu palpite para adivinhar a palavra secreta: ").lower()
            # Se o palpite não tiver a mesma quantidade de letras que a palavra secreta, pede para o jogador digitar novamente

        if palpite == palavra_secreta:
            print('Parabéns! Você ganhou o jogo.')
            print(f"Você utilizou {tentativa} tentativas para acertar a palavra secreta.")
            # Se o palpite for igual a palavra secreta, o jogador ganhou e o jogo termina, mostrando quantas tentativas foram usadas
            break 
            # O break serve para quebrar o loop do while

        resultado = ''
        # Cria uma variável nomeada resultado que inicia vazia, para armazenar o resultado do palpite do jogador

        for i in range(quantidade_letras):
            if palpite[i] == palavra_secreta[i]:
                letras_descobertas[i] = palpite [i]
                # Se a letra do palpite for igual a letra da palavra secreta, a letra descoberta é igual a letra do palpite, ou seja, o jogador acertou a letra e ela é mostrada na tela dentro de uma lista

        letras_ja_mostradas = set()
        # Cria uma variável letras_ja_mostradas que inicia vazia, para armazenar as letras que já foram mostradas na tela, assim o jogador não fica confuso com letras repetidas

        for letra in palpite:
            if letra in palavra_secreta and letra not in letras_ja_mostradas:
                letras_ja_mostradas.add(letra)
                # Se a letra do palpite estiver na palavra secreta e não estiver na lista de letras já mostradas, adiciona a letra na lista de letras já mostradas

        print(f'A palavra contém as letras: {", ".join(sorted(letras_ja_mostradas))}')
        # Mostra as letras que o jogador acertou, mas errou o lugar, ordenadas em ordem alfabética, para facilitar a visualização
        print(f'Letras no lugar certo: {" ".join(letras_descobertas)}')
        # Mostra as letras que o jogador acertou o lugar na palavra secreta

               
        tentativa += 1
        # Adiciona 1 na variável tentativa, para contar quantas tentativas o jogador já fez

        if tentativa > quantidade_letras:
            print(f"Você perdeu! A palavra secreta era {palavra_secreta}")
            print(f"Você utilizou {tentativa} tentativas para tentar adivinhar a palavra secreta.")
            # Se o número de tentativas for maior que a quantidade de letras, o jogador perdeu e o jogo termina, mostrando a palavra secreta
        
jogo(quantidade_letras)
# Chama a função jogo com a quantidade de letras escolhida pelo jogador, para iniciar o jogo
