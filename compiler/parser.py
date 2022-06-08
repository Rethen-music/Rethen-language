from re import S
import re
from telnetlib import XDISPLOC

from structures.sound import Sound
from structures.piece import Piece
from structures.group import Group
from structures.voice import Voice
from structures.bar import Bar


from matplotlib.colors import NoNorm
import ply.yacc as yacc
from music21 import *

#piece
result_score = Piece()

#group
#currentGroup = None



#sound
sound_clef = None
sound_articulation = None
sound_lyrics = None
sound_dynamics = None
sound_duration = None
sound_key = None
sound_description = None

#measure
measure_time_signature = None

"""
currentVoice = None
currentMeasure = None
currentSound = None
currentStaff = None
"""

sounds_list = []
voice_list = []
measure_list =[] 
staff_list = []
group_list = []

def p_create_piece(p):
    """
    create_piece :  CREATE PIECE COLON_SIGN after_create_piece
    """

def p_after_create_piece(p):
    """
    after_create_piece : empty
    | TAB AUTHOR EQUALS STRING after_create_piece
    | TAB TITLE EQUALS STRING after_create_piece
    | TAB KEY KEY_VALUE after_create_piece
    | TAB CLEF CLEF_VALUE after_create_piece
    | TAB TEMPO EQUALS STRING after_create_piece
    | TAB TIME_SIGNATURE EQUALS TIME_SIGNATURE_VALUE after_create_piece
    | TAB CREATE GROUP COLON_SIGN after_create_group
    | TAB CREATE GROUP REPEAT ITERATION_NUMBER COLON_SIGN after_create_group
    """
    global result_score
    global group_list
    result_score.groups = group_list
    group_list.clear()
    
    if(len(p)>=3):
        if(p[2] == "author"):
            result_score.score.metadata.composer = p[4]
        elif(p[2]=='title'):
            result_score.score.metadata.title = p[4]
        elif(p[2]=='key'):
            result_score.key = key.Key(parseKey(p[3]))
        elif(p[2]=='tempo'):
            result_score.tempo = tempo.MetronomeMark(p[4][1:-1])
        elif(p[2]=='time_signature'):
            result_score.time_signature = meter.TimeSignature(p[4][1:-1])
        elif(p[2]=='clef'):
            result_score.clef = clef.Clef(p[4][1:-1])
        elif(p[2]=='create'):
            if(p[3]=='group'):
                if(p[4]==':'):
                    result_score.groups.append(currentGroup)
                    currentGroup = None
                if(p[4]=='repeat'):
                    for i in range(0,int(p[5][1:-1])):
                        result_score.groups.append(currentGroup)
                        currentGroup = None
        

def p_after_create_group(p):
    """
    after_create_group : empty
        | TAB TAB CREATE STAFF COLON_SIGN after_create_staff
        | TAB TAB CREATE STAFF REPEAT ITERATION_NUMBER COLON_SIGN after_create_staff
    """
    global staff_list
    global group_list
    currentGroup = Group()
    currentGroup.staffs = staff_list
    staff_list.clear()
    group_list.append(currentGroup)


    

    if(len(p)>=4):
        if(p[3]=='create'):
            if(p[4]=='staff'):
                if(p[5]==':'):
                    currentGroup.staff_group.append(currentVoice)
                    currentVoice = None



def p_after_create_staff(p):
    """
    after_create_staff : empty
        | TAB TAB TAB CLEF CLEF_VALUE after_create_staff
        | TAB TAB TAB TIME_SIGNATURE EQUALS TIME_SIGNATURE_VALUE after_create_staff
        | TAB TAB TAB KEY KEY_VALUE after_create_staff
        | TAB TAB TAB TEMPO EQUALS STRING after_create_staff
        | TAB TAB TAB CREATE BAR REPEAT ITERATION_NUMBER COLON_SIGN after_create_bar
        | TAB TAB TAB CREATE BAR COLON_SIGN after_create_bar
    """
    global staff_list
    global measure_list
    currentStaff = layout.Staff()
    currentStaff.bars = measure_list
    measure_list.clear()
    staff_list.append(currentStaff)

    ##### 
    if(len(p)>=5):
        if(p[4]=='clef'):
            sound_clef = p[5][1:-1]
            currentStaff.clef = clef.Clef(sound_clef)
        elif(p[4]=='time_signature'):
            measure_time_signature = p[5][1:-1]
            currentStaff.time_signature = meter.TimeSignature(measure_time_signature)
        elif(p[4]=='key'):
            sound_key = p[5][1:-1]
            currentStaff.key = key.Key(parseKey(sound_key))  
        elif(p[4]=='tempo'):
            sound_tempo = p[5][1:-1]
            currentStaff.tempo = tempo.MetronomeMark(sound_tempo)
        elif(p[4]=='create'):                             # ? ? ?                             
            if(p[5]=='staff'):                            # ? ? ?  
                if(p[6]==':'):                            # ? ? ?  
                    staff_list.append(currentStaff)       # ? ? ? 
                    currentStaff = None                   # ? ? ? 
                if(p[6]=='repeat'):                       # ? ? ?
                    for i in range(0,int(p[7][1:-1])):    # ? ? ? 
                        staff_list.append(currentStaff)   # ? ? ? 
                        currentStaff = None               # ? ? ? 




def p_after_create_bar(p):
    """
    after_create_bar :  empty
        | TAB TAB TAB TAB sounds_list after_create_bar
        | TAB TAB TAB TAB CLEF CLEF_VALUE after_create_bar
        | TAB TAB TAB TAB TEMPO EQUALS STRING after_create_bar
        | TAB TAB TAB TAB TIME_SIGNATURE EQUALS TIME_SIGNATURE_VALUE after_create_bar
        | TAB TAB TAB TAB KEY KEY_VALUE after_create_bar
    """
    print("after_create_bar")
    global voice_list
    global measure_list
    
    currentMeasure = Bar() 
    currentMeasure.measure.insert(meter.TimeSignature("4/4"))
    currentMeasure.voices = voice_list
    voice_list.clear()

    for voice in currentMeasure.voices:
        currentMeasure.append(voice)

    measure_list.append(currentMeasure)
    currentMeasure = None
    pass





def p_expression_list(p):
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
    """

def p_sounds_list(p):
    """
    sounds_list : LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET
        | LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET REPEAT ITERATION_NUMBER
        | LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET APPLY LEFT_SQUARE_BRACKET additionals_for_sound RIGHT_SQUARE_BRACKET FOR LEFT_SQUARE_BRACKET expression_list RIGHT_SQUARE_BRACKET
        | LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET REPEAT ITERATION_NUMBER AND APPLY LEFT_SQUARE_BRACKET additionals_for_sound RIGHT_SQUARE_BRACKET FOR LEFT_SQUARE_BRACKET expression_list RIGHT_SQUARE_BRACKET
    """
    print("sounds list")

    global sounds_list
    global voice_list
    global sound_clef
    global sound_articulation
    global sound_lyrics
    global sound_dynamics
    global sound_duration
    global sound_key
    global sound_description
    currentVoice = Voice()

    
    if(len(p)>=15):  #repeat and apply
        print("repeat and apply")
        for i in range(0,int(p[5][1:-1])):
            currentVoice.sounds += sounds_list
        sounds_list.clear()
        for sound in currentVoice.sounds:
            if sound_clef != None: 
                currentVoice.append(sound.clef)
                sound_clef = None
            if sound_key != None: 
                currentVoice.append(sound.key)
                sound_key = None
            currentVoice.append(sound.note)
            if sound_dynamics != None:
                currentVoice.insert(sound.offset,sound.dynamics)
                if sound_dynamics.value != "accent":
                    sound_dynamics = None
            if sound_articulation != None: sound.note.articulations.append(sound_articulation)            
            if sound_lyrics != None: currentSound.note.addLyric(sound_lyrics)
            if sound_duration != None:currentSound.note.duration = sound_duration

    elif(len(p)>=12): #apply
        print("apply")
        currentVoice.sounds = sounds_list
        sounds_list.clear()
        for sound in currentVoice.sounds:
            if sound_clef != None: 
                currentVoice.append(sound.clef)
                sound_clef = None
            if sound_key != None: 
                currentVoice.append(sound.key)
                sound_key = None
            currentVoice.append(sound.note)
            if sound_dynamics != None:
                currentVoice.insert(sound.offset,sound.dynamics)
                if sound_dynamics.value != "accent":
                    sound_dynamics = None
            if sound_articulation != None: sound.note.articulations.append(sound_articulation)            
            if sound_lyrics != None: currentSound.note.addLyric(sound_lyrics)
            if sound_duration != None:currentSound.note.duration = sound_duration 

    elif(len(p)>=6): #repeat
        for i in range(0,int(p[5][1:-1])):
            currentVoice.sounds += sounds_list
        sounds_list.clear()
        for sound in currentVoice.sounds:
            if sound.clef != None: currentVoice.append(sound.clef)
            if sound.key != None: currentVoice.append(sound.key)
            currentVoice.append(sound.note)
            if sound.dynamics != None:currentVoice.insert(sound.offset,sound.dynamics)
    else:
        currentVoice.sounds = sounds_list
        sounds_list.clear()
        for sound in currentVoice.sounds:
            if sound.clef != None: currentVoice.append(sound.clef)
            if sound.key != None: currentVoice.append(sound.key)
            currentVoice.append(sound.note)
            if sound.dynamics != None:currentVoice.insert(sound.offset,sound.dynamics)

    voice_list.append(currentVoice)
    currentVoice = None
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

    global sounds_list
    global currentSound
    
    
    currentSound.note = note.Note(p[1])
    if sound_lyrics != None: currentSound.note.addLyric(sound_lyrics)
    if sound_articulation != None: currentSound.note.articulations.append(sound_articulation)
    if sound_clef != None: currentSound.clef = sound_clef
    if sound_key != None: currentSound.key = sound_key
    if sound_dynamics != None:currentSound.dynamics = dynamics.Dynamic(p[4][1:-1])
    if sound_duration != None:currentSound.note.duration = sound_duration

  #  currentMeasure.append(currentSound)
    
    if sound_description != None:currentSound.note.addLyric(sound_description)
    sounds_list.append(currentSound)



    currentSound = None
    sound_articulation = None
    sound_lyrics = None
    sound_duration = None
    sound_description = None
    sound_clef = None
    sound_dynamics = None
    sound_key = None

    pass
   

def p_expression_for_rest(p):
    """
    expression_for_rest : REST additionals_for_rest
    """
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
        | SEPARATOR SOUND_DURATION additionals_for_sound
        | SEPARATOR CLEF CLEF_VALUE additionals_for_sound
        | SEPARATOR ARTICULATION ARTICULATION_VALUE additionals_for_sound
        | SEPARATOR DYNAMICS DYNAMICS_VALUE additionals_for_sound
        | SEPARATOR LYRICS EQUALS STRING additionals_for_sound
        | SEPARATOR DESCRIPTION EQUALS STRING additionals_for_sound
        | SEPARATOR KEY KEY_VALUE additionals_for_sound
    """


    global sound_clef
    global sound_articulation
    global sound_lyrics
    global sound_dynamics
    global sound_duration
    global sound_key
    global sound_description

    global currentVoice
    
    
    global sounds_list
    print("additionals for sound")

    if len(p) >= 3:
        if(p[2] == "key"): 
            sound_key = key.Key(parseKey(p[3]))
        elif(p[2] =="description"):
            if sound_duration is None:
                sound_duration = p[4][1:-1]
            #currentSound.addLyric(p[4][1:-1])
        elif(p[2] =="lyrics"):  
            if sound_lyrics is None:
                sound_lyrics = p[4][1:-1]
            #currentSound.addLyric(p[4][1:-1])
        elif(p[2] =="dynamics"):  
            if sound_dynamics is None:
                sound_dynamics = dynamics.Dynamic(p[4][1:-1])
            #currentMeasure.insert(currentSound.offset,dynamics.Dynamic(p[4][1:-1]))
        elif(p[2] =="articulation"):
            if sound_articulation is None:
                if(p[4][1:-1] == "staccato"):
                    sound_articulation = articulations.Staccato()
                    #currentSound.articulations.append(articulations.Staccato())
                elif(p[4][1:-1] == "pizzicato"):
                    sound_articulation = articulations.Pizzicato()
                    #currentSound.articulations.append(articulations.Pizzicato)
                elif(p[4][1:-1] == "legato"):
                    sound_articulation = articulations.DetachedLegato()
                    #currentSound.articulations.append(articulations.DetachedLegato())
                elif(p[4][1:-1] == "accent"):
                    sound_articulation = articulations.Accent()
                    #currentSound.articulations.append(articulations.Accent())
        elif(p[2] =="clef"):
            if sound_clef is None:
                if(p[3][1:-1] == "treble"):
                    sound_clef = clef.TrebleClef()
                    #currentMeasure.append(clef.TrebleClef())
                elif(p[3][1:-1]  == "bass"):
                    sound_clef = clef.BassClef()
                    #currentMeasure.append(clef.BassClef())
                elif(p[3][1:-1]  == "alto"):
                    sound_clef = clef.AltoClef()
                    #currentMeasure.append(clef.AltoClef())     
        else: #sound duration
            if sound_duration is None:
                d = duration.Duration()
                numbers =  [float(x) for x in p[2][1:-1].split('/')]
                if len(numbers) == 2:
                    d.quarterLength = numbers[0]/numbers[1] * 4
                elif len(numbers) == 1:
                    d.quarterLength = numbers[0] * 4
                sound_duration = d
                #currentSound.duration = d
        #currentMeasure.append(currentSound)
    pass

def p_additionals_for_rest(p):
    """
    additionals_for_rest : empty
    | SEPARATOR SOUND_DURATION additionals_for_sound
    | SEPARATOR CLEF CLEF_VALUE additionals_for_sound
    | SEPARATOR DESCRIPTION EQUALS STRING additionals_for_sound
    | SEPARATOR KEY KEY_VALUE additionals_for_sound
    """
    pass

def p_empty(p):
    'empty :'
    pass

def showNotes():
    result_score.score.show()