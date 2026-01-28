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

        # objects/track.py

class Line:
    def __init__(self, index):
        self.index = index
        self.z = index * SEGMENT_LENGTH
        self.curve = 0
        self.objects = [] # აქ შეინახება ამ სეგმენტის ობიექტები
        self.color = COLORS['LIGHT'] if (index // RUMBLE_LENGTH) % 2 == 0 else COLORS['DARK']

class Track:
    def __init__(self, num_segments=2000):
        self.segments = []
        for i in range(num_segments):
            line = Line(i)
            
            # ყოველ მე-20 სეგმენტზე დავდგათ ხე გზის პირას
            if i % 20 == 0:
                # -1.5 ნიშნავს გზის მარცხნივ, 1.5 ნიშნავს გზის მარჯვნივ
                side = -1.5 if (i // 20) % 2 == 0 else 1.5
                line.objects.append({'pos': side, 'type': 'tree'})
            
            self.segments.append(line)