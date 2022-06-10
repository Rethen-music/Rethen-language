from re import S
import re
from telnetlib import XDISPLOC
from tokenize import group

from structures.sound import Sound
from structures.staff import Staff
from structures.piece import Piece
from structures.group import Group
from structures.voice import Voice
from structures.bar import Bar
from structures.expression import Expression


from matplotlib.colors import NoNorm
import ply.yacc as yacc
from music21 import *

sound_clef = None
sound_articulation = None
sound_lyrics = None
sound_dynamics = None
sound_duration = None
sound_key = None
sound_description = None
sound_tempo = None

currentMeasure = None
currentSound = None
currentStaff = None
currentGroup = None
currentPiece = None

sounds_list = []
voice_list = []
measure_list =[] 
staff_list = []
group_list = []
piece_list = []
indices = set()

def p_after_create_piece(p):
    """
    after_create_piece : empty
    | TAB AUTHOR EQUALS STRING after_create_piece
    | TAB TITLE EQUALS STRING after_create_piece
    | TAB CLEF CLEF_VALUE after_create_piece
    | TAB TEMPO EQUALS STRING after_create_piece
    | TAB TIME_SIGNATURE EQUALS TIME_SIGNATURE_VALUE after_create_piece
    | TAB KEY KEY_VALUE after_create_piece
    | TAB SOUND_DURATION EQUALS SOUND_DURATION_VALUE after_create_piece
    | TAB ARTICULATION ARTICULATION_VALUE after_create_piece
    | TAB DYNAMICS DYNAMICS_VALUE after_create_piece
    | TAB LYRICS EQUALS STRING after_create_piece
    | TAB DESCRIPTION EQUALS STRING after_create_piece
    | create_bar after_create_bar
    | create_staff after_create_staff
    | create_group after_create_group
    | create_piece after_create_piece
    """
    print("after_create_piece")
    global currentPiece
    if currentPiece is None:
        currentPiece = Piece()
    
    if(len(p)>=4):
        if(p[2] == "author"):
            currentPiece.score.metadata.composer = p[4]
        elif(p[2]=='title'):
            currentPiece.score.metadata.title = p[4]
        elif(p[2]=='key'):
            currentPiece.key = key.Key(parseKey(p[3]))
        elif(p[2]=='tempo'):
            currentPiece.tempo = tempo.MetronomeMark(p[4][1:-1])
        elif(p[2]=='time_signature'):
            currentPiece.time_signature = meter.TimeSignature(p[4][1:-1])
        elif(p[2]=='clef'):
            currentPiece.clef = clef.Clef(p[4][1:-1])
        elif p[2] == "dynamics":
            currentPiece.dynamics = dynamics.Dynamic(p[3][1:-1])
        elif p[2] == "articulation":
            if(p[3][1:-1] == "staccato"):
                currentPiece.articulation = articulations.Staccato()
            elif(p[3][1:-1] == "pizzicato"):
                currentPiece.articulation = articulations.Pizzicato()
            elif(p[3][1:-1] == "legato"):
                currentPiece.articulation = articulations.DetachedLegato()
            elif(p[3][1:-1] == "accent"):
                currentPiece.articulation = articulations.Accent()
        elif p[2] == "lyrics":
            currentPiece.lyrics = p[4][1:-1]
        elif p[2] == "description":
            currentPiece.duration = p[4][1:-1]
        elif p[2] == "sound_duration":
            currentPiece.sound_duration = p[4][1:-1]
    pass

def p_after_create_group(p):
    """
    after_create_group : empty
        | TAB TAB CLEF CLEF_VALUE after_create_group
        | TAB TAB TEMPO EQUALS STRING after_create_group
        | TAB TAB TIME_SIGNATURE EQUALS TIME_SIGNATURE_VALUE after_create_group
        | TAB TAB KEY KEY_VALUE after_create_group
        | TAB TAB SOUND_DURATION EQUALS SOUND_DURATION_VALUE after_create_group
        | TAB TAB ARTICULATION ARTICULATION_VALUE after_create_group
        | TAB TAB DYNAMICS DYNAMICS_VALUE after_create_group
        | TAB TAB LYRICS EQUALS STRING after_create_group
        | TAB TAB DESCRIPTION EQUALS STRING after_create_group
        | create_bar after_create_bar
        | create_staff after_create_staff
        | create_group after_create_group
        | create_piece after_create_piece
    """
    print("after_create_group")
    global currentGroup
    if currentGroup is None:
        currentGroup = Group()

    if len(p) == 6:
        if p[3] == "clef":
            currentGroup.clef = clef.Clef(p[4][1:-1])
        elif p[3] == "dynamics":
            currentGroup.dynamics = dynamics.Dynamic(p[4][1:-1])
        elif p[3] == "articulation":
            if(p[4][1:-1] == "staccato"):
                currentGroup.articulation = articulations.Staccato()
            elif(p[4][1:-1] == "pizzicato"):
                currentGroup.articulation = articulations.Pizzicato()
            elif(p[4][1:-1] == "legato"):
                currentGroup.articulation = articulations.DetachedLegato()
            elif(p[4][1:-1] == "accent"):
                currentGroup.articulation = articulations.Accent()
        elif p[3] == 'key':
            currentGroup.key = key.Key(parseKey(p[4][1:-1]))  
    elif len(p) == 7:
        if p[3] == "tempo":
            currentGroup.tempo = tempo.MetronomeMark(p[5][1:-1])
        elif p[3] == "lyrics":
            currentGroup.lyrics = p[5][1:-1]
        elif p[3] == "description":
            currentGroup.duration = p[5][1:-1]
        elif p[3] == "sound_duration":
            currentGroup.sound_duration = p[5][1:-1]
        else:
            currentGroup.times_signature =  meter.TimeSignature(p[5][1:-1])
    pass

def p_after_create_staff(p):
    """
    after_create_staff : empty
        | TAB TAB TAB CLEF CLEF_VALUE after_create_staff
        | TAB TAB TAB TEMPO EQUALS STRING after_create_staff
        | TAB TAB TAB TIME_SIGNATURE EQUALS TIME_SIGNATURE_VALUE after_create_staff
        | TAB TAB TAB KEY KEY_VALUE after_create_staff
        | TAB TAB TAB SOUND_DURATION EQUALS SOUND_DURATION_VALUE after_create_staff
        | TAB TAB TAB ARTICULATION ARTICULATION_VALUE after_create_staff
        | TAB TAB TAB DYNAMICS DYNAMICS_VALUE after_create_staff
        | TAB TAB TAB LYRICS EQUALS STRING after_create_staff
        | TAB TAB TAB DESCRIPTION EQUALS STRING after_create_staff
        | create_bar after_create_bar
        | create_staff after_create_staff
        | create_group after_create_group
        | create_piece after_create_piece
    """
    print("after_create_staff")
    global currentStaff 

    if currentStaff is None:
        currentStaff = Staff()

    if len(p) == 7:
        if p[4] == "clef":
            currentStaff.clef = clef.Clef(p[5][1:-1])
        elif p[4] == "dynamics":
            currentStaff.dynamics = dynamics.Dynamic(p[5][1:-1])
        elif p[4] == "articulation":
            if(p[5][1:-1] == "staccato"):
                currentStaff.articulation = articulations.Staccato()
            elif(p[5][1:-1] == "pizzicato"):
                currentStaff.articulation = articulations.Pizzicato()
            elif(p[5][1:-1] == "legato"):
                currentStaff.articulation = articulations.DetachedLegato()
            elif(p[5][1:-1] == "accent"):
                currentStaff.articulation = articulations.Accent()
        elif p[4] == 'key':
            currentStaff.key = key.Key(parseKey(p[5][1:-1]))  
    elif len(p) == 8:
        if p[4] == "tempo":
            currentStaff.tempo = tempo.MetronomeMark(p[6][1:-1])
        elif p[4] == "lyrics":
            currentStaff.lyrics = p[6][1:-1]
        elif p[4] == "description":
            currentStaff.duration = p[6][1:-1]
        elif p[5] == "sound_duration":
            currentStaff.sound_duration = p[6][1:-1]
        else:
            currentStaff.times_signature =  meter.TimeSignature(p[6][1:-1])
    pass                

def p_create_bar(p):
    """
    create_bar : TAB TAB TAB CREATE BAR COLON_SIGN
    | TAB TAB TAB CREATE BAR REPEAT ITERATION_NUMBER COLON_SIGN
    """
    global measure_list
    global currentMeasure
    global voice_list

    if currentMeasure is not None:
        measure_list.append(currentMeasure)
        currentMeasure = None
        voice_list.clear()
    pass

def p_create_staff(p):
    """
    create_staff : TAB TAB CREATE STAFF COLON_SIGN
    | TAB TAB CREATE STAFF REPEAT ITERATION_NUMBER COLON_SIGN
    """
    global voice_list
    global measure_list
    global staff_list
    global currentMeasure 
    global currentStaff

    if currentMeasure is not None:
        measure_list.append(currentMeasure)
        currentMeasure = None
        voice_list.clear()
    if currentStaff is not None:
        currentStaff.bars = measure_list
        measure_list.clear()
        staff_list.append(currentStaff)
        currentStaff = None
    pass

def p_create_group(p):
    """
    create_group : TAB CREATE GROUP COLON_SIGN
    | TAB CREATE GROUP REPEAT ITERATION_NUMBER COLON_SIGN
    """
    global voice_list
    global measure_list
    global staff_list
    global group_list
    global currentMeasure 
    global currentStaff
    global currentGroup

    if currentMeasure is not None:
        measure_list.append(currentMeasure)
        currentMeasure = None
        voice_list.clear()
    if currentStaff is not None:
        currentStaff.bars = measure_list
        measure_list.clear()
        staff_list.append(currentStaff)
        currentStaff = None
    if currentGroup is not None:
        currentGroup.staffs = staff_list
        staff_list.clear()
        group_list.append(currentGroup)
        currentGroup = None
    pass

def p_create_piece(p):
    """
    create_piece : CREATE PIECE COLON_SIGN
    | CREATE PIECE REPEAT ITERATION_NUMBER COLON_SIGN
    """
    global voice_list
    global measure_list
    global staff_list
    global group_list
    global piece_list
    global currentMeasure 
    global currentStaff
    global currentPiece
    global currentGroup

    if currentMeasure is not None:
        measure_list.append(currentMeasure)
        currentMeasure = None
        voice_list.clear()
    if currentStaff is not None:
        currentStaff.bars = measure_list
        measure_list.clear()
        staff_list.append(currentStaff)
        currentStaff = None
    if currentGroup is not None:
        currentGroup.staffs = staff_list
        staff_list.clear()
        group_list.append(currentGroup)
        currentGroup = None
    if currentPiece is not None:
        currentPiece.groups = group_list
        group_list.clear()
        piece_list.append(currentPiece)
        currentPiece = None
    pass


def p_after_create_bar(p):
    """
    after_create_bar :  empty
        | TAB TAB TAB TAB sounds_list after_create_bar
        | TAB TAB TAB TAB CLEF CLEF_VALUE after_create_bar
        | TAB TAB TAB TAB TEMPO EQUALS STRING after_create_bar
        | TAB TAB TAB TAB TIME_SIGNATURE EQUALS TIME_SIGNATURE_VALUE after_create_bar
        | TAB TAB TAB TAB KEY KEY_VALUE after_create_bar
        | TAB TAB TAB TAB SOUND_DURATION EQUALS SOUND_DURATION_VALUE after_create_bar
        | TAB TAB TAB TAB ARTICULATION ARTICULATION_VALUE after_create_bar
        | TAB TAB TAB TAB DYNAMICS DYNAMICS_VALUE after_create_bar
        | TAB TAB TAB TAB LYRICS EQUALS STRING after_create_bar
        | TAB TAB TAB TAB DESCRIPTION EQUALS STRING after_create_bar
        | create_bar after_create_bar
        | create_staff after_create_staff
        | create_group after_create_group
        | create_piece after_create_piece
    """
    print("after_create_bar")
    global voice_list
    global currentMeasure 

    if currentMeasure is None:
        currentMeasure = Bar()
    if len(p) == 7: 
            currentMeasure.voices = voice_list
    elif len(p) == 8:
        if p[5] == "clef":
            currentMeasure.clef = clef.Clef(p[6][1:-1])
        elif p[5] == "dynamics":
            currentMeasure.dynamics = dynamics.Dynamic(p[6][1:-1])
        elif p[5] == "articulation":
            if(p[6][1:-1] == "staccato"):
                currentMeasure.articulation = articulations.Staccato()
            elif(p[6][1:-1] == "pizzicato"):
                currentMeasure.articulation = articulations.Pizzicato()
            elif(p[6][1:-1] == "legato"):
                currentMeasure.articulation = articulations.DetachedLegato()
            elif(p[6][1:-1] == "accent"):
                currentMeasure.articulation = articulations.Accent()
        elif p[5] == 'key':
            currentMeasure.key = key.Key(parseKey(p[6][1:-1]))  
    elif len(p) == 9:
        if p[5] == "tempo":
            currentMeasure.tempo = tempo.MetronomeMark(p[7][1:-1])
        elif p[5] == "lyrics":
            currentMeasure.lyrics = p[7][1:-1]
        elif p[5] == "description":
            currentMeasure.duration = p[7][1:-1]
        elif p[5] == "sound_duration":
            currentMeasure.sound_duration = p[7][1:-1]
        else:
            currentMeasure.times_signature =  meter.TimeSignature(p[7][1:-1])
    pass

def p_expression_list(p):
    print("expression_list")
    """
    expression_list : expression
        | expression SEPARATOR expression_list
    """

def p_expression(p):
    """
    expression : INDEX EQUALS NUMBER
    | INDEX GREATER_EQUALS NUMBER
    | INDEX LOWER_EQUALS NUMBER
    | INDEX LOWER NUMBER
    | INDEX GREATER NUMBER
    | NUMBER
    | NUMBER LOWER INDEX LOWER NUMBER
    | NUMBER LOWER INDEX LOWER_EQUALS NUMBER
    | NUMBER LOWER_EQUALS INDEX LOWER NUMBER
    | NUMBER LOWER_EQUALS INDEX LOWER_EQUALS NUMBER
    | NUMBER GREATER INDEX GREATER NUMBER
    | NUMBER GREATER INDEX GREATER_EQUALS NUMBER
    | NUMBER GREATER_EQUALS INDEX GREATER NUMBER
    | NUMBER GREATER_EQUALS INDEX GREATER_EQUALS NUMBER
    """
    print("expression")
    global indices
    if len(p) == 2: #number
        number = p[1] - 1
        if number < len(sounds_list):
            indices.add(number)
        else:
            raise Exception("Index out of range")

    elif len(p) == 4: #index sign number
        number = p[3] - 1

        if p[2] == "=":
            if number < len(sounds_list):
                indices.add(number)
            else:
                raise Exception("Index out of range")
        elif p[2] == ">=":
            numbers = set(range(len(sounds_list))).intersection(set(range(number,len(sounds_list))))
            if len(numbers) == 0:
                raise Exception("Wrong expression: i>={}".format(number))
            else:
                indices.add(numbers)

        elif p[2] == "<=":
            numbers = set(range(len(sounds_list))).intersection(set(range(0,number)))
            if len(numbers) == 0:
                raise Exception("Wrong expression: i<={}".format(number))
            else:
                indices.add(numbers)

        elif p[2] == ">":
            numbers = set(range(len(sounds_list))).intersection(set(range(number+1,len(sounds_list))))
            if len(numbers) == 0:
                raise Exception("Wrong expression: i>{}".format(number))
            else:
                indices.add(numbers)
        elif p[2] == "<":
            numbers = set(range(len(sounds_list))).intersection(set(range(0,number-1)))
            if len(numbers) == 0:
                raise Exception("Wrong expression: i<{}".format(number))
            else:
                indices.add(numbers)

def repeat_sounds(x):
    print("repeat_sounds")
    global sounds_list
    result = []
    for i in range(0,x):
        result += sounds_list
    sounds_list = result

def apply_attributes():
    print("apply_attributes")
    global sounds_list
    global sound_clef
    global sound_articulation
    global sound_lyrics
    global sound_dynamics
    global sound_duration
    global sound_key
    global sound_description
    global indices
    
    for i in indices:
        if sound_clef != None: 
            sounds_list[i].clef = sound_clef
        if sound_key != None: 
            sounds_list[i].key = sound_key
        if sound_dynamics != None:
            sounds_list[i].dynamics = sound_dynamics
        if sound_articulation != None: sounds_list[i].note.articulations.append(sound_articulation)            
        if sound_lyrics != None: sounds_list[i].note.addLyric(sound_lyrics)
        if sound_duration != None: sounds_list[i].note.duration = sound_duration 

    sound_clef = None
    sound_articulation = None
    sound_lyrics = None
    sound_dynamics = None
    sound_duration = None
    sound_key = None
    sound_description = None

def p_repeat(p):
    """
    repeat : REPEAT ITERATION_NUMBER
    """
    print("repeat")
    global sounds_list
    repeat_sounds(p[5][1:-1])
    pass


def p_apply(p):
    """
    apply : APPLY LEFT_SQUARE_BRACKET additionals_for_sound RIGHT_SQUARE_BRACKET FOR LEFT_SQUARE_BRACKET expression_list RIGHT_SQUARE_BRACKET
    """
    print("apply")
    global sounds_list
    global indices
    apply_attributes()
    indices.clear()
    pass

def p_sounds_list(p):
    """
    sounds_list : LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET
        | LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET 
        | LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET apply
        | LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET repeat AND apply
        | LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET apply AND repeat
    """
    print("sounds list")
    global sounds_list
    global voice_list
    voice = Voice()
    voice.sounds = sounds_list
    sounds_list.clear()
    voice_list.append(voice)
    pass

def  p_sounds(p):
    """
    sounds : sound
        | rest
        | sound SEPARATOR sounds
        | rest SEPARATOR sounds
    """
    print("sounds")
    pass

def p_sound(p):
    """
    sound :   LEFT_CURLY_BRACKET expression_for_sound  RIGHT_CURLY_BRACKET
    """
    print("sound")
    pass

def p_rest(p):
    """
    rest : LEFT_CURLY_BRACKET expression_for_rest RIGHT_CURLY_BRACKET
    """ 
    print("rest")
    pass  
   
# first example
"""
n = note.Note(p[2])
d = duration.Duration()
numbers =  [float(x) for x in p[4][1:-1].split('/')]
if len(numbers) == 2:
    d.quarterLength = numbers[0]/numbers[1] * 4
elif len(numbers) == 1:
    d.quarterLength = numbers[0] * 4
n.duration = d
n.show()
"""




def p_expression_for_sound(p):
    """
    expression_for_sound : SOUND_NAME additionals_for_sound
    """
    print("expression for sound")
    global sound_clef
    global sound_articulation
    global sound_lyrics
    global sound_dynamics
    global sound_duration
    global sound_key
    global sound_description
    global sound_tempo

    global sounds_list
    global currentSound
    
    
    currentSound = Sound()
    if sound_lyrics != None: currentSound.lyrics = sound_lyrics
        #currentSound.note.addLyric(sound_lyrics)
    if sound_articulation != None: currentSound.articulation = sound_articulation
        #currentSound.note.articulations.append(sound_articulation)
    if sound_clef != None: currentSound.clef = sound_clef
    if sound_key != None: currentSound.key = sound_key
    if sound_dynamics != None:currentSound.dynamics = sound_dynamics
    # dynamics.Dynamic(p[4][1:-1])
    if sound_duration != None: currentSound.sound_duration = sound_duration
        #currentSound.note.duration = sound_duration
    if sound_description != None: currentSound.description = sound_description
    if sound_tempo != None: currentSound.tempo = sound_tempo
        #currentSound.note.addLyric(sound_description)

    sounds_list.append(currentSound)



    currentSound = None
    sound_articulation = None
    sound_lyrics = None
    sound_duration = None
    sound_description = None
    sound_clef = None
    sound_dynamics = None
    sound_key = None
    sound_tempo = None

    pass
   

def p_expression_for_rest(p):
    """
    expression_for_rest : REST additionals_for_rest
    """
    print("expression_for_rest")
    global sound_clef
    global sound_articulation
    global sound_lyrics
    global sound_dynamics
    global sound_duration
    global sound_key
    global sound_description
    global currentSound


    currentSound = note.Rest()
    pass



def parseKey(str):
    print("parseKey")
    str = str[1:-1]
    letter = str[0]
    sign = None
    if len(str) > 1:
        if str[1:] == '-flat':
            sign = '-'
        elif str[1:] == '-sharp':
            sign = '#'
        return letter + sign
    return letter



def p_additionals_for_sound(p):
    """
    additionals_for_sound : empty
        | SEPARATOR SOUND_DURATION_VALUE additionals_for_sound
        | SEPARATOR CLEF CLEF_VALUE additionals_for_sound
        | SEPARATOR ARTICULATION ARTICULATION_VALUE additionals_for_sound
        | SEPARATOR DYNAMICS DYNAMICS_VALUE additionals_for_sound
        | SEPARATOR LYRICS EQUALS STRING additionals_for_sound
        | SEPARATOR DESCRIPTION EQUALS STRING additionals_for_sound
        | SEPARATOR KEY KEY_VALUE additionals_for_sound
        | SEPARATOR TEMPO EQUALS STRING additionals_for_sound
    """
    print("additionals for sound")

    global sound_clef
    global sound_articulation
    global sound_lyrics
    global sound_dynamics
    global sound_duration
    global sound_key
    global sound_description
    global sounds_list
    global sound_tempo

    if len(p) >= 3:
        if(p[2] == "key"): 
            sound_key = key.Key(parseKey(p[3]))
        elif(p[2] =="description"):
            if sound_duration is None:
                sound_duration = p[4][1:-1]
        elif(p[2] =="lyrics"):  
            if sound_lyrics is None:
                sound_lyrics = p[4][1:-1]
        elif(p[2] =="dynamics"):  
            if sound_dynamics is None:
                sound_dynamics = dynamics.Dynamic(p[4][1:-1])
        elif(p[2] =="articulation"):
            if sound_articulation is None:
                if(p[4][1:-1] == "staccato"):
                    sound_articulation = articulations.Staccato()
                elif(p[4][1:-1] == "pizzicato"):
                    sound_articulation = articulations.Pizzicato()
                elif(p[4][1:-1] == "legato"):
                    sound_articulation = articulations.DetachedLegato()
                elif(p[4][1:-1] == "accent"):
                    sound_articulation = articulations.Accent()
        elif(p[2] =="clef"):
            if sound_clef is None:
                if(p[3][1:-1] == "treble"):
                    sound_clef = clef.TrebleClef()
                elif(p[3][1:-1]  == "bass"):
                    sound_clef = clef.BassClef()
                elif(p[3][1:-1]  == "alto"):
                    sound_clef = clef.AltoClef() 
        elif(p[2] =="tempo"):  
            sound_tempo = tempo.MetronomeMark(p[4][1:-1])
        else: #sound duration
            if sound_duration is None:
                d = duration.Duration()
                numbers =  [float(x) for x in p[2][1:-1].split('/')]
                if len(numbers) == 2:
                    d.quarterLength = numbers[0]/numbers[1] * 4
                elif len(numbers) == 1:
                    d.quarterLength = numbers[0] * 4
                sound_duration = d
    pass

def p_additionals_for_rest(p):
    """
    additionals_for_rest : empty
    | SEPARATOR SOUND_DURATION_VALUE additionals_for_sound
    | SEPARATOR CLEF CLEF_VALUE additionals_for_sound
    | SEPARATOR DESCRIPTION EQUALS STRING additionals_for_sound
    | SEPARATOR KEY KEY_VALUE additionals_for_sound
    """
    print("additionals_for_rest")
    pass

def p_empty(p):
    'empty :'
    print("empty")
    pass

def inherit_attributes():
    for piece in piece_list:
        for group in piece.groups:
            if group.sound_duration is None: group.sound_duration = piece.sound_duration
            if group.clef is None: group.clef = piece.clef
            if group.articulation is None: group.articulation = piece.articulation
            if group.dynamics is None: group.dynamics = piece.dynamics
            if group.lyrics is None: group.lyrics = piece.lyrics
            if group.description is None: group.description = piece.description
            if group.key is None: group.key = piece.key
            if group.tempo is None: group.tempo = piece.tempo
            if group.time_signature is None: group.time_signature = piece.time_signature

            for staff in group.staffs:
                if staff.sound_duration is None: staff.sound_duration = group.sound_duration
                if staff.clef is None: staff.clef = group.clef
                if staff.articulation is None: staff.articulation = group.articulation
                if staff.dynamics is None: staff.dynamics = group.dynamics
                if staff.lyrics is None: staff.lyrics = group.lyrics
                if staff.description is None: staff.description = group.description
                if staff.key is None: staff.key = group.key
                if staff.tempo is None: staff.tempo = group.tempo
                if staff.time_signature is None: staff.time_signature = piece.time_signature

                for bar in staff.bars:
                    if bar.sound_duration is None: bar.sound_duration = staff.sound_duration
                    if bar.clef is None: bar.clef = staff.clef
                    if bar.articulation is None: bar.articulation = staff.articulation
                    if bar.dynamics is None: bar.dynamics = staff.dynamics
                    if bar.lyrics is None: bar.lyrics = staff.lyrics
                    if bar.description is None: bar.description = staff.description
                    if bar.key is None: bar.key = staff.key
                    if bar.tempo is None: bar.tempo = staff.tempo
                    if bar.time_signature is None: bar.time_signature = piece.time_signature

                    for voice in bar.voices:
                        for sound in voice.sounds:
                            if sound.sound_duration is None: sound.sound_duration = bar.sound_duration
                            if sound.clef is None: sound.clef = bar.clef
                            if sound.articulation is None: sound.articulation = bar.articulation
                            if sound.dynamics is None: sound.dynamics = bar.dynamics
                            if sound.lyrics is None: sound.lyrics = bar.lyrics
                            if sound.description is None: sound.description = bar.description
                            if sound.key is None: sound.key = bar.key
                            if sound.tempo is None: sound.tempo = bar.tempo
                            if sound.time_signature is None: sound.time_signature = piece.time_signature
    pass



def showNotes():
    print("showNotes")
    piece_list[0].score.show()