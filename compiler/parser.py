from re import S
from matplotlib.colors import NoNorm
import ply.yacc as yacc
from music21 import *
#        | LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET REPEAT INTERATION_NUMBER AND APPLY attributes loop

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


currentMeasure = stream.Measure()
currentMeasure.insert(meter.TimeSignature("4/4"))
currentSound = None


sounds_list = []
def p_sounds_list(p):
    """
    sounds_list : LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET
        | LEFT_SQUARE_BRACKET sounds RIGHT_SQUARE_BRACKET REPEAT ITERATION_NUMBER
    """
    print("sounds list")
   # sounds_list.clear()
    pass


def p_sounds(p):
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
    currentSound = note.Note(p[1])
    if sound_lyrics != None: currentSound.addLyric(sound_lyrics)
    if sound_articulation != None: currentSound.articulations.append(sound_articulation)
    if sound_clef != None: currentMeasure.append(sound_clef)
    if sound_duration != None:currentSound.duration = sound_duration
    if sound_key != None: currentMeasure.append(sound_key)
    currentMeasure.append(currentSound)
    if sound_dynamics != None:currentMeasure.insert(currentSound.offset,dynamics.Dynamic(p[4][1:-1]))
    if sound_description != None:currentSound.addLyric(sound_description)
    sounds_list.append(currentSound)

    currentSound = None
    sound_clef = None
    sound_articulation = None
    sound_lyrics = None
    sound_dynamics = None
    sound_duration = None
    sound_key = None
    sound_description = None
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

    global currentMeasure
    global currentSound
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