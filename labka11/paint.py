import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
screen.fill((255, 255, 255))

color = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255, 0, 0)
            if event.key == pygame.K_g:
                color = (0, 255, 0)
            if event.key == pygame.K_b:
                color = (0, 0, 255)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if pygame.key.get_pressed()[pygame.K_1]:
                pygame.draw.rect(screen, color, (x, y, 50, 50), 2)

            if pygame.key.get_pressed()[pygame.K_2]:
                pygame.draw.polygon(screen, color, [(x, y), (x, y+50), (x+50, y+50)], 2)

            if pygame.key.get_pressed()[pygame.K_3]:
                pygame.draw.polygon(screen, color, [(x, y), (x-30, y+50), (x+30, y+50)], 2)

            if pygame.key.get_pressed()[pygame.K_4]:
                pygame.draw.polygon(screen, color, [(x, y-30), (x-30, y), (x, y+30), (x+30, y)], 2)

    pygame.display.update()

pygame.quit()