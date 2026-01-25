import random
# Importa o dicionário de palavras organizado por tamanho
from palavras import PALAVRAS
# Importa funções auxiliares para entrada e validações
from utils import pedir_palpite, escolher_dificuldade, letras_existentes


def escolher_palavra(tamanho):
    """
    Escolhe aleatoriamente uma palavra com o tamanho definido
    e inicializa a lista de letras descobertas com '_'.
    """
    palavra = random.choice(PALAVRAS[tamanho])
    letras_descobertas = ["_"] * tamanho
    return palavra, letras_descobertas


def atualizar_letras_corretas(palpite, palavra, letras_descobertas):
    """
    Atualiza as letras que estão na posição correta,
    comparando o palpite com a palavra secreta.
    """
    for i, letra in enumerate(palpite):
        if letra == palavra[i]:
            letras_descobertas[i] = letra


def mostrar_status(letras_descobertas, letras_fora_lugar):
    """
    Mostra ao jogador:
    - letras que já foram acertadas na posição correta
    - letras que existem na palavra, mas podem estar fora do lugar
    """
    print(f"Letras no lugar certo: {' '.join(letras_descobertas)}")
    print(f"Letras existentes na palavra: {', '.join(letras_fora_lugar)}")


def jogar():
    """
    Função principal do jogo.
    Controla o fluxo da partida, tentativas e mensagens ao jogador.
    """
    nome = input("Digite seu nome para iniciar o jogo: ")

    # Exibe as regras do jogo
    print(f"""
    Bem-vindo(a), {nome}!
        - Palavras de 5, 6 ou 7 letras
        - Tentativas = quantidade de letras escolhidas
        - Letras no lugar certo serão mostradas
        - Letras existentes na palavra serão mostradas
""")

    # Escolhe a dificuldade (tamanho da palavra)
    tamanho = escolher_dificuldade(PALAVRAS)

    # Define a palavra secreta e o estado inicial das letras descobertas
    palavra_secreta, letras_descobertas = escolher_palavra(tamanho)

    # Número de tentativas permitido
    tentativas = tamanho

    # Loop principal do jogo
    while tentativas > 0:
        palpite = pedir_palpite(tamanho)

        # Verifica se o jogador acertou a palavra
        if palpite == palavra_secreta:
            print(f"Parabéns, {nome}! Você acertou a palavra '{palavra_secreta}' em {tentativas} tentativas!")
            return

        # Atualiza letras corretas e mostra feedback
        atualizar_letras_corretas(palpite, palavra_secreta, letras_descobertas)
        existentes = letras_existentes(palpite, palavra_secreta)
        mostrar_status(letras_descobertas, existentes)

        tentativas -= 1
        print(f"Tentativas restantes: {tentativas}\n")

    # Caso o jogador não acerte dentro do limite
    print(f"Você perdeu! A palavra era '{palavra_secreta}'.")
