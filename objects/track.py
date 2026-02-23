# objects/track.py
from settings import SEGMENT_LENGTH, RUMBLE_LENGTH, COLORS

class Line:
    def __init__(self, index):
        self.index = index
        self.z = index * SEGMENT_LENGTH
        self.curve = 0 # მოხვევისთვის (მოგვიანებით დასამატებლად)
        self.color = COLORS['LIGHT'] if (index // RUMBLE_LENGTH) % 2 == 0 else COLORS['DARK']
        self.screen_data = None # აქ შეინახება პროექციის შედეგი

class Track:
    def __init__(self, num_segments=500):
        self.segments = [Line(i) for i in range(num_segments)]

    def get_segment(self, z):
        return self.segments[int(z / SEGMENT_LENGTH) % len(self.segments)]