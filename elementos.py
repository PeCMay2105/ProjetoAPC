import pygame
def desenha_quadrado(surface,backgorund_color,posx,posy,largura,altura):
    rect =pygame.draw.rect(surface, backgorund_color, pygame.Rect(posx,posy,largura,altura))
    return rect

def desenha_linhas(surface,background_color,tupleStart,tupleEnd):
    line = pygame.draw.line(surface,background_color,tupleStart,tupleEnd)


