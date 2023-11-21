import pygame
# variaveis de setup
largura = 600
altura = 450
pixel_por_bloco = 4
backgorund_color = (192,217,217)
cor_preta = (0,0,0)
################
def gerador_de_fonte(nome_da_fonte,tamanho):
    fonte = pygame.font.Font(nome_da_fonte,tamanho)
    return fonte

def gerador_de_texto(texto,fonte,cor): 
    # gera os textos que vão ser mostrados. Recebe o conteudo do texto (texto), fonte e cor
    text = fonte.render(texto,True,cor)
    return text

def gerador_de_superficie(largura,altura,tamanho):
    superficie = pygame.display.set_mode((largura*tamanho,altura*tamanho))
    return superficie

def gerador_de_mapa(surface):
    pygame.draw.rect(surface, backgorund_color, pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()
