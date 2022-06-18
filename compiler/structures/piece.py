from music21 import *
class Piece:
    score = None
    time_signature = None
    groups = []

    sound_duration = None
    clef = None
    articulation = None
    dynamics = None
    lyrics = None
    description = None
    key = None
    tempo = None

    def __init__(self):
        self.score = stream.Score()
        self.score.metadata = metadata.Metadata()
        