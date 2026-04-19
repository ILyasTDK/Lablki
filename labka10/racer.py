import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

car_x = 180
car_y = 500

coin_x = random.randint(0, 370)
coin_y = -50

coins = 0

font = pygame.font.SysFont(None, 30)

running = True
while running:
    screen.fill((200, 200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= 5
    if keys[pygame.K_RIGHT]:
        car_x += 5

    coin_y += 5

    if coin_y > 600:
        coin_y = -50
        coin_x = random.randint(0, 370)

    if abs(car_x - coin_x) < 40 and abs(car_y - coin_y) < 40:
        coins += 1
        coin_y = -50
        coin_x = random.randint(0, 370)

    pygame.draw.rect(screen, (0, 0, 255), (car_x, car_y, 40, 60))
    pygame.draw.circle(screen, (255, 215, 0), (coin_x, coin_y), 15)

    text = font.render("Coins: " + str(coins), True, (0, 0, 0))
    screen.blit(text, (250, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()