
def storeScore(pontuacao):
    with open("score.txt","a") as arquivo:
       pontuacao = str(pontuacao) + "\n"
       arquivo.write(pontuacao)


def readScore():
    lista_pontuacao = []
    with open("score.txt","r") as arquivo:
        pontuacao = arquivo
        for item in pontuacao:  
            try:
                lista_pontuacao.append((int(item.strip())))
            except ValueError:
                print(ValueError)
    return sorted(lista_pontuacao,reverse = True)

print(readScore())
