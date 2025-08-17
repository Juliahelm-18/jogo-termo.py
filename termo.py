import random

# Listas de palavras
CINCO_LETRAS = ["nuvem", "poder", "diabo", "nesta", "nariz"]
SEIS_LETRAS = ["utopia", "casual", "hostil", "anseio", "gentil"]
SETE_LETRAS = ["mochila", "lasanha", "cozinha", "atacado", "alergia"]

# Função para escolher palavra e inicializar letras descobertas
def escolher_palavra(quantidade_letras):
    if quantidade_letras == 5:
        palavra = random.choice(CINCO_LETRAS)
    elif quantidade_letras == 6:
        palavra = random.choice(SEIS_LETRAS)
    elif quantidade_letras == 7:
        palavra = random.choice(SETE_LETRAS)
    else:
        return None, None
    letras_descobertas = ['_'] * quantidade_letras
    return palavra, letras_descobertas

# Função para pedir palpite válido
def pedir_palpite(quantidade_letras):
    while True:
        palpite = input(f"Digite seu palpite ({quantidade_letras} letras): ").lower()
        if len(palpite) != quantidade_letras:
            print(f"Seu palpite deve ter exatamente {quantidade_letras} letras.")
        else:
            return palpite

# Função para atualizar letras no lugar certo
def atualizar_letras(palpite, palavra_secreta, letras_descobertas):
    for i in range(len(palpite)):
        if palpite[i] == palavra_secreta[i]:
            letras_descobertas[i] = palpite[i]

# Função para mostrar status do jogo
def mostrar_status(palpite, palavra_secreta, letras_descobertas):
    letras_certas_fora_lugar = set()
    for letra in palpite:
        if letra in palavra_secreta:
            letras_certas_fora_lugar.add(letra)
    print(f"Letras no lugar certo: {' '.join(letras_descobertas)}")
    print(f"Letras que existem na palavra (posição errada ou certa): {', '.join(sorted(letras_certas_fora_lugar))}")

# Função principal do jogo
def jogo():
    nome = input("Digite seu nome para iniciar o jogo: ")
    print(f"\nBem-vindo, {nome}! Aqui estão as regras:\n"
          "- Escolha a dificuldade do jogo: palavras de 5, 6 ou 7 letras.\n"
          "- O número de tentativas é igual à quantidade de letras.\n"
          "- O jogo mostrará letras corretas e letras existentes na palavra.\n"
          "- O jogo termina quando você acertar ou acabar as tentativas.\n")

    while True:
        try:
            quantidade_letras = int(input("Escolha a quantidade de letras da palavra secreta (5, 6 ou 7): "))
            if quantidade_letras not in [5, 6, 7]:
                print("Escolha inválida. Digite 5, 6 ou 7.")
                continue
            break
        except ValueError:
            print("Digite um número válido.")

    palavra_secreta, letras_descobertas = escolher_palavra(quantidade_letras)
    tentativas = 0
    max_tentativas = quantidade_letras

    while tentativas < max_tentativas:
        palpite = pedir_palpite(quantidade_letras)
        tentativas += 1

        if palpite == palavra_secreta:
            print(f"Parabéns, {nome}! Você acertou a palavra secreta '{palavra_secreta}' em {tentativas} tentativas!")
            return

        atualizar_letras(palpite, palavra_secreta, letras_descobertas)
        mostrar_status(palpite, palavra_secreta, letras_descobertas)
        print(f"Tentativas restantes: {max_tentativas - tentativas}\n")

    print(f"Você perdeu! A palavra secreta era '{palavra_secreta}'. Tente novamente, {nome}!")

# Chamada do jogo
jogo()

while True:
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente == 's':
        jogo()
    elif jogar_novamente == 'n':
        print("Obrigado por jogar! Até a próxima.")
        break
    else:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")
