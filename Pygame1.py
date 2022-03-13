# Computação e Matemática
# Santiago

# Pygame: biblioteca de jogos multiplataforma (independente de sistema 
# operacional) feita para ser utilizada em conjunto com a linguagem de
# programação python. 

import pygame
pygame.init()

# Definindo variáveis de acordo com as cores
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

# Configurando a janela e preenchendo-a com preto
tela = pygame.display.set_mode([600, 600])
tela.fill(preto)

rodar = True
while rodar:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodar = False

    move = 25
    for i in range(1,6):
    # Triângulo Equilátero. Criando 5 triângulosm um do lado do outro
      pygame.draw.polygon(tela, verde, ((move,200),(move+100, 200),(move+50,113.3)))
      move+=100
          
    # Triângulo Isósceles
    pygame.draw.polygon(tela, azul, ((50,300),(450, 300),(250,250)))
    
    
    # Triângulo Retângulo
    pygame.draw.polygon(tela, vermelho, ((200, 500),(400, 500),(200,400)))

    
    pygame.display.flip()

pygame.quit()