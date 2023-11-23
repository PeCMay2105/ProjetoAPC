from pygame import *
import tabuleiro

def Menu(superficie,opcoes,posicaoX,posicaoY):
    fonte = tabuleiro.gerador_de_fonte("Monospace",20)
    fonte_titulo = tabuleiro.gerador_de_fonte("Monospace",50)
    texto = tabuleiro.gerador_de_texto("Ascentions of Lamar",fonte_titulo,(105,85,205))
    superficie.blit(texto,(posicaoX-250,posicaoY-100))
        
    for i in range(len(opcoes)):
        texto = tabuleiro.gerador_de_texto(opcoes[i],fonte,(255,255,255))

        superficie.blit(texto,(posicaoX,posicaoY))
        posicaoY += 50

    



