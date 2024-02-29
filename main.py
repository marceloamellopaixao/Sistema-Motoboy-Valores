from valorBairros import regiaoCliente, regiaoMotoboy
import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

# Sistema de Preços (Motoboy)

opcoesFrete = ['(1) - Valor do Frete (p/Região)', '(0) - Voltar ao Menu']


def exibir_menu(text, *args):
    """
    Exibe um menu com as opções passadas como argumentos.

    Parameters:
    - text (str): Texto a ser exibido como título do menu.
    - *args (list): Lista de opções a serem exibidas no menu.

    Returns:
    None
    """
    print(f'[----------- {text} -----------]\n')
    idOpcao = 0

    for opcao in args:
        idOpcao += len([opcao])
        print(f'({idOpcao}) - {opcao}')

    print('(0) - Fechar Programa')


def precosMotoboy():
    """
    Exibe o menu e realiza ações relacionadas aos preços do motoboy.

    Returns:
    None
    """
    while True:
        print('[----------- Tabela de Preços - Motoboy -----------]\n')

        for i in range(2):
            print(f'{opcoesFrete[i]}')

        try:
            opcao = int(input('\nDigite o número da opção desejada: '))

            while opcao > 1 or opcao < 0:
                print('Ocorreu um Erro!! Opção inexistente!')
                opcao = int(input('Digite o número da opção correta: '))

            if opcao == 1:
                regiaoMotoboy()
                print()
            else:
                print('\n[Retornando ao Menu principal!]\n')
                break

        except ValueError:
            print('Ocorreu um erro!! Favor digitar somente números.\n')


def precosCliente():
    """
    Exibe o menu e realiza ações relacionadas aos preços do cliente.

    Returns:
    None
    """
    while True:
        print('[----------- Tabela de Preços - Cliente -----------]\n')

        for i in range(2):
            print(f'{opcoesFrete[i]}')

        try:
            opcao = int(input('\nDigite o número da opção desejada: '))

            while opcao > 1 or opcao < 0:
                print('Ocorreu um Erro!! Opção inexistente!')
                opcao = int(input('Digite o número da opção correta: '))

            if opcao == 1:
                regiaoCliente()
                print()
            else:
                print('\n[Retornando ao Menu principal!]\n')
                break

        except ValueError:
            print('Ocorreu um erro!! Favor digitar somente números.\n')


def main():
    """
    Função principal que controla o fluxo do programa.

    Returns:
    None
    """
    while True:
        exibir_menu('Tabela de Preços', 'Motoboy', 'Cliente')
        try:
            opcaoEscolhida = int(input('\nDigite o número da opção desejada: '))
            print()
            while opcaoEscolhida < 0 or opcaoEscolhida > 2:
                print('Ocorreu um erro, opção inexistente!!')
                int(input('\nDigite a opção desejada: '))
                print()

            if opcaoEscolhida == 1:
                precosMotoboy()

            elif opcaoEscolhida == 2:
                precosCliente()

            else:
                print('\n[Programa finalizado com sucesso!]')
                break

        except ValueError:
            print('Ocorreu um Erro!! Favor digitar somente números.\n')


if __name__ == "__main__":
    main()
