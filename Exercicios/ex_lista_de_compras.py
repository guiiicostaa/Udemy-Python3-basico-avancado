'''
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de indices inexistentes.
'''
import os

lista = []

while True:
    print('Escolha uma opção abaixo:')
    opcao = input('[i]nserir, [a]pagar, [l]istar ou [p]arar: ')

    if opcao == "i":
        os.system('cls')
        item = input("Item: ")
        lista.append(item)

    elif opcao == 'a':
        indice_str = input('Digite o número do indice que deseja apagar: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Digite um número inteiro.')
        except IndexError:
            print('Indice não existente.')
        except Exception:
            print('Erro não identificado.')

    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Lista vazia.')
        for i, item in enumerate(lista):
            print(i, item)

    elif opcao == 'p':
        break

    else:
        print('Escolha uma das opções válidas.') 
