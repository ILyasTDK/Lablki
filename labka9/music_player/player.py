import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        self.tracks = [os.path.join(music_folder, f) for f in os.listdir(music_folder)]
        self.index = 0
        pygame.mixer.init()

    def play(self):
        pygame.mixer.music.load(self.tracks[self.index])
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.index = (self.index + 1) % len(self.tracks)
        self.play()

    def previous(self):
        self.index = (self.index - 1) % len(self.tracks)
        self.play()

    def get_current_track(self):
        return os.path.basename(self.tracks[self.index])