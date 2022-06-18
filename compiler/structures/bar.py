from music21 import *
class Bar:
    measure = None
    time_signature = None
    voices = []
    
    sound_duration = None
    clef = None
    articulation = None
    dynamics = None
    lyrics = None
    description = None
    key = None
    tempo = None
    
    def __init__(self):
        self.measure = stream.base.Measure()