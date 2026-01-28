import pygame
import sys
from settings import *
from engine.camera import Camera
from objects.track import Track
from objects.car import Car

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pseudo-3D Racing - Fixed Bottom")
        self.clock = pygame.time.Clock()
        
        self.camera = Camera()
        self.track = Track(2000)
        self.player = Car()
        
        self.camera.z = 0
        self.player.pos_x = 0
        self.speed = 0

    def draw_polygon(self, color, x1, y1, w1, x2, y2, w2):
        points = [(x1 - w1, y1), (x2 - w2, y2), (x2 + w2, y2), (x1 + w1, y1)]
        pygame.draw.polygon(self.screen, color, points)

    def render(self):
        # 1. ცა
        self.screen.fill((135, 206, 235)) 
        
        player_z = self.camera.z
        start_pos = int(player_z / SEGMENT_LENGTH)
        
        # კამერის ცენტრირება
        self.camera.x = self.player.pos_x * ROAD_WIDTH

        # 2. გზის ხატვა
        # ვიწყებთ DRAW_DISTANCE-დან და ჩავდივართ -10-მდე, რომ ბოლომდე დაიხატოს
        for i in range(DRAW_DISTANCE, -10, -1):
            segment_index = (start_pos + i) % len(self.track.segments)
            segment = self.track.segments[segment_index]
            
            # მნიშვნელოვანია: segment.z - player_z აძლევს გლუვ მოძრაობას
            p1 = self.camera.project(0, 0, segment.z - player_z, ROAD_WIDTH)
            p2 = self.camera.project(0, 0, (segment.z + SEGMENT_LENGTH) - player_z, ROAD_WIDTH)
            
            if p1 is None or p2 is None:
                continue
            
            x1, y1, w1 = p1
            x2, y2, w2 = p2

            # main.py - render() მეთოდის შიგნით, გზის ხატვის შემდეგ (ციკლშივე):

            # --- გზის ხატვის მერე (იგივე for i in range ციკლში) ---
            for obj in segment.objects:
                # ობიექტის X პოზიცია ეკრანზე
                # obj['pos'] არის -1.5 ან 1.5, რაც განსაზღვრავს მხარეს
                sprite_x = x1 + (w1 * obj['pos'])
                sprite_w = w1 * 0.3 # ხის ზომა გზის სიგანის პროპორციულია
                sprite_h = sprite_w * 2 # სიმაღლე

                # ხატავ ხეს (უბრალო მწვანე ოთხკუთხედი/სამკუთხედი)
                pygame.draw.rect(self.screen, '#228B22', 
                                (sprite_x - sprite_w/2, y1 - sprite_h, sprite_w, sprite_h))
            
            # თუ სეგმენტი ეკრანს ქვემოდან გასცდა, აღარ ვხატავთ
            if y2 >= y1:
                continue

            # ბალახი
            pygame.draw.rect(self.screen, segment.color['grass'], (0, y2, WIDTH, y1 - y2))
            # რამბლი
            self.draw_polygon(segment.color['rumble'], x1, y1, w1 * 1.1, x2, y2, w2 * 1.1)
            # გზა
            self.draw_polygon(segment.color['road'], x1, y1, w1, x2, y2, w2)
            
            # ხაზები
            if segment.color == COLORS['LIGHT']:
                self.draw_polygon(COLORS['LIGHT']['lane'], x1, y1, w1 * 0.02, x2, y2, w2 * 0.02)

        # 3. მანქანის ხატვა (ციკლის გარეთ!)
        # WIDTH // 2 - 40 არის ცენტრი, 80 სიგანე, 40 სიმაღლე
        pygame.draw.rect(self.screen, (255, 0, 0), (WIDTH // 2 - 40, HEIGHT - 100, 80, 40))

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        
        if keys[pygame.K_UP]: self.speed += 2
        elif keys[pygame.K_DOWN]: self.speed -= 5
        else: self.speed *= 0.98
            
        self.speed = max(0, min(self.speed, 200))
        self.camera.z += self.speed

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            self.update()
            self.render()
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    Game().run()