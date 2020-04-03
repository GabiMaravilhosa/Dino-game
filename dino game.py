import pygame
pygame.init()
pygame.display.set_caption("ice crean run")
velocity_x = 0.1
tempo = pygame.time.Clock()
largura=640
altura=200
rosa = (255,105,180)
azul = (0,0,255)
carmesim = (220, 20, 60)
def tela():
    pos_x=largura/4
    pos_y= altura/1.4
    pos_z = altura/1.4
    pos_sor=largura
    pos_voa = altura/2.5
    
    salto = False
    base = 20
    lado_dino = -20
    lado_sor = -40

 
    fundo = pygame.display.set_mode((largura, altura))
    
    
    sair = True
    
    while sair:
 
        dt = tempo.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and salto == False:
                    salto = True
                    baixo = False
                
        if salto == True:
            if baixo == False:
                pos_y-=2
                pos_y = altura/2
                pos_x+=50
                if pos_y == altura/2:
                    baixo = True
            elif baixo == True:
                pos_y+=2
                pos_y = altura/1.4
                if pos_y == altura/1.4:
                    baixo = False
                    salto = False
        
        


            
        pos_sor-=2
        fundo.fill(rosa)
        dino = pygame.draw.rect(fundo, azul, [pos_x, pos_y,20,-20])
        sor_1 = pygame.draw.rect(fundo, carmesim, [pos_sor, pos_z,20, -40])
        sor_2 = pygame.draw.rect(fundo, carmesim, [pos_sor, pos_voa,20, 10])
        pygame.display.update()
        
        if dino.colliderect(sor_1) or dino.colliderect(sor_2):
            print("loser")
       
            
    pygame.quit()

tela()

