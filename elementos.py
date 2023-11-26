import pygame
import random

def desenha_quadrado(surface,backgorund_color,posx,posy,largura,altura):
    rect =pygame.draw.rect(surface, backgorund_color, pygame.Rect(posx,posy,largura,altura))
    return rect

def desenha_linhas(surface,background_color,tupleStart,tupleEnd):
    line = pygame.draw.line(surface,background_color,tupleStart,tupleEnd)


def des_objetos(surface,largura_tela,altura_tela,largura_obj,altura_obj):
    fator_aleatorio = random()
    posx = largura_tela*fator_aleatorio
    posy = altura_tela*fator_aleatorio
    desenha_quadrado(surface,(255,0,0),posy,posx,largura_obj,altura_obj)


def distancia_minima(pos1,pos2,distancia_definida):
    return abs(pos1["posx"] - pos2["posx"]) > distancia_definida

def verifica_colisao(posy1,posx1,l1,a1,posy2,posx2,l2,a2):
    rect1 = pygame.Rect(posx1,posy1,a1,l1)
    rect2 = pygame.Rect(posx2,posy2,a2,l2)
    return rect1.colliderect(rect2)

def verifica_colisao_entre_rects(rect1,rect2):
    return rect1.colliderect(rect2)
    

