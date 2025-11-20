import pygame
import os
from src.config import YELLOW
from src.utils.asset_loader import load_image_safe

class Animal:
    def __init__(self, x, y, animal_type, name, desc):
        self.animal_type = animal_type
        self.name = name
        self.description = desc
        self.type = "animal"
        self.highlight = False

        path = os.path.join("assets", "animals", f"{animal_type}.png")
        self.image = load_image_safe(path, scale=2)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, surface, camera):
        screen_rect = self.rect.move(-camera.x, -camera.y)
        if self.highlight:
            pygame.draw.circle(surface, YELLOW, screen_rect.center, 35, 3)
        surface.blit(self.image, screen_rect)
