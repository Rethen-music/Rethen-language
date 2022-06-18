from music21 import *
class Voice:
    voice = None
    sounds = []

    def __init__(self):
        self.voice = stream.base.Voice()