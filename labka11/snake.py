import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

snake = [(100, 100)]
dx = 20
dy = 0

food_x = random.randrange(0, 400, 20)
food_y = random.randrange(0, 400, 20)
food_weight = random.choice([1, 2, 3])

food_time = time.time()

score = 0

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

    head = (snake[0][0] + dx, snake[0][1] + dy)

    if head[0] < 0 or head[0] >= 400 or head[1] < 0 or head[1] >= 400:
        running = False

    snake.insert(0, head)

    if head[0] == food_x and head[1] == food_y:
        score += food_weight
        food_x = random.randrange(0, 400, 20)
        food_y = random.randrange(0, 400, 20)
        food_weight = random.choice([1, 2, 3])
        food_time = time.time()
    else:
        snake.pop()

    if time.time() - food_time > 5:
        food_x = random.randrange(0, 400, 20)
        food_y = random.randrange(0, 400, 20)
        food_weight = random.choice([1, 2, 3])
        food_time = time.time()

    for s in snake:
        pygame.draw.rect(screen, (0, 255, 0), (s[0], s[1], 20, 20))

    pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, 20, 20))

    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(5)

pygame.quit()