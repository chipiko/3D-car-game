# engine/camera.py
import math
from settings import WIDTH, HEIGHT, FIELD_OF_VIEW, CAMERA_HEIGHT

class Camera:
    def __init__(self):
        self.x = 0
        self.y = CAMERA_HEIGHT
        self.z = 0
        self.dist_to_plane = 1 / math.tan((FIELD_OF_VIEW / 2) * math.pi / 180)

    def project(self, p_x, p_y, p_z, road_width):
        relative_z = p_z - self.z
        if relative_z <= 0: return None

        scale = self.dist_to_plane / relative_z
        
        screen_x = round((WIDTH / 2) + (scale * (p_x - self.x) * WIDTH / 2))
        screen_y = round((HEIGHT / 2) - (scale * (p_y - self.y) * HEIGHT / 2))
        
        # მნიშვნელოვანია: screen_w უნდა იყოს მასშტაბირებული გზის სიგანეზე
        screen_w = round(scale * road_width * (WIDTH / 2)) 
        
        return screen_x, screen_y, screen_w