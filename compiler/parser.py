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
import copy

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

def p_piece_attribute(p):
    """
    piece_attribute : AUTHOR EQUALS STRING
    | TITLE EQUALS STRING
    | CLEF CLEF_VALUE
    | TEMPO EQUALS STRING
    | TIME_SIGNATURE TIME_SIGNATURE_VALUE
    | KEY KEY_VALUE
    | SOUND_DURATION EQUALS SOUND_DURATION_VALUE
    | ARTICULATION ARTICULATION_VALUE
    | DYNAMICS DYNAMICS_VALUE
    | LYRICS EQUALS STRING
    | DESCRIPTION EQUALS STRING
    """
    print("piece_attribute")
    global currentPiece
    
    if(len(p)>=3):
        if(p[1] == "author"):
            currentPiece.score.metadata.composer = p[3]
        elif(p[1]=='title'):
            currentPiece.score.metadata.title = p[3]
        elif(p[1]=='key'):
            currentPiece.key = key.Key(parseKey(p[2]))
        elif(p[1]=='tempo'):
            currentPiece.tempo = tempo.MetronomeMark(p[3][1:-1])
        elif(p[1]=='time_signature'):
            currentPiece.time_signature = meter.TimeSignature(p[2][1:-1])
        elif(p[1]=='clef'):
            currentPiece.clef = clef.clefFromString(p[2][1:-1])
        elif p[1] == "dynamics":
            currentPiece.dynamics = dynamics.Dynamic(p[2][1:-1])
        elif p[1] == "articulation":
            if(p[2][1:-1] == "staccato"):
                currentPiece.articulation = articulations.Staccato()
            elif(p[2][1:-1] == "pizzicato"):
                currentPiece.articulation = articulations.Pizzicato()
            elif(p[2][1:-1] == "legato"):
                currentPiece.articulation = articulations.DetachedLegato()
            elif(p[2][1:-1] == "accent"):
                currentPiece.articulation = articulations.Accent()
        elif p[1] == "lyrics":
            currentPiece.lyrics = p[3][1:-1]
        elif p[1] == "description":
            currentPiece.duration = p[3][1:-1]
        elif p[1] == "sound_duration":
            currentPiece.sound_duration = p[3][1:-1]
    pass


def p_group_attribute(p):
    """
    group_attribute : CLEF CLEF_VALUE
        | TEMPO EQUALS STRING
        | TIME_SIGNATURE TIME_SIGNATURE_VALUE
        | KEY KEY_VALUE
        | SOUND_DURATION EQUALS SOUND_DURATION_VALUE
        | ARTICULATION ARTICULATION_VALUE
        | DYNAMICS DYNAMICS_VALUE
        | LYRICS EQUALS STRING
        | DESCRIPTION EQUALS STRING
    """
    print("group_attribute")
    global currentGroup

    if len(p) == 3:
        if p[1] == "clef":
            currentGroup.clef = clef.clefFromString(p[2][1:-1])
        elif p[1] == "dynamics":
            currentGroup.dynamics = dynamics.Dynamic(p[2][1:-1])
        elif p[1] == "articulation":
            if(p[2][1:-1] == "staccato"):
                currentGroup.articulation = articulations.Staccato()
            elif(p[2][1:-1] == "pizzicato"):
                currentGroup.articulation = articulations.Pizzicato()
            elif(p[2][1:-1] == "legato"):
                currentGroup.articulation = articulations.DetachedLegato()
            elif(p[2][1:-1] == "accent"):
                currentGroup.articulation = articulations.Accent()
        elif p[1] == 'key':
            currentGroup.key = key.Key(parseKey(p[2][1:-1]))  
    elif len(p) == 4:
        if p[1] == "tempo":
            currentGroup.tempo = tempo.MetronomeMark(p[3][1:-1])
        elif p[1] == "lyrics":
            currentGroup.lyrics = p[3][1:-1]
        elif p[1] == "description":
            currentGroup.duration = p[3][1:-1]
        elif p[1] == "sound_duration":
            currentGroup.sound_duration = p[3][1:-1]
        else:
            currentGroup.times_signature =  meter.TimeSignature(p[3][1:-1])
    pass

def p_staff_attribute(p):
    """
    staff_attribute : CLEF CLEF_VALUE
        | TEMPO EQUALS STRING
        | TIME_SIGNATURE TIME_SIGNATURE_VALUE
        | KEY KEY_VALUE
        | SOUND_DURATION EQUALS SOUND_DURATION_VALUE
        | ARTICULATION ARTICULATION_VALUE
        | DYNAMICS DYNAMICS_VALUE
        | LYRICS EQUALS STRING
        | DESCRIPTION EQUALS STRING
    """
    print("staff_attribute")
    global currentStaff 

    if len(p) == 3:
        if p[1] == "clef":
            currentStaff.clef = clef.clefFromString(p[2][1:-1])
        elif p[1] == "dynamics":
            currentStaff.dynamics = dynamics.Dynamic(p[2][1:-1])
        elif p[1] == "articulation":
            if(p[2][1:-1] == "staccato"):
                currentStaff.articulation = articulations.Staccato()
            elif(p[2][1:-1] == "pizzicato"):
                currentStaff.articulation = articulations.Pizzicato()
            elif(p[2][1:-1] == "legato"):
                currentStaff.articulation = articulations.DetachedLegato()
            elif(p[2][1:-1] == "accent"):
                currentStaff.articulation = articulations.Accent()
        elif p[1] == 'key':
            currentStaff.key = key.Key(parseKey(p[2][1:-1]))  
    elif len(p) == 4:
        if p[1] == "tempo":
            currentStaff.tempo = tempo.MetronomeMark(p[3][1:-1])
        elif p[1] == "lyrics":
            currentStaff.lyrics = p[3][1:-1]
        elif p[1] == "description":
            currentStaff.duration = p[3][1:-1]
        elif p[1] == "sound_duration":
            currentStaff.sound_duration = p[3][1:-1]
        else:
            currentStaff.times_signature =  meter.TimeSignature(p[2][1:-1])
    pass                

def p_create_bar(p):
    """
    create_bar : CREATE BAR COLON_SIGN
    | CREATE BAR REPEAT ITERATION_NUMBER COLON_SIGN
    """
    print("create_bar")
    global measure_list
    global currentMeasure
    global voice_list

    if currentMeasure is not None:
        currentMeasure.voices = copy.deepcopy(voice_list)
        measure_list.append(currentMeasure)
        currentMeasure = None
        voice_list.clear()
    if currentMeasure is None:
        currentMeasure = Bar()
    pass

def p_create_staff(p):
    """
    create_staff : CREATE STAFF COLON_SIGN
    | CREATE STAFF REPEAT ITERATION_NUMBER COLON_SIGN
    """
    print("create_staff")
    global voice_list
    global measure_list
    global staff_list
    global currentMeasure 
    global currentStaff

    if currentMeasure is not None:
        currentMeasure.voices = copy.deepcopy(voice_list)
        measure_list.append(currentMeasure)
        currentMeasure = None
        voice_list.clear()
    if currentStaff is not None:
        currentStaff.bars = copy.deepcopy(measure_list)
        measure_list.clear()
        staff_list.append(currentStaff)
        currentStaff = None
        
    if currentStaff is None:
        currentStaff = Staff()
    pass

def p_create_group(p):
    """
    create_group : CREATE GROUP COLON_SIGN
    | CREATE GROUP REPEAT ITERATION_NUMBER COLON_SIGN
    """
    print("create_group")
    global voice_list
    global measure_list
    global staff_list
    global group_list
    global currentMeasure 
    global currentStaff
    global currentGroup

    if currentMeasure is not None:
        currentMeasure.voices = copy.deepcopy(voice_list)
        measure_list.append(currentMeasure)
        currentMeasure = None
        voice_list.clear()
    if currentStaff is not None:
        currentStaff.bars = copy.deepcopy(measure_list)
        measure_list.clear()
        staff_list.append(currentStaff)
        currentStaff = None
    if currentGroup is not None:
        currentGroup.staffs = copy.deepcopy(staff_list)
        staff_list.clear()
        group_list.append(currentGroup)
        currentGroup = None
    
    if currentGroup is None:
        currentGroup = Group()

    pass

def p_start(p):
    """
    start : create_piece tabs
    """
    print("start")
    pass

def p_create_piece(p):
    """
    create_piece : CREATE PIECE COLON_SIGN
    | CREATE PIECE REPEAT ITERATION_NUMBER COLON_SIGN
    """
    print("create_piece")

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
        currentMeasure.voices = copy.deepcopy(voice_list)
        measure_list.append(currentMeasure)
        currentMeasure = None
        voice_list.clear()
    if currentStaff is not None:
        currentStaff.bars = copy.deepcopy(measure_list)
        measure_list.clear()
        staff_list.append(currentStaff)
        currentStaff = None
    if currentGroup is not None:
        currentGroup.staffs = copy.deepcopy(staff_list)
        staff_list.clear()
        group_list.append(currentGroup)
        currentGroup = None
    if currentPiece is not None:
        currentPiece.groups = copy.deepcopy(group_list)
        group_list.clear()
        piece_list.append(currentPiece)
        currentPiece = None

    if currentPiece is None:
        currentPiece = Piece()
    pass

def p_zero_tabs(p):
    """
    zero_tabs : create_piece
    """

def p_one_tab(p):
    """
    one_tab : piece_attribute
    | create_group
    """

def p_two_tabs(p):
    """
    two_tabs : group_attribute
    | create_staff
    """    

def p_three_tabs(p):
    """
    three_tabs : staff_attribute
    | create_bar
    """

def p_four_tabs(p):
    """
    four_tabs : bar_attribute
    """
    
def p_tabs(p):
    """
    tabs : empty 
    | zero_tabs tabs
    | TAB one_tab tabs
    | TAB TAB two_tabs tabs
    | TAB TAB TAB three_tabs tabs
    | TAB TAB TAB TAB four_tabs tabs
    """

def p_bar_attribute(p):
    """
    bar_attribute : sounds_list
        | CLEF CLEF_VALUE
        | TEMPO EQUALS STRING
        | TIME_SIGNATURE TIME_SIGNATURE_VALUE
        | KEY KEY_VALUE
        | SOUND_DURATION EQUALS SOUND_DURATION_VALUE
        | ARTICULATION ARTICULATION_VALUE
        | DYNAMICS DYNAMICS_VALUE
        | LYRICS EQUALS STRING
        | DESCRIPTION EQUALS STRING
    """
    print("bar_attribute")
    global voice_list
    global currentMeasure 

    if len(p) == 2: 
            currentMeasure.voices = voice_list
    elif len(p) == 3:
        if p[1] == "clef":
            currentMeasure.clef = clef.clefFromString(p[2][1:-1])
        elif p[1] == "dynamics":
            currentMeasure.dynamics = dynamics.Dynamic(p[2][1:-1])
        elif p[1] == "articulation":
            if(p[2][1:-1] == "staccato"):
                currentMeasure.articulation = articulations.Staccato()
            elif(p[2][1:-1] == "pizzicato"):
                currentMeasure.articulation = articulations.Pizzicato()
            elif(p[2][1:-1] == "legato"):
                currentMeasure.articulation = articulations.DetachedLegato()
            elif(p[2][1:-1] == "accent"):
                currentMeasure.articulation = articulations.Accent()
        elif p[1] == 'key':
            currentMeasure.key = key.Key(parseKey(p[2][1:-1]))  
    elif len(p) == 4:
        if p[1] == "tempo":
            currentMeasure.tempo = tempo.MetronomeMark(p[3][1:-1])
        elif p[1] == "lyrics":
            currentMeasure.lyrics = p[3][1:-1]
        elif p[1] == "description":
            currentMeasure.duration = p[3][1:-1]
        elif p[1] == "sound_duration":
            currentMeasure.sound_duration = p[3][1:-1]
        else:
            currentMeasure.times_signature =  meter.TimeSignature(p[2][1:-1])
    pass

def p_expression_list(p):
    """
    expression_list : expression
        | expression SEPARATOR expression_list
    """
    print("expression_list")

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
        number = int(p[1]) - 1
        if number < len(sounds_list):
            indices.add(number)
        else:
            raise Exception("Index out of range")

    elif len(p) == 4: #index sign number
        number = int(p[3]) - 1

        if p[2] == "=":
            if number < len(sounds_list):
                indices.add(number)
            else:
                raise Exception("Index out of range")
        elif p[2] == ">=":
            numbers = set(range(len(sounds_list))).intersection(set(range(number,len(sounds_list))))
            if len(numbers) == 0:
                msg = "Wrong expression: i>={}".format(number+1)
                raise Exception(msg)
            else:
                indices = indices.union(numbers)

        elif p[2] == "<=":
            numbers = set(range(len(sounds_list))).intersection(set(range(0,number+1)))
            if len(numbers) == 0:
                msg = "Wrong expression: i<={}".format(number+1)
                raise Exception(msg)
            else:
                indices = indices.union(numbers)

        elif p[2] == ">":
            numbers = set(range(len(sounds_list))).intersection(set(range(number+1,len(sounds_list))))
            if len(numbers) == 0:
                msg = "Wrong expression: i>{}".format(number+1)
                raise Exception(msg)
            else:
                indices = indices.union(numbers)
        elif p[2] == "<":
            numbers = set(range(len(sounds_list))).intersection(set(range(0,number)))
            if len(numbers) == 0:
                msg = "Wrong expression: i<{}".format(number+1)
                raise Exception(msg)
            else:
                indices = indices.union(numbers)

def repeat_sounds(x):
    print("repeat_sounds")
    global sounds_list
    result = []
    for i in range(0,int(x)):
        result += copy.deepcopy(sounds_list)
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
    global sound_tempo
    global sound_description
    global indices
    
    for i in indices:
        if sound_clef != None: 
            sounds_list[i].clef = copy.deepcopy(sound_clef)
        if sound_key != None: 
            sounds_list[i].key = copy.deepcopy(sound_key)
        if sound_dynamics != None:
            sounds_list[i].dynamics = copy.deepcopy(sound_dynamics)
        if sound_articulation != None: sounds_list[i].articulation = copy.deepcopy(sound_articulation)
        if sound_lyrics != None: sounds_list[i].lyrics = copy.deepcopy(sound_lyrics)
        if sound_description != None: sounds_list[i].description = copy.deepcopy(sound_description)
        if sound_tempo != None: sounds_list[i].tempo = copy.deepcopy(sound_tempo)
        if sound_duration != None: sounds_list[i].sound_duration = copy.deepcopy(sound_duration) 

    sound_clef = None
    sound_articulation = None
    sound_lyrics = None
    sound_dynamics = None
    sound_duration = None
    sound_key = None
    sound_description = None
    sound_tempo = None

def p_repeat(p):
    """
    repeat : REPEAT ITERATION_NUMBER
    """
    print("repeat")
    global sounds_list
    repeat_sounds(p[2][1:-1])
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
        | LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET repeat
        | LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET apply
        | LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET repeat AND apply
        | LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET apply AND repeat
    """
    print("sounds list")
    global sounds_list
    global voice_list
    voice = Voice()
    voice.sounds = copy.deepcopy(sounds_list)
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
    currentSound.note = note.Note(p[1])
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
    | sound_attribute additionals_for_sound
    """
    print("additionals_for_sound")

def p_sound_attribute(p):
    """
    sound_attribute : SEPARATOR SOUND_DURATION_VALUE
        | SEPARATOR CLEF CLEF_VALUE
        | SEPARATOR ARTICULATION ARTICULATION_VALUE
        | SEPARATOR DYNAMICS DYNAMICS_VALUE
        | SEPARATOR LYRICS EQUALS STRING
        | SEPARATOR DESCRIPTION EQUALS STRING
        | SEPARATOR KEY KEY_VALUE
        | SEPARATOR TEMPO EQUALS STRING
    """
    print("sound_attribute")

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
            if sound_description is None:
                sound_description = p[4][1:-1]
        elif(p[2] =="lyrics"):  
            if sound_lyrics is None:
                sound_lyrics = p[4][1:-1]
        elif(p[2] =="dynamics"):  
            if sound_dynamics is None:
                sound_dynamics = dynamics.Dynamic(p[3][1:-1])
        elif(p[2] =="articulation"):
            if sound_articulation is None:
                if(p[3][1:-1] == "staccato"):
                    sound_articulation = articulations.Staccato()
                elif(p[3][1:-1] == "pizzicato"):
                    sound_articulation = articulations.Pizzicato()
                elif(p[3][1:-1] == "legato"):
                    sound_articulation = articulations.DetachedLegato()
                elif(p[3][1:-1] == "accent"):
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
    print("inherit_attributes")
    for piece in piece_list:
        for group in piece.groups:
            if group.sound_duration is None: group.sound_duration = copy.deepcopy(piece.sound_duration)
            if group.clef is None: group.clef = copy.deepcopy(piece.clef)
            if group.articulation is None: group.articulation = copy.deepcopy(piece.articulation)
            if group.dynamics is None: group.dynamics = copy.deepcopy(piece.dynamics)
            if group.lyrics is None: group.lyrics = copy.deepcopy(piece.lyrics)
            if group.description is None: group.description = copy.deepcopy(piece.description)
            if group.key is None: group.key = copy.deepcopy(piece.key)
            if group.tempo is None: group.tempo = copy.deepcopy(piece.tempo)
            if group.time_signature is None: group.time_signature =copy.deepcopy(piece.time_signature)

            for staff in group.staffs:
                if staff.sound_duration is None: staff.sound_duration = copy.deepcopy(group.sound_duration)
                if staff.clef is None: staff.clef = copy.deepcopy(group.clef)
                if staff.articulation is None: staff.articulation = copy.deepcopy(group.articulation)
                if staff.dynamics is None: staff.dynamics = copy.deepcopy(group.dynamics)
                if staff.lyrics is None: staff.lyrics = copy.deepcopy(group.lyrics)
                if staff.description is None: staff.description = copy.deepcopy(group.description)
                if staff.key is None: staff.key = copy.deepcopy(group.key)
                if staff.tempo is None: staff.tempo = copy.deepcopy(group.tempo)
                if staff.time_signature is None: staff.time_signature = copy.deepcopy(piece.time_signature)

                for bar in staff.bars:
                    if bar.sound_duration is None: bar.sound_duration = copy.deepcopy(staff.sound_duration)
                    if bar.clef is None: bar.clef = copy.deepcopy(staff.clef)
                    if bar.articulation is None: bar.articulation = copy.deepcopy(staff.articulation)
                    if bar.dynamics is None: bar.dynamics = copy.deepcopy(staff.dynamics)
                    if bar.lyrics is None: bar.lyrics = copy.deepcopy(staff.lyrics)
                    if bar.description is None: bar.description = copy.deepcopy(staff.description)
                    if bar.key is None: bar.key = copy.deepcopy(staff.key)
                    if bar.tempo is None: bar.tempo = copy.deepcopy(staff.tempo)
                    if bar.time_signature is None: bar.time_signature = copy.deepcopy(piece.time_signature)

                    for voice in bar.voices:
                        for sound in voice.sounds:
                            if sound.sound_duration is None: sound.sound_duration = copy.deepcopy(bar.sound_duration)
                            if sound.clef is None: sound.clef = copy.deepcopy(bar.clef)
                            if sound.articulation is None: sound.articulation = copy.deepcopy(bar.articulation)
                            if sound.dynamics is None: sound.dynamics = copy.deepcopy(bar.dynamics)
                            if sound.lyrics is None: sound.lyrics = copy.deepcopy(bar.lyrics)
                            if sound.description is None: sound.description = copy.deepcopy(bar.description)
                            if sound.key is None: sound.key = copy.deepcopy(bar.key)
                            if sound.tempo is None: sound.tempo = copy.deepcopy(bar.tempo)
                            #if sound.time_signature is None: sound.time_signature = piece.time_signature
    pass

def build_piece():
    inherit_attributes()
    print("build_piece")
    i = 0
    for piece in piece_list:
        for group in piece.groups:
            for staff in group.staffs:
                for bar in staff.bars:
                    for voice in bar.voices:
                        for sound in voice.sounds:
                            if sound.lyrics != None: sound.note.addLyric(sound.lyrics)
                            if sound.description != None: sound.note.addLyric(sound.description)
                            if sound.articulation != None: sound.note.articulations.append(sound.articulation)
                            if sound.sound_duration != None: sound.note.duration = sound.sound_duration
                            #if sound.clef != None: sound.clef = sound.clef
                            voice.voice.append(sound.note)
                        
                        bar.measure.append(voice.voice)
                    staff.staff.append(bar.measure)
                piece.score.insert(0, staff.staff)
            group.staff_group = layout.StaffGroup([x.staff for x in group.staffs])
            piece.score.insert(0, group.staff_group)
    piece.score.show()
    """
                    #if bar.time_signature != None: bar.measure.append(bar.time_signature)
                    
                        
                        
                            
                """


    """
     if sound_clef != None: 
         sounds_list[i].clef = sound_clef
        if sound_key != None: 
            sounds_list[i].key = sound_key
        if sound_dynamics != None:
            sounds_list[i].dynamics = sound_dynamics 
        if sound_tempo != None: sounds_list[i].tempo = sound_tempo
                            """
    pass


def showNotes():
    build_piece()
    print("showNotes")
    print(piece_list)
    print(piece_list[0].groups[0])
    print(piece_list[0].groups[0].staffs)

    print(piece_list[0].groups[0].staffs[0].bars[0])
    print(piece_list[0].groups[0].staffs[0].bars[0].voices)

    print(piece_list[0].groups[0].staffs[0].bars[1]) 
    print(piece_list[0].groups[0].staffs[0].bars[1].voices)

    print(piece_list[0].groups[0].staffs[0].bars[0].voices[0].sounds)
    print(piece_list[0].groups[0].staffs[0].bars[0].voices[0].sounds[0].note)
    print(piece_list[0].groups[0].staffs[0].bars[0].measure.voices)
    #piece_list[0].groups[0].staffs[1].bars[0].measure.show()
    #piece_list[0].score.show()