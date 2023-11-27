import pygame
from sys import exit
from pygame.locals import *
import random
import tabuleiro
import elementos
import menu
pygame.init()

# funções


def Game_over():
    global game_over
    print("função game over está funcionando")
    # Exibe mensagem de game over na tela
    fonte_game_over = tabuleiro.gerador_de_fonte("Monospace", 36)
    fonte_options = tabuleiro.gerador_de_fonte("Monospace",25)
    mensagem_game_over = fonte_game_over.render("Game Over", True, (255, 0, 0))
    option1 = fonte_options.render("1 - Tentar novamente",True,(255,0,0))
    option2 = fonte_options.render("0 - sair",True,(255,0,0))
    tela.blit(mensagem_game_over, (largura_janela // 2 - 100, altura_janela // 2 - 50))
    tela.blit(option2, (largura_janela // 2 - 75, altura_janela // 2-10))
    tela.blit(option1, (largura_janela // 2 - 75, altura_janela // 2 + 20))
    pygame.display.flip()

    aguardando_tecla = True
    while aguardando_tecla:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_1:
                    reiniciar_jogo()
                    return  
                elif event.key == K_0:
                    pygame.quit()
                    exit()


def reiniciar_jogo():
    #Variaveis globais:
    game_over = False
    probabilidade_inimigo = 0
    largura_janela = 950 # largura da janela
    altura_janela  = 480 # altura da janela
    largura = 950 #largura do tabuleiro
    altura = 480 ## altura do tabuleiro
    clock = pygame.time.Clock()
    fps = 24 #valor inicial para o fps. Incrementa com o tempo
    combustivel = 600
    pontos = 0
    velocidade = 20
    distancia_minima_entre_objetos = 100
    ## Inicialização dos personagens

    ### tanques
    tanques = []
    posicao_x_tanque = random.randrange(475,950)
    posicao_y_tanque = altura_janela/random.randrange(1,150)
    velocidade_tanque_de_combustivel = 0.5

    ### inimigos
    inimigos = []
    posicao_inimigo_X = 940
    posicao_inimigo_Y = random.randrange(100,480)
    velocidade_inimigo = 4
    largura_inimigo = 20
    altura_inimigo = 20

    ### avatar
    posicao_avatar_X = 20 # personagem começa no início do eixo x do tabuleiro de jogo
    posicao_avatar_Y = 50 #personagem começa na metade do eixo y do tabuleiro
    largura_avatar = 20
    altura_avatar = 20


    ### projétil
    projetil_lista = []
    projetil = ""
    vel_projetil = 7

    ######################################################################

    #inicializadores dos elementos principais
    tela = tabuleiro.gerador_de_superficie(largura_janela,altura_janela)
    state = True #condição para o loop de menu funcionar
    #loop Menu
    while state == True:
        menu.Menu(tela,["0 - Jogar","1 - Configurações","2 - Sobre","3 - Créditos"],400,240)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_0:
                    state = False
                if event.key == K_1:
                    fonte_configurações = tabuleiro.gerador_de_fonte("Monospace", 36)
                

    mapa = tabuleiro.gerador_de_mapa(tela,largura,altura,5)
    A = elementos.desenha_quadrado(tela,(0,250,154),posicao_avatar_X,posicao_avatar_Y,largura_avatar,altura_avatar) # (Avatar do jogo)
    retangulo_referencia_A = pygame.Rect(posicao_avatar_X,posicao_avatar_Y,largura,altura)
    gera_avatar()


    #Loop de jogo
    state_main_loop = True
    while state_main_loop == True:
        pontos_e_combustível()
        for i in inimigos:
            i["posx"] -= velocidade_inimigo
        for i in tanques:
            i["posx"] -= velocidade_tanque_de_combustivel
        for i in projetil_lista:
            i.x += vel_projetil
        aparicao_objetos()

        mapa = tabuleiro.gerador_de_mapa(tela, largura, altura, 5)
        A = elementos.desenha_quadrado(tela, (0, 250, 154), posicao_avatar_X, posicao_avatar_Y, largura_avatar, altura_avatar)  # Avatar do jogo
        retangulo_referencia_A = pygame.Rect(posicao_avatar_X, posicao_avatar_Y, largura_avatar, altura_avatar)
        gera_avatar()

        for inimigo in inimigos:
            elementos.desenha_quadrado(tela,(255,0,0),inimigo["posx"],inimigo["posy"],inimigo["largura"],inimigo["altura"])
            if elementos.verifica_colisao_entre_rects(retangulo_referencia_A, pygame.Rect(inimigo["posx"], inimigo["posy"], inimigo["largura"], inimigo["altura"])):
                    print("Colisão com inimigo")
                    tela.fill((0,0,0))
                    state_main_loop = False
                    
                    
                    

        for tanque in tanques:
            elementos.desenha_quadrado(tela, (0, 206, 209), tanque["posx"], tanque["posy"], largura_avatar, altura_avatar)
            if elementos.verifica_colisao(tanque["posy"], tanque["posx"], tanque["largura"], tanque["altura"], posicao_avatar_Y, posicao_avatar_X, largura_avatar, altura_avatar):
                combustivel += 1
        
        projetil_para_remocao = []

        for projetil in projetil_lista:
            
            inimigos_para_remover = [inimigo for inimigo in inimigos if pygame.Rect(inimigo["posx"], inimigo["posy"], inimigo["altura"], inimigo["largura"]).colliderect(projetil)]
            projetil_para_remocao.extend(inimigos_para_remover)
            if pygame.Rect(inimigo["posx"], inimigo["posy"], inimigo["altura"], inimigo["largura"]).colliderect(projetil):
                projetil_lista.remove(projetil)
            pygame.draw.rect(tela, (0, 0, 255), projetil)

        # Remove inimigos atingidos por projéteis
        for inimigo in projetil_para_remocao:
            inimigos.remove(inimigo)
            pontos += 1

        # Remove projéteis que atingiram inimigos
        projetil_lista = [projetil for projetil in projetil_lista if projetil not in projetil_para_remocao]
            
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_w:
                    combustivel += 0.01
                    combustivel -= 1
                    if posicao_avatar_Y >30 :
                        posicao_avatar_Y -=velocidade
                        gera_avatar()
                        gera_mascara_para_o_avatar("w")
                        gera_avatar()
                        print(posicao_avatar_Y)
                    else: 
                        pass      
                elif event.key == K_s:
                    combustivel += 0.01
                    combustivel -=1
                    if posicao_avatar_Y < 460:
                        posicao_avatar_Y += velocidade
                        gera_avatar()
                        gera_mascara_para_o_avatar("s")
                        gera_avatar()
                elif event.key == K_t:
                    projetil = pygame.Rect(retangulo_referencia_A.right, retangulo_referencia_A.centery - 10, 10, 10)
                    projetil_lista.append(projetil)

        pygame.display.flip()           
        pygame.display.update()
        clock.tick(60)
        
        combustivel -= 0.01

def gera_avatar():
    global A; A = elementos.desenha_quadrado(tela,(0,250,154),posicao_avatar_X,posicao_avatar_Y,largura_avatar,altura_avatar) # (Avatar do jogo)
def gera_mascara_para_o_avatar(key):
    global velocidade;
    if key == "w":
        mascara = elementos.desenha_quadrado(tela,tabuleiro.backgorund_color,posicao_avatar_X,(posicao_avatar_Y)+velocidade,largura_avatar,altura_avatar)
    else: mascara = elementos.desenha_quadrado(tela,tabuleiro.backgorund_color,posicao_avatar_X,(posicao_avatar_Y)-velocidade,largura_avatar,altura_avatar)
    return mascara
def gera_mascara_objeto(key):
    global velocidade;
    if key == "w":
        mascara = elementos.desenha_quadrado(tela,tabuleiro.backgorund_color,posicao_avatar_X,(posicao_avatar_Y)+velocidade,largura_avatar,altura_avatar)
    else: mascara = elementos.desenha_quadrado(tela,tabuleiro.backgorund_color,posicao_avatar_X,(posicao_avatar_Y)-velocidade,largura_avatar,altura_avatar)
    return mascara

def pontos_e_combustível():
    
    global pontos;
    pontuacao = str(pontos)
    global combustivel;
    tanque_combustivel = str(combustivel)
    global tela;
    fonte = tabuleiro.gerador_de_fonte("Monospace",20)
    mostrador_pontuacao = tabuleiro.gerador_de_texto(pontuacao,fonte,(255,255,255))
    mostrador_combustivel = tabuleiro.gerador_de_texto(tanque_combustivel,tabuleiro.gerador_de_fonte("Monospace",20),(255,255,255))
    pygame.draw.rect(tela,(0,0,0),(50,12,100,16))
    pygame.draw.rect(tela,(0,0,0),(900,12,100,16))
    
    tela.blit(mostrador_pontuacao,(50,12))
    tela.blit(mostrador_combustivel,(900,12))


def aparicao_objetos():
   for i in inimigos:
        i["posx"] -= velocidade_inimigo

   if random.randint(0, 10) > 2:
        novo_inimigo = {"posx": 940, "posy": random.randint(50, altura_janela - altura_inimigo), "altura": altura_inimigo, "largura": largura_inimigo}
        if all(elementos.distancia_minima(novo_inimigo, inimigo, distancia_minima_entre_objetos) for inimigo in inimigos):
            inimigos.append(novo_inimigo)
   elif random.randint(0, 10)> 8:
        novo_tanque = {"posx": 940, "posy": random.randint(50, altura_janela - altura_inimigo), "altura": altura_avatar, "largura": largura_avatar}
        if all(elementos.distancia_minima(novo_tanque, tanque_de_combustivel, distancia_minima_entre_objetos) for tanque_de_combustivel in tanques):
            tanques.append(novo_tanque)

#Variaveis globais:
game_over = False
probabilidade_inimigo = 0
largura_janela = 950 # largura da janela
altura_janela  = 480 # altura da janela
largura = 950 #largura do tabuleiro
altura = 480 ## altura do tabuleiro
clock = pygame.time.Clock()
fps = 24 #valor inicial para o fps. Incrementa com o tempo
combustivel = 600
pontos = 0
velocidade = 20
distancia_minima_entre_objetos = 100
## Inicialização dos personagens

### tanques
tanques = []
posicao_x_tanque = random.randrange(475,950)
posicao_y_tanque = altura_janela/random.randrange(1,150)
velocidade_tanque_de_combustivel = 0.5

### inimigos
inimigos = []
posicao_inimigo_X = 940
posicao_inimigo_Y = random.randrange(100,480)
velocidade_inimigo = 4
largura_inimigo = 20
altura_inimigo = 20

### avatar
posicao_avatar_X = 20 # personagem começa no início do eixo x do tabuleiro de jogo
posicao_avatar_Y = 50 #personagem começa na metade do eixo y do tabuleiro
largura_avatar = 20
altura_avatar = 20


### projétil
projetil_lista = []
projetil = ""
vel_projetil = 7

######################################################################

#inicializadores dos elementos principais
tela = tabuleiro.gerador_de_superficie(largura_janela,altura_janela)
state = True #condição para o loop de menu funcionar
#loop Menu
while state == True:
    
    menu.Menu(tela,["0 - Jogar","1 - Configurações","2 - Sobre","3 - Créditos"],400,240)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_0:
                state = False
            if event.key == K_1:
                tela.fill((0,0,0))
                state = "Config"
            
while state == "Config":
    menu.configuracoes(tela,400,240)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_0:
                velocidade_inimigo = 2
                state = True
            if event.key == K_1:
                velocidade_inimigo = 4
                state = True
            if event.key == K_2:
                velocidade_inimigo = 6
                state = True

mapa = tabuleiro.gerador_de_mapa(tela,largura,altura,5)
A = elementos.desenha_quadrado(tela,(0,250,154),posicao_avatar_X,posicao_avatar_Y,largura_avatar,altura_avatar) # (Avatar do jogo)
retangulo_referencia_A = pygame.Rect(posicao_avatar_X,posicao_avatar_Y,largura,altura)
gera_avatar()


#Loop de jogo
state_main_loop = True
while state_main_loop == True:
    pontos_e_combustível()
    for i in inimigos:
        i["posx"] -= velocidade_inimigo
    for i in tanques:
        i["posx"] -= velocidade_tanque_de_combustivel
    for i in projetil_lista:
        i.x += vel_projetil
    aparicao_objetos()

    mapa = tabuleiro.gerador_de_mapa(tela, largura, altura, 5)
    A = elementos.desenha_quadrado(tela, (0, 250, 154), posicao_avatar_X, posicao_avatar_Y, largura_avatar, altura_avatar)  # Avatar do jogo
    retangulo_referencia_A = pygame.Rect(posicao_avatar_X, posicao_avatar_Y, largura_avatar, altura_avatar)
    gera_avatar()

    for inimigo in inimigos:
        elementos.desenha_quadrado(tela,(255,0,0),inimigo["posx"],inimigo["posy"],inimigo["largura"],inimigo["altura"])
        if elementos.verifica_colisao_entre_rects(retangulo_referencia_A, pygame.Rect(inimigo["posx"], inimigo["posy"], inimigo["largura"], inimigo["altura"])):
                print("Colisão com inimigo")
                tela.fill((0,0,0))
                Game_over()
                state_main_loop = False
                
                
                

    for tanque in tanques:
        elementos.desenha_quadrado(tela, (0, 206, 209), tanque["posx"], tanque["posy"], largura_avatar, altura_avatar)
        if elementos.verifica_colisao(tanque["posy"], tanque["posx"], tanque["largura"], tanque["altura"], posicao_avatar_Y, posicao_avatar_X, largura_avatar, altura_avatar):
            combustivel += 1
    
    projetil_para_remocao = []

    for projetil in projetil_lista:
        
        inimigos_para_remover = [inimigo for inimigo in inimigos if pygame.Rect(inimigo["posx"], inimigo["posy"], inimigo["altura"], inimigo["largura"]).colliderect(projetil)]
        projetil_para_remocao.extend(inimigos_para_remover)
        if pygame.Rect(inimigo["posx"], inimigo["posy"], inimigo["altura"], inimigo["largura"]).colliderect(projetil):
            projetil_lista.remove(projetil)
        pygame.draw.rect(tela, (0, 0, 255), projetil)

    # Remove inimigos atingidos por projéteis
    for inimigo in projetil_para_remocao:
        inimigos.remove(inimigo)
        pontos += 1

    # Remove projéteis que atingiram inimigos
    projetil_lista = [projetil for projetil in projetil_lista if projetil not in projetil_para_remocao]
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                combustivel += 0.01
                combustivel -= 1
                if posicao_avatar_Y >30 :
                    posicao_avatar_Y -=velocidade
                    gera_avatar()
                    gera_mascara_para_o_avatar("w")
                    gera_avatar()
                    print(posicao_avatar_Y)
                else: 
                    pass      
            elif event.key == K_s:
                combustivel += 0.01
                combustivel -=1
                if posicao_avatar_Y < 460:
                    posicao_avatar_Y += velocidade
                    gera_avatar()
                    gera_mascara_para_o_avatar("s")
                    gera_avatar()
            elif event.key == K_t:
                projetil = pygame.Rect(retangulo_referencia_A.right, retangulo_referencia_A.centery - 10, 10, 10)
                projetil_lista.append(projetil)

    pygame.display.flip()           
    pygame.display.update()
    clock.tick(60)
    
    combustivel -= 0.01


