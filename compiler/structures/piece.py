from music21 import *
class Piece:
    score = stream.Score()
    clef = None
    key = None
    tempo = None
    time_signature = None
    groups = []


    def __init__(self):
        self.score.metadata = metadata.Metadata()