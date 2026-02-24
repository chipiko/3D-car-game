# objects/track.py
from settings import SEGMENT_LENGTH, RUMBLE_LENGTH, COLORS

class Line:
    def __init__(self, index):
        self.index = index
        self.z = index * SEGMENT_LENGTH
        self.curve = 0  # ყოველთვის 0, რომ არ მოუხვიოს
        self.color = COLORS['LIGHT'] if (index // RUMBLE_LENGTH) % 2 == 0 else COLORS['DARK']

class Track:
    def __init__(self, num_segments=2000):
        # ვქმნით მხოლოდ სწორ სეგმენტებს
        self.segments = [Line(i) for i in range(num_segments)]