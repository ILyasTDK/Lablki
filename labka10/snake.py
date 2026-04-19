import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

snake = [(100, 100)]
dx = 20
dy = 0

food_x = random.randrange(0, 400, 20)
food_y = random.randrange(0, 400, 20)

score = 0
level = 1
speed = 5

font = pygame.font.SysFont(None, 30)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        dx, dy = 0, -20
    if keys[pygame.K_DOWN]:
        dx, dy = 0, 20
    if keys[pygame.K_LEFT]:
        dx, dy = -20, 0
    if keys[pygame.K_RIGHT]:
        dx, dy = 20, 0

    new_head = (snake[0][0] + dx, snake[0][1] + dy)

    if new_head[0] < 0 or new_head[0] >= 400 or new_head[1] < 0 or new_head[1] >= 400:
        running = False

    snake.insert(0, new_head)

    if new_head[0] == food_x and new_head[1] == food_y:
        score += 1
        food_x = random.randrange(0, 400, 20)
        food_y = random.randrange(0, 400, 20)

        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    for s in snake:
        pygame.draw.rect(screen, (0, 255, 0), (s[0], s[1], 20, 20))

    pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, 20, 20))

    text = font.render("Score: " + str(score) + " Level: " + str(level), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()