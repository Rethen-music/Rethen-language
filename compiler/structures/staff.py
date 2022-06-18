from music21 import *
class Staff:
    staff = None
    time_signature = None
    bars= []

    sound_duration = None
    clef = None
    articulation = None
    dynamics = None
    lyrics = None
    description = None
    key = None
    tempo = None

    def __init__(self):
        self.staff = layout.Staff()