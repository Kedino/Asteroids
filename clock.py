import pygame
from constants import SCREEN_WIDTH
from score import ScoreManager

class GameClockManager(pygame.sprite.Sprite):
    def __init__(self, score_manager):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.start_time = pygame.time.get_ticks()
        self.paused_time = 0
        self.time_paused = 0
        self.paused = False
        self.last_scored_time = 0
        self.score_manager = score_manager

    def pause(self): 
        if not self.paused:
            self.paused_time = pygame.time.get_ticks()
            self.paused = True

    def resume(self):
        if self.paused:
            self.time_paused += pygame.time.get_ticks() - self.paused_time
            self.paused = False

    def get_elapsed_time(self):
        now = pygame.time.get_ticks()
        if self.paused:
            elapsed = self.paused_time - self.start_time - self.time_paused
        else:
            elapsed = now - self.start_time - self.time_paused
        return elapsed // 1000
    
    def update(self, dt):
        current_time = self.get_elapsed_time()
        while current_time - self.last_scored_time >= 1:
            self.last_scored_time += 1
            self.score_manager.add_score(1)

    def draw(self, screen):
        if not hasattr(self, 'font'):
            self.font = pygame.font.Font(None, 36)
        time = self.get_elapsed_time()
        clock_text = self.font.render(f"Time: {time} seconds", True, (255, 255, 255))
        clock_rect = clock_text.get_rect(midtop=(SCREEN_WIDTH // 2, 10))
        screen.blit(clock_text, clock_rect)
