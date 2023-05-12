import pygame

pygame.init()
login_screen = pygame.display.set_mode((1000,500))

font_type = pygame.font.SysFont("arial",16)
hello_world = font_type.render("Hello world",True,(255,255,255))
hello_world_cordinate = hello_world.get_rect()
hello_world_cordinate.topleft = (450,230)

pygame.mixer.music.load("Sounds/login_screen.wav")
pygame.mixer.music.play(-1,0.0)

work_state = True
while work_state:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            work_state =False 
        login_screen.blit(hello_world,hello_world_cordinate)
        pygame.display.update()

pygame.quit()