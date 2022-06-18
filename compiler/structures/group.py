from music21 import *
class Group:
    staff_group = None
    staffs = []
    time_signature = None

    sound_duration = None
    clef = None
    articulation = None
    dynamics = None
    lyrics = None
    description = None
    key = None
    tempo = None

    def __init__(self):
        self.measure = layout.StaffGroup()