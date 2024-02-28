import pandas as pd
import sys
import os

diretorio_script_principal = os.path.dirname(os.path.abspath(sys.argv[0]))
caminho_excel = os.path.join(diretorio_script_principal, 'enderecos.xlsx')

dados = pd.read_excel(caminho_excel, sheet_name='tabelaValores')

import difflib

def buscar_regioes_aproximadas(regiao_digitada, regioes_disponiveis):
    """
    Busca correspondências aproximadas para a região digitada.

    Parameters:
    - regiao_digitada (str): A região digitada pelo usuário.
    - regioes_disponiveis (array): Lista de regiões disponíveis.

    Returns:
    - list: Lista de correspondências aproximadas encontradas.
    """
    correspondencias_aproximadas = difflib.get_close_matches(regiao_digitada, regioes_disponiveis,
                                                             n=len(regioes_disponiveis), cutoff=0.5)
    return correspondencias_aproximadas


def obter_valor_frete(regiao_correspondente, tipo_valor):
    """
    Obtém o valor do frete para a região e tipo de valor especificados.

    Parameters:
    - regiao_correspondente (str): A região correspondente.
    - tipo_valor (str): Tipo de valor, 'ValorMotoboy' ou 'ValorCliente'.

    Returns:
    - float: Valor do frete.
    """
    dados_regiao = dados[dados['Local'] == regiao_correspondente]
    return dados_regiao[tipo_valor].iloc[0] if not dados_regiao.empty else None


def exibir_correspondencias_e_valores(correspondencias, tipo_valor):
    """
    Exibe todas as correspondências e seus respectivos valores.

    Parameters:
    - correspondencias (list): Lista de correspondências aproximadas.
    - tipo_valor (str): Tipo de valor, 'ValorMotoboy' ou 'ValorCliente'.

    Returns:
    None
    """
    print(f'\nCorrespondências aproximadas:')
    for correspondencia in correspondencias:
        valor = obter_valor_frete(correspondencia, tipo_valor)
        print(f'Região: {correspondencia.capitalize()} - R$ {valor:.2f}')


def regiaoMotoboy():
    """
    Obtém e imprime o valor do frete para a região inserida pelo usuário (motoboy).

    Returns:
    None
    """
    try:
        regiao_digitada = input('\nDigite a região (Exemplo: Diadema): ').strip().lower()
        print()

    except Exception as errorValue:
        print(f'\nOcorreu um erro!! [{errorValue}].')
    else:
        try:
            pass
            # peso = float(input('Digite o peso: '))

        except ValueError as errorValue:
            print(f"\nOcorreu um erro!! [{errorValue}]")
            print('Digite somente números inteiros ou decimal para o Peso.')

        else:
            dados['Local'] = dados['Local'].str.lower()
            # dadosPontos = dados['Pontos'].copy()  # Copia a série para evitar modificar a tabela original
            #
            # if peso >= 10:
            #     dadosPontos += 1
            # elif 20 <= peso <= 25:
            #     dadosPontos += 2
            # elif peso > 25:
            #     print('Este serviço não pode ser feito, Risco de Segurança ao Motoboy!!')
            # else:
            #     print('teste')
            #
            # # Atualizar temporariamente a tabela com a nova pontuação
            # dados_temporarios = dados.copy()
            # dados_temporarios['Pontos'] = dadosPontos

            # Obter a lista de regiões disponíveis
            regioes_disponiveis = dados['Local'].unique()

            # Verificar se a região digitada é uma correspondência exata
            if regiao_digitada in regioes_disponiveis:
                regiao_correspondente = regiao_digitada
                return regiao_correspondente#, dados_temporarios
            else:
                # Tentar encontrar correspondências aproximadas
                correspondencias_aproximadas = buscar_regioes_aproximadas(regiao_digitada, regioes_disponiveis)

                if correspondencias_aproximadas:
                    exibir_correspondencias_e_valores(correspondencias_aproximadas, "ValorMotoboy")
                else:
                    print('Nenhuma correspondência aproximada encontrada.')
                    return

                # Pode escolher uma das correspondências aproximadas
                escolha = input('\nEscolha uma das opções acima ou pressione '
                                'Enter para tentar novamente: ').strip().lower()

                if escolha in correspondencias_aproximadas:
                    regiao_correspondente = escolha
                else:
                    print('Escolha inválida. Tente novamente.')
                    return

            # Obter e exibir o valor do frete para Cliente
            valor_motoboy = obter_valor_frete(regiao_correspondente, "ValorMotoboy")
            print(f'\nValor do Frete para {regiao_correspondente.capitalize()}: R$ {valor_motoboy:.2f}')


def regiaoCliente():
    """
    Obtém e imprime o valor do frete para a região inserida pelo usuário (cliente).

    Returns:
    None
    """
    try:
        # Pedir ao usuário para digitar a região
        regiao_digitada = input('\nDigite a região (Exemplo: Diadema): ').strip().lower()

    except Exception as errorValue:
        print(f'\nOcorreu um erro!! [{errorValue}].')
        print('Digite a região, por favor.')

    else:
        # Converter a coluna "Local" para minúsculas para comparação insensível a maiúsculas/minúsculas
        dados['Local'] = dados['Local'].str.lower()

        # Obter a lista de regiões disponíveis
        regioes_disponiveis = dados['Local'].unique()

        # Verificar se a região digitada é uma correspondência exata
        if regiao_digitada in regioes_disponiveis:
            regiao_correspondente = regiao_digitada
            return regiao_correspondente
        else:
            # Tentar encontrar correspondências aproximadas
            correspondencias_aproximadas = buscar_regioes_aproximadas(regiao_digitada, regioes_disponiveis)

            if correspondencias_aproximadas:
                exibir_correspondencias_e_valores(correspondencias_aproximadas, "ValorCliente")
            else:
                print('Nenhuma correspondência aproximada encontrada.')
                return

            # Pode escolher uma das correspondências aproximadas
            escolha = input('\nEscolha uma das opções acima ou pressione '
                            'Enter para tentar novamente: ').strip().lower()

            if escolha in correspondencias_aproximadas:
                regiao_correspondente = escolha
            else:
                print('Escolha inválida. Tente novamente.')
                return

            # Obter e exibir o valor do frete para Cliente
            valor_cliente = obter_valor_frete(regiao_correspondente, "ValorCliente")
            print(f'\nValor do Frete para {regiao_correspondente.capitalize()}: R$ {valor_cliente:.2f}')
