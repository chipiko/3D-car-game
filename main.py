# main.py
import pygame
import sys
from settings import *
from engine.camera import Camera
from objects.track import Track

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pseudo-3D Racing")
        self.clock = pygame.time.Clock()
        
        self.camera = Camera()
        self.track = Track(2000) # 2000 სეგმენტიანი გზა
        self.speed = 0

    def draw_polygon(self, color, x1, y1, w1, x2, y2, w2):
        """ ხატავს ტრაპეციას ორ სეგმენტს შორის """
        points = [
            (x1 - w1, y1),
            (x2 - w2, y2),
            (x2 + w2, y2),
            (x1 + w1, y1)
        ]
        pygame.draw.polygon(self.screen, color, points)

    def render(self):
        self.screen.fill((135, 206, 235)) # ცისფერი ცა
        
        start_pos = int(self.camera.z / SEGMENT_LENGTH)
        
        # ვხატავთ უკნიდან წინ (Painter's Algorithm)
        for i in range(DRAW_DISTANCE, 0, -1):
            segment = self.track.segments[(start_pos + i) % len(self.track.segments)]
            
            # პროექცია
            p1 = self.camera.project(0, 0, segment.z)
            p2 = self.camera.project(0, 0, segment.z + SEGMENT_LENGTH)
            
            if p1 is None or p2 is None: continue
            
            x1, y1, w1 = p1
            x2, y2, w2 = p2
            
            # ბალახი
            self.screen.fill(segment.color['grass'], (0, y2, WIDTH, y1 - y2))
            
            # გზა და ზოლები
            self.draw_polygon(segment.color['rumble'], x1, y1, w1 * 1.1, x2, y2, w2 * 1.1)
            self.draw_polygon(segment.color['road'], x1, y1, w1, x2, y2, w2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: self.speed += 5
        elif keys[pygame.K_DOWN]: self.speed -= 5
        else: self.speed *= 0.95 # შენელება
        
        self.speed = max(0, min(self.speed, 200)) # სიჩქარის ლიმიტი
        self.camera.z += self.speed

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.update()
            self.render()
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()