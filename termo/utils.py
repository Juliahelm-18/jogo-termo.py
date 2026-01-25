def pedir_palpite(tamanho):
    """
    Solicita ao jogador um palpite com a quantidade correta de letras.
    Continua pedindo até que o palpite seja válido.
    """
    while True:
        palpite = input(f"Digite seu palpite ({tamanho} letras): ").lower()

        # Verifica se o palpite tem o tamanho correto
        if len(palpite) == tamanho:
            return palpite

        print(f"O palpite deve ter exatamente {tamanho} letras.")


def escolher_dificuldade(palavras):
    """
    Permite ao jogador escolher a dificuldade do jogo,
    baseada no tamanho da palavra secreta.
    """
    while True:
        try:
            tamanho = int(input("Escolha a quantidade de letras (5, 6 ou 7): "))

            # Verifica se o tamanho existe no dicionário de palavras
            if tamanho in palavras:
                return tamanho

            print("Escolha inválida.")
        except ValueError:
            # Trata o caso em que o usuário não digita um número
            print("Digite um número válido.")


def letras_existentes(palpite, palavra):
    """
    Retorna uma lista ordenada de letras que existem
    na palavra secreta, independentemente da posição.
    """
    return sorted({letra for letra in palpite if letra in palavra})
