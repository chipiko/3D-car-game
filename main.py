import pygame
import sys
from settings import *
from engine.camera import Camera
from objects.track import Track
from objects.car import Car
# main.py-ს დასაწყისში
from ui.hud import HUD

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
        # main.py -> class Game -> def __init__
        self.hud = HUD()
        self.distance = 0 # გავლილი მანძილი


    def draw_polygon(self, color, x1, y1, w1, x2, y2, w2):
        points = [(x1 - w1, y1), (x2 - w2, y2), (x2 + w2, y2), (x1 + w1, y1)]
        pygame.draw.polygon(self.screen, color, points)

    def render(self):
        pygame.draw.rect(self.screen, (0, 150, 255), (0, 0, WIDTH, HEIGHT // 2))
        pygame.draw.rect(self.screen, (135, 206, 235), (0, HEIGHT // 4, WIDTH, HEIGHT // 4))

        player_z = self.camera.z
        start_pos = int(player_z / SEGMENT_LENGTH)
        self.camera.x = self.player.pos_x * ROAD_WIDTH
        
        track_length = len(self.track.segments) * SEGMENT_LENGTH

        # ეტაპი 1: პროექცია
        segments_to_draw = []
        x = 0
        dx = 0

        for i in range(DRAW_DISTANCE):
            segment_index = (start_pos + i) % len(self.track.segments)
            segment = self.track.segments[segment_index]
            
            segment_z = segment.z
            # თუ სეგმენტი ტრასის დასაწყისშია, მაგრამ კამერა ბოლოშია, 
            # სეგმენტს ვირტუალურად წინ ვწევთ
            if segment_index < start_pos:
                segment_z += track_length
                
            relative_z1 = segment_z - player_z
            relative_z2 = (segment_z + SEGMENT_LENGTH) - player_z
            
            p1 = self.camera.project(x, 0, relative_z1, ROAD_WIDTH)
            
            dx += segment.curve
            x += dx
            
            p2 = self.camera.project(x, 0, relative_z2, ROAD_WIDTH)
            
            if p1 is not None and p2 is not None:
                segments_to_draw.append((segment, p1, p2))

        # ეტაპი 2: ხატვა უკუღმა (ჰორიზონტიდან ახლოსკენ)
        for segment, p1, p2 in reversed(segments_to_draw):
            x1, y1, w1 = p1
            x2, y2, w2 = p2

            if y2 >= y1: continue

            pygame.draw.rect(self.screen, segment.color['grass'], (0, y2, WIDTH, y1 - y2))
            self.draw_polygon(segment.color['rumble'], x1, y1, w1 * 1.1, x2, y2, w2 * 1.1)
            self.draw_polygon(segment.color['road'], x1, y1, w1, x2, y2, w2)
            
            if segment.color == COLORS['LIGHT']:
                self.draw_polygon(COLORS['LIGHT']['lane'], x1, y1, w1 * 0.02, x2, y2, w2 * 0.02)

            for obj in segment.objects:
                sprite_x = x1 + (w1 * obj['pos'])
                sprite_w = w1 * 0.3
                sprite_h = sprite_w * 2
                pygame.draw.rect(self.screen, '#228B22', 
                                (sprite_x - sprite_w/2, y1 - sprite_h, sprite_w, sprite_h))

        # 3. მანქანა
        keys = pygame.key.get_pressed()
        tilt = 0
        if keys[pygame.K_LEFT]: tilt = -5 
        if keys[pygame.K_RIGHT]: tilt = 5

        car_surface = pygame.Surface((80, 40), pygame.SRCALPHA)
        pygame.draw.rect(car_surface, (255, 0, 0), (0, 0, 80, 40)) 
        
        rotated_car = pygame.transform.rotate(car_surface, -tilt) 
        rect = rotated_car.get_rect(center=(WIDTH // 2, HEIGHT - 80))
        self.screen.blit(rotated_car, rect)

        # 4. HUD
        self.hud.draw(self.screen, self.speed, self.distance)
    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        
        # სიჩქარის მართვა (რაც გეწერა)
        if keys[pygame.K_UP]: 
            self.speed += 2
        elif keys[pygame.K_DOWN]: 
            self.speed -= 5
        else: 
            self.speed *= 0.98 
            
        if abs(self.player.pos_x) > 1.2:
            self.speed *= 0.95 
            self.speed = min(self.speed, 60) 

        self.speed = max(0, min(self.speed, 200))
        self.camera.z += self.speed
        
        # --------------------------------------------------------
        # მთავარი ფიქსი: კამერის Z-ის განულება ახალ წრეზე!
        track_length = len(self.track.segments) * SEGMENT_LENGTH
        if self.camera.z >= track_length:
            self.camera.z -= track_length
        # --------------------------------------------------------
        
        self.distance += self.speed
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