import pygame

class ScoreManager:
    def __init__(self):
        self.score = 0

    def add_score(self, amount = 10):
        self.score += amount

    def reset_score(self):
        self.score = 0

    def draw(self, screen):
        if not hasattr(self, 'font'):
            self.font = pygame.font.Font(None, 36)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(topleft=(10, 10))
        screen.blit(score_text, score_rect)