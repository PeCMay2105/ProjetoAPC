
def storeScore(pontuacao):
    with open("score.txt","w") as arquivo:
        arquivo.write(pontuacao)


def readScore():
    lista_pontos = []
    with open("score.txt","r") as arquivo:
        pontuacao = arquivo.read()
        for item in pontuacao:
            lista_pontos.append(item)
    return ("pontuação: " + pontuacao)


print("pontuação: "+readScore())