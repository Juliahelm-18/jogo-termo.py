import random  

nome = input("Digite seu nome para iniciarmos o jogo: ")

print(f"Bem vindo {nome} antes de iniciar o jogo vamos lhe mostrar as regras: \n- Você deve escolher a dificuldade do jogo, se serão palavras de 5, 6 ou 7 letras; \n- As tentativas são relacionadas com a quantidade de letras, ou seja, 5, 6 ou 7 tentativas; \n- Após o palpite o jogo irá mostrar onde ocorreram acertos e se as letras existem na palavra; \n- O jogo terminará quando você acertar ou quando não houver mais tentativas. ")
print("Vamos iniciar o jogo termo.py!")

quantidade_letras = int(input("Qual a dificuldade você gostaria de jogar, 5, 6 ou 7 letras? "))

