import pygame
# variaveis de setup
largura = 600
altura = 450
pixel_por_bloco = 4
backgorund_color = (192,217,217)
cor_preta = (0,0,0)
################
def gerador_de_fonte(nome_da_fonte,tamanho):
    fonte = pygame.font.SysFont(nome_da_fonte,tamanho,True,True)
    return fonte

def gerador_de_texto(texto,fonte,cor): 
    # gera os textos que vão ser mostrados. Recebe o conteudo do texto (texto), fonte e cor
    text = fonte.render(texto,True,cor)
    return text

def gerador_de_superficie(largura,altura):
    superficie = pygame.display.set_mode((largura,altura))
    return superficie

def gerador_de_mapa(surface,largura,altura,pixels_por_unidade):
    mapa = pygame.draw.rect(surface, backgorund_color, pygame.Rect(0, 30, largura*pixels_por_unidade, altura*pixels_por_unidade))
    pygame.display.flip()
    return mapa