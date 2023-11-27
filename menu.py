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

    
def configuracoes(superficie,posicaoX,PosicaoY):
    superficie.fill((0,0,0))

    fonte_titulo = tabuleiro.gerador_de_fonte("Monospace",50)
    fonte_subtitulo = tabuleiro.gerador_de_fonte("Monospace",40)
    fonte = tabuleiro.gerador_de_fonte("Monospace",20)
    texto = tabuleiro.gerador_de_texto("Configurações",fonte_titulo,(105,85,205))
    texto_dificuldade = tabuleiro.gerador_de_texto("Selecione a dificuldade",fonte_subtitulo,(105,85,205))
    facil = tabuleiro.gerador_de_texto("0 - facil",fonte,(105,85,205))
    medio = tabuleiro.gerador_de_texto("1 - medio",fonte,(105,85,205))
    dificil = tabuleiro.gerador_de_texto("2 - dificil",fonte,(105,85,205))
    superficie.blit(texto,(posicaoX-250,PosicaoY-100))
    superficie.blit(texto_dificuldade,(posicaoX-250,PosicaoY))
    superficie.blit(facil,(posicaoX-250,PosicaoY+50))
    superficie.blit(medio,(posicaoX-250,PosicaoY+100))
    superficie.blit(dificil,(posicaoX-250,PosicaoY+150))
    display.flip()