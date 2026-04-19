import pygame
from player import MusicPlayer

pygame.init()
screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 36)

player = MusicPlayer("music")

running = True
while running:
    screen.fill((255, 255, 255))

    text = font.render("Track: " + player.get_current_track(), True, (0, 0, 0))
    screen.blit(text, (20, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next()
            elif event.key == pygame.K_b:
                player.previous()
            elif event.key == pygame.K_q:
                running = False

    pygame.display.flip()

pygame.quit()