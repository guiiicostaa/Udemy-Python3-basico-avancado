"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'bolacha'
letras_acertadas = '' #variavel para salvar as letras acertadas. pois no while reseta tudo quando voltar
n_tentativas = 0

while True:
    letra = input("Digite uma letra: ")
    n_tentativas += 1

    #primeira condição de digitar somente uma letra
    if len(letra)>1:
        print('Digite apenas UMA letra: ')
        continue
    
    if letra in palavra_secreta:
        letras_acertadas += letra #vai acumulando e salvando as letras acertadas

    #vamos percorrer a palavra secreta.
    palavra_formada=''
    for i in palavra_secreta:
        if i in letras_acertadas:
            palavra_formada += i
        else:
            palavra_formada += "*"
    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('Parabéns, você ganhou!')
        print(f'Tentativas: {n_tentativas}')
        break
    

    
    

       



