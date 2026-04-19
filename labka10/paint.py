import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
screen.fill((255, 255, 255))

color = (0, 0, 0)
mode = "draw"

drawing = False
start_pos = (0, 0)

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

            if event.key == pygame.K_e:
                mode = "erase"
            if event.key == pygame.K_t:
                mode = "rect"
            if event.key == pygame.K_c:
                mode = "circle"
            if event.key == pygame.K_d:
                mode = "draw"

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if mode == "rect":
                pygame.draw.rect(screen, color, (start_pos[0], start_pos[1],
                                                 end_pos[0]-start_pos[0],
                                                 end_pos[1]-start_pos[1]), 2)

            if mode == "circle":
                r = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, color, start_pos, r, 2)

        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "draw":
                pygame.draw.circle(screen, color, event.pos, 3)
            if mode == "erase":
                pygame.draw.circle(screen, (255, 255, 255), event.pos, 10)

    pygame.display.update()

pygame.quit()