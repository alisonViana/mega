import csv
import random


def carregar_resultados():
    try:
        resultados = []

        with open("resultados/megasena_todos_resultados_221222.csv", 'r') as resultados_csv:
            reader = csv.reader(resultados_csv)
            header = next(reader)

            for row in reader:
                resultado = {
                    "concurso": row[0],
                    "data": row[1],
                    "jogo": row[2:8]
                }
                resultados.append(resultado)
        # print(resultados[0:5])
        return resultados

    except Exception as e:
        print("Algo deu errado! " + str(e))


def mais_sorteados():
    try:
        with open("./resultados/megasena_mais_sorteados_221226.csv", 'r') as mais_sorteados_csv:
            reader = csv.reader(mais_sorteados_csv)
            header = next(reader)

            numeros = [f'{int(row[0]):02}' for row in reader]
            # print(numeros)
        return numeros[0:12]

    except Exception as e:
        print("Algo deu errado! " + str(e))


def conferir_jogo(jogo):
    resultados = carregar_resultados()

    for resultado in resultados:
        if jogo == resultado["jogo"]:
            print(f'Jogo já sorteado em {resultado["data"]} no concurso: {resultado["concurso"]}!')
            return True
    else:
        print("Jogo nunca sorteado!")
        return False


def gerar_jogo(aleatorio=False, todos_numeros=True):
    if aleatorio:
        mensagem_sucesso = "Jogo gerado:"
        mensagem_erro = "Gerando novo jogo..."
        lista = range(1, 61) if todos_numeros else mais_sorteados()
        jogo = list(map(lambda x: f'{x:02}', random.sample(lista, 6)))
    else:
        mensagem_sucesso = "Seu jogo:"
        mensagem_erro = "Tente novamente"
        jogo = input("Digite 6 números entre 1 e 60 seguido de espaço: ").split(' ')

    jogo.sort()

    if conferir_jogo(jogo):
        print(mensagem_erro)
        gerar_jogo()
    else:
        print(mensagem_sucesso)
        print(jogo)
        resposta = input("Salvar jogo y/n: ").lower()
        if resposta == 'y':
            salvar_jogo(jogo)


def salvar_jogo(jogo):
    try:
        with open("./jogos/jogos_gerados.csv", 'a') as jogos_gerados:
            writer = csv.writer(jogos_gerados, delimiter=',')
            writer.writerow(jogo)
        print("Jogo salvo!")

    except Exception as e:
        print("Algo deu errado! " + str(e))


def menu():
    return input('''1 - Criar jogo
2 - Gerar jogo aleatório
3 - Gerar jogo aleatótrio com os números mais sorteados
9 - Sair
--> ''')


while True:
    match menu():
        case "1":
            gerar_jogo()
        case "2":
            gerar_jogo(aleatorio=True)
        case "3":
            gerar_jogo(aleatorio=True, todos_numeros=False)
        case _:
            break
