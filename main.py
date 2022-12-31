import csv
import random


def carregar_resultados():
    try:
        resultados = []

        with open("./resultados/todos_resultados_2022_12_22.csv", 'r') as resultados_csv:
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


def conferir_jogo(jogo):
    resultados = carregar_resultados()

    for resultado in resultados:
        if jogo == resultado["jogo"]:
            print("Jogo já sorteado!")
            return True
    else:
        print("Jogo nunca sorteado!")
        return False


def gerar_jogo():
    jogo = random.sample(range(1, 61), 6)
    jogo.sort()

    if conferir_jogo(jogo):
        print("gerando novo jogo...")
        gerar_jogo()
    else:
        print(jogo)

def criar_jogo():
    jogo = input("Digite os números seguido de espaço: ").split(' ')
    jogo.sort()

    if len(jogo) == 6:
        if conferir_jogo(jogo):
            print("Digite outros números...")
            criar_jogo()
        else:
            print(jogo)
    else:
        print("Digite 6 números!")
        criar_jogo()

criar_jogo()
# gerar_jogo()
