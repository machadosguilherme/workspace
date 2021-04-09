import os


def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep} Ola {nome}, Estudo ADS na faculdade impacta de Tecnologia. {os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep} Ola {nome}, É um curso superior de tecnologia (ANALISE E DESENVOLVIMENTO DE SISTEMAS). {os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep} Ola {nome}, Porque eu quero curioso. {os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep} Ola {nome}, Origado pela passagem, tenha um otimo dia. {os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep} Obrigado pela visita, tenha um otimo dia {nome}. {os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')
    return


def start():
    print("Olá! Seja Bem vindo ao Machados-World")
    nome = input('Qual o seu nome? ')
    email = input('Digite seu email: ')
    while True:
        resposta = input(f'O que gostaria de saber hoje? {os.linesep} [1] - O que você estuda? {os.linesep} [2] - O que é ADS? {os.linesep} [3] - Por que estuda ADS? {os.linesep} [4] - Nada não só passei por aqui. {os.linesep} [5] - Por hoje é só isso mesmo. {os.linesep}')
        print(processar_resposta(resposta, nome))


if __name__ == '__main__':
    start()