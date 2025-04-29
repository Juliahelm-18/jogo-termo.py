import random  

nome = input("Digite seu nome para iniciarmos o jogo: ")

print(f"Bem vindo {nome} antes de iniciar o jogo vamos lhe mostrar as regras: \n- Você deve escolher a dificuldade do jogo, se serão palavras de 5, 6 ou 7 letras; \n- As tentativas são relacionadas com a quantidade de letras, ou seja, 5, 6 ou 7 tentativas; \n- Após o palpite o jogo irá mostrar onde ocorreram acertos e se as letras existem na palavra; \n- O jogo terminará quando você acertar ou quando não houver mais tentativas. ")
print("Vamos iniciar o jogo termo.py!")

quantidade_letras = int(input("Qual a dificuldade você gostaria de jogar, 5, 6 ou 7 letras? "))

CINCO_LETRAS = ["nuvem", "poder", "diabo", "nesta", "nariz"]
SEIS_LETRAS = ["utopia", "casual", "hostil", "anseio", "gentil"]
SETE_LETRAS = ["mochila", "lasanha", "cozinha", "atacado", "alergia"]

if quantidade_letras == 5:
    palavra_secreta = random.choice(CINCO_LETRAS)
elif quantidade_letras == 6:
    palavra_secreta = random.choice(SEIS_LETRAS)
elif quantidade_letras == 7:
    palavra_secreta = random.choice(SETE_LETRAS)

def adivinhacao(quantidade_letras):
  tentativa = 1
  letras_descobertas * (quantidade_letras)

  while tentativa <= (quantidade_letras):
    
    palpite = input("Digite seu palpite para tentar adivinhar a palavra: ")
    
    if len(palpite) != (quantidade_letras):
        print(f"A palavra não tem {quantidade_letras}, digite novamente")
        palpite = input("Digite seu palpite para tentar adivinhar a palavra: ")

    if palpite == palavra_secreta:
        print("Parabéns você acertou a palavra secreta!")
        break 

    resultado = ''
    for i in range(quantidade_letras):
        if palpite[i] = palavra_secreta[i]:
            letras_descobertas[i] = palpite[i]
    
    letras_ja_mostradas = set()

    for letra in palpite:
        if letra in palavra_secreta and letra not in letras_ja_mostradas:
            print(f'A palavra contém a letra {letra}')


  
