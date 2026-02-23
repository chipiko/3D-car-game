# settings.py
WIDTH = 800
HEIGHT = 600
FPS = 60

# გზის პარამეტრები
ROAD_WIDTH = 2000
SEGMENT_LENGTH = 200  # თითოეული "ხაზის" სიგრძე
RUMBLE_LENGTH = 3      # რამდენი სეგმენტია ერთი ფერის (ზოლებისთვის)
FIELD_OF_VIEW = 100    # FOV
CAMERA_HEIGHT = 1000   # კამერის სიმაღლე მიწიდან
DRAW_DISTANCE = 300    # რამდენი სეგმენტი გამოჩნდეს ეკრანზე

# ფერები
COLORS = {
    'LIGHT':  {'road': '#6B6B6B', 'grass': '#10AA10', 'rumble': '#555555', 'lane': '#CCCCCC'},
    'DARK':   {'road': '#696969', 'grass': '#009A00', 'rumble': '#BBBBBB', 'lane': '#696969'},
}