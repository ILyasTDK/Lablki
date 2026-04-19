import pygame
import datetime

class MickeyClock:
    def __init__(self, screen, bg, right_hand, left_hand):
        self.screen = screen
        self.bg = bg
        self.right_hand = right_hand
        self.left_hand = left_hand
        self.center = (screen.get_width() // 2, screen.get_height() // 2)

    def draw(self):
        self.screen.blit(self.bg, (0, 0))

        now = datetime.datetime.now()
        minutes = now.minute
        seconds = now.second

        minute_angle = -(minutes * 6)
        second_angle = -(seconds * 6)

        m_hand = pygame.transform.rotate(self.right_hand, minute_angle)
        m_rect = m_hand.get_rect()
        m_rect.center = self.center


        s_hand = pygame.transform.rotate(self.left_hand, second_angle)
        s_rect = s_hand.get_rect()
        s_rect.center = self.center

        self.screen.blit(m_hand, m_rect)
        self.screen.blit(s_hand, s_rect)