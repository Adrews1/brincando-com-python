def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        return  n % (m+1)

def usuario_escolhe_jogada(n, m):
    jogada = int(input('Quantas peças você vai tirar?: '))
    while jogada <= 0 or jogada >m or jogada > n:
        print('Oops! Jogada inválida! Tente de novo.')
        jogada = int(input(f'Quantas peças você vai tirar?: '))
    if jogada == 1:
        print(f'Você tirou {jogada} peça')
    else:
        print(f'Você tirou {jogada} peças')
    return jogada


def partida():
    n = int(input('quantas peças?: '))
    m = int(input('Limite de peças por jogada?: '))
    if n % (m + 1) >= 1:
        print('Computador começa!')
        while n > 0:
            pc = computador_escolhe_jogada(n, m)
            print(f'O computador tirou {pc}')
            n -= pc
            if n == 0:
                print('O computador venceu!')
                break
            jogador = usuario_escolhe_jogada(n, m)
            n -= jogador
            if n == 0:
                print('Você venceu!')
                break
    elif n % (m+1) == 0:
        print('Você começa')
        while n > 0:
            jogador = usuario_escolhe_jogada(n, m)
            n -= jogador
            if n == 0:
                print('Você venceu!')
                break
            pc = computador_escolhe_jogada(n, m)
            print(f'O computador tirou {pc}')
            n -= pc
            if n == 0:
                print('O computador venceu!')
                break

def campeonato():
    print("""Bem-vindo ao jogo do NIM! Escolha:

1 - para jogar uma partida isolada
2 - para jogar um campeonato 2""")
    escolha = int(input('Escolha: '))
    while escolha > 2:
        escolha = int(input('Escolha uma opção valida: '))
    if escolha == 1:
        partida()
    elif escolha == 2:
        for vez in range(3):
            partida()
        print(f'**** Final do campeonato! ****\n'
              'Placar: Você 0 X 3 Computador') 

campeonato()