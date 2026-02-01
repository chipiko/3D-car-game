# ui/hud.py
import pygame
from settings import WIDTH, HEIGHT

class HUD:
    def __init__(self):
        # ვიყენებთ სისტემურ ფონტს
        self.font_main = pygame.font.SysFont("Arial", 36, bold=True)
        self.font_small = pygame.font.SysFont("Arial", 18, bold=True)

    def draw(self, screen, speed, distance):
        # 1. სიჩქარის მაჩვენებელი (კილომეტრებში გადაყვანილი სიჩქარე)
        speed_kmh = int(speed * 1.5) 
        speed_text = self.font_main.render(f"{speed_kmh} KM/H", True, (255, 255, 0))
        screen.blit(speed_text, (WIDTH - 180, HEIGHT - 80))

        # 2. გავლილი მანძილი
        dist_text = self.font_small.render(f"DISTANCE: {int(distance/1000)} M", True, (255, 255, 255))
        screen.blit(dist_text, (20, 20))

        # 3. დეკორატიული "Gear" (სიჩქარე)
        gear = "LO" if speed_kmh < 120 else "HI"
        gear_text = self.font_small.render(f"GEAR: {gear}", True, (0, 255, 255))
        screen.blit(gear_text, (WIDTH - 180, HEIGHT - 40))