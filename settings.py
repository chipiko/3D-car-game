# settings.py
WIDTH = 800
HEIGHT = 600
FPS = 60

# გზის პარამეტრები
ROAD_WIDTH = 2000    # გზის რეალური სიგანე (ეს თუ დიდია, გზა განიერი გამოჩნდება)
SEGMENT_LENGTH = 200 # ერთი სეგმენტის სიგრძე
RUMBLE_LENGTH = 3    # რამდენი სეგმენტია ერთი ფერის (ფერების მონაცვლეობისთვის)
DRAW_DISTANCE = 300  # რამდენი სეგმენტი გამოჩნდეს წინ
CAMERA_HEIGHT = 1000
FIELD_OF_VIEW = 100

# ფერები
COLORS = {
    'LIGHT':  {'road': '#6B6B6B', 'grass': '#10AA10', 'rumble': '#555555', 'lane': '#CCCCCC'},
    'DARK':   {'road': '#696969', 'grass': '#009A00', 'rumble': '#BBBBBB', 'lane': '#696969'},
}