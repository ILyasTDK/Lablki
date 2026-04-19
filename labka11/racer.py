import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

car_x = 180
car_y = 500

enemy_x = 180
enemy_y = -100
enemy_speed = 5

coin_x = random.randint(0, 370)
coin_y = -50
coin_weight = random.choice([1, 2, 3])

coins = 0
N = 5  

font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 60)

running = True
game_over = False

while running:
    screen.fill((200, 200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car_x -= 5
        if keys[pygame.K_RIGHT]:
            car_x += 5

        coin_y += 5

        if coin_y > 600:
            coin_y = -50
            coin_x = random.randint(0, 370)
            coin_weight = random.choice([1, 2, 3])

        if abs(car_x - coin_x) < 40 and abs(car_y - coin_y) < 40:
            coins += coin_weight
            coin_y = -50
            coin_x = random.randint(0, 370)
            coin_weight = random.choice([1, 2, 3])

        if coins >= N:
            enemy_speed = 8

        enemy_y += enemy_speed
        if enemy_y > 600:
            enemy_y = -100

        if abs(car_x - enemy_x) < 40 and abs(car_y - enemy_y) < 60:
            game_over = True

    pygame.draw.rect(screen, (0, 0, 255), (car_x, car_y, 40, 60))
    pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, 40, 60))
    pygame.draw.circle(screen, (255, 215, 0), (coin_x, coin_y), 15)

    text = font.render("Coins: " + str(coins), True, (0, 0, 0))
    screen.blit(text, (250, 10))

    if game_over:
        over_text = big_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(over_text, (60, 250))

    pygame.display.update()
    clock.tick(60)

pygame.quit()