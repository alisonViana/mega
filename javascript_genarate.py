import csv


def carregar_jogos():
    with open("./jogos/jogos_gerados.csv", 'r') as jogos_csv:
        reader = csv.reader(jogos_csv)
        for index, row in enumerate(reader):
            print("***** NOVO JOGO *****")
            print(f'Linha: {index+1}')
            for number in row:
                print(f'document.getElementById("n{number}").click()')
            print('document.getElementById("colocarnocarrinho").click()')



carregar_jogos()
