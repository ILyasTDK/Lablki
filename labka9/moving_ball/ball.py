import pygame

class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.x = 100
        self.y = 100
        self.radius = 25
        self.speed = 20

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        width = self.screen.get_width()
        height = self.screen.get_height()

        if self.radius <= new_x <= width - self.radius:
            self.x = new_x
        if self.radius <= new_y <= height - self.radius:
            self.y = new_y

    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), self.radius)