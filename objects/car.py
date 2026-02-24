# objects/car.py
import pygame

class Car:
    def __init__(self):
        self.pos_x = 0  # 0 არის ზუსტი ცენტრი
        self.speed = 0

    def update(self, keys):
        # მართვა ისრებით
        if keys[pygame.K_LEFT]: self.pos_x -= 0.05
        if keys[pygame.K_RIGHT]: self.pos_x += 0.05
        
        # არ გადავიდეთ გზის მიღმა ძალიან შორს
        self.pos_x = max(-2, min(self.pos_x, 2))