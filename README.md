# Termo - Jogo de Palavras
Termo é um jogo interativo de adivinhação de palavras em Python. O jogador deve descobrir uma palavra secreta escolhida aleatoriamente, com dicas sobre letras corretas e suas posições.

# Regras do Jogo
- Escolha a dificuldade do jogo: palavras de 5, 6 ou 7 letras.

- O número de tentativas é igual à quantidade de letras da palavra secreta.

- Após cada palpite, o jogo mostrará:

     - Letras no lugar correto.

     - Letras que existem na palavra, mas em posição diferente.

- O jogo termina quando o jogador acerta a palavra ou esgota todas as tentativas.

- Ao final, é possível escolher jogar novamente.

# Funcionalidades
- Geração aleatória de palavras de diferentes tamanhos.

- Validação automática de palpite (tamanho correto).

- Exibição clara de letras corretas e letras presentes na palavra.

- Loop para jogar novamente caso o jogador queira.

# Estrutura do Código
- escolher_palavra(): escolhe a palavra secreta e inicializa a lista de letras descobertas.

- pedir_palpite(): solicita ao jogador um palpite válido.

- atualizar_letras(): atualiza a lista de letras corretas na posição certa.

- mostrar_status(): mostra as letras corretas e letras presentes na palavra.

- jogo(): função principal que controla o fluxo do jogo.

# Licença
Este projeto é livre para uso e modificação.

# Exemplo de uso
``` Digite seu nome para iniciar o jogo: Julia
Bem-vindo, Julia! Aqui estão as regras:
- Escolha a dificuldade do jogo: palavras de 5, 6 ou 7 letras.
- O número de tentativas é igual à quantidade de letras.
- O jogo mostrará letras corretas e letras existentes na palavra.
- O jogo termina quando você acertar ou acabar as tentativas.

Escolha a quantidade de letras da palavra secreta (5, 6 ou 7): 5
Digite seu palpite (5 letras): nuvem

Parabéns! Você acertou a palavra secreta 'nuvem' em 1 tentativa!

Deseja jogar novamente? (s/n): n

Obrigado por jogar! Até a próxima. 








