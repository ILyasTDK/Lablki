import pygame
from clock import MickeyClock

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

bg = pygame.image.load("images/clock.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

right_hand = pygame.image.load("images/right_hand.png")
right_hand = pygame.transform.scale(right_hand, (600, 200))

left_hand = pygame.image.load("images/left_hand.png")
left_hand = pygame.transform.scale(left_hand, (600,200))

mickey = MickeyClock(screen, bg, right_hand, left_hand)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mickey.draw()

    pygame.display.flip()
    clock.tick(1)

pygame.quit()