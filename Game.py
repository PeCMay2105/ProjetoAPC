import pygame
from sys import exit
from pygame.locals import *
import math
import tabuleiro
import elementos
import menu
pygame.init()

# funções
def gera_avatar():
    global A; A = elementos.desenha_quadrado(tela,(0,250,154),posicao_avatar_X,posicao_avatar_Y,largura_avatar,altura_avatar) # (Avatar do jogo)
def gera_mascara_para_o_avatar(key):
    global velocidade;
    if key == "w":
        mascara = elementos.desenha_quadrado(tela,tabuleiro.backgorund_color,posicao_avatar_X,(posicao_avatar_Y)+velocidade,largura_avatar,altura_avatar)
    else: mascara = elementos.desenha_quadrado(tela,tabuleiro.backgorund_color,posicao_avatar_X,(posicao_avatar_Y)-velocidade,largura_avatar,altura_avatar)
    return mascara
#Variaveis globais:

largura_janela = 950 # largura da janela
altura_janela  = 480 # altura da janela
largura = 950 #largura do tabuleiro
altura = 480 ## altura do tabuleiro
clock = pygame.time.Clock()
fps = 24 #valor inicial para o fps. Incrementa com o tempo
combustivel = 600
pontos = 0
velocidade = 5

## Inicialização do avatar
posicao_avatar_X = 20 # personagem começa no início do eixo x do tabuleiro de jogo
posicao_avatar_Y = 50 #personagem começa na metade do eixo y do tabuleiro

largura_avatar = 20
altura_avatar = 20
######################################################################

#inicializadores dos elementos principais
tela = tabuleiro.gerador_de_superficie(largura_janela,altura_janela)
state = True #condição para o loop de menu funcionar
#loop Menu
while state == True:
    menu.Menu(tela,["Jogar","Configurações","Sobre","Créditos"],400,240)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_0:
                state = False
            

mapa = tabuleiro.gerador_de_mapa(tela,largura,altura,5)
A = elementos.desenha_quadrado(tela,(0,250,154),posicao_avatar_X,posicao_avatar_Y,largura_avatar,altura_avatar) # (Avatar do jogo)
gera_avatar()


#Loop de jogo
while True:


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                if posicao_avatar_Y > 0:
                    posicao_avatar_Y -=velocidade
                    gera_avatar()
                    gera_mascara_para_o_avatar("w")
                    gera_avatar()
                    
                    pygame.display.flip()
                else: 
                    pass      
            elif event.key == K_s:
                if posicao_avatar_Y < altura_janela:
                    posicao_avatar_Y += velocidade
                    gera_avatar()
                    gera_mascara_para_o_avatar("s")
                    gera_avatar()
                    pygame.display.flip()              
    pygame.display.update()
    clock.tick()
