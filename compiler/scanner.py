
import ply.lex as lex
 
 # List of token names.   This is always required
tokens = (
    'SOUND_NAME',
    'REST',
    'SEPARATOR',
    'SOUND_DURATION',
    'SOUND_DURATION_VALUE',
    'CLEF',
    'CLEF_VALUE',
    'KEY',
    'KEY_VALUE',
    'DYNAMICS',
    'DYNAMICS_VALUE',
    'DESCRIPTION',
    'LYRICS',
    'ARTICULATION',
    'ARTICULATION_VALUE',
    'AUTHOR',
    'TITLE',
    'TIME_SIGNATURE',
    'TIME_SIGNATURE_VALUE',
    'TAB',
    'TEMPO',
    'CREATE',
    'PIECE',
    'GROUP',
    'STAFF',
    'BAR',
    'COLON_SIGN',
    'LEFT_SQUARE_BRACKET',
    'RIGHT_SQUARE_BRACKET',
    'LEFT_CURLY_BRACKET',
    'RIGHT_CURLY_BRACKET',
    'REPEAT',
    'APPLY',
    'FOR',
    'AND',
    'INDEX',
    'GREATER',
    'GREATER_EQUALS',
    'LOWER',
    'LOWER_EQUALS',
    'EQUALS',
    'NUMBER',
    'STRING',
    'ITERATION_NUMBER'
 )
 
# Regular expression rules

t_SOUND_NAME = r'[CDEFGAB](\#|b|bb|\#\#)?[1-8]?'
t_REST = r'R'
t_SEPARATOR = r','
t_SOUND_DURATION= r'sound_duration'
t_SOUND_DURATION_VALUE = r'\'([1-9][0-9]?[\/][1-9][0-9]?|1)\''
t_CLEF = r'clef'
t_CLEF_VALUE = r'\((treble|bass|alto)\)'
t_KEY = r'key'
t_KEY_VALUE = r'\((c|C|d|D|e|E|f|F|g|G|a|A|b|B)(-sharp|-flat)?\)'
t_DYNAMICS = r'dynamics'
t_DYNAMICS_VALUE = r'\((ppp|pp|p|mp|mf|f|ff|fff|sf|cresc|decresc|dim)\)'
t_DESCRIPTION = r'description'
t_LYRICS = r'lyrics'
t_ARTICULATION = r'articulation'
t_ARTICULATION_VALUE = r'\((staccato|legato|pizzicato|accent)\)'
t_AUTHOR = r'author'
t_TITLE = r'title'
t_TIME_SIGNATURE = r'time_signature'
t_TIME_SIGNATURE_VALUE = r'\([1-9][0-9]?[\/][1-9][0-9]?\)'
t_TAB = r'[ ]{4}|[\t]'
t_TEMPO = r'tempo'
t_CREATE = r'create'
t_PIECE = r'piece'
t_GROUP = r'group'
t_STAFF = r'staff'
t_BAR = r'bar'
t_COLON_SIGN = r':'
t_LEFT_SQUARE_BRACKET = r'\['
t_RIGHT_SQUARE_BRACKET = r']'
t_LEFT_CURLY_BRACKET = r'\{'
t_RIGHT_CURLY_BRACKET = r'\}'
t_REPEAT = r'repeat'
t_APPLY = r'apply'
t_FOR = r'for'
t_AND = r'&'
t_INDEX = r'i'
t_GREATER = r'>'
t_GREATER_EQUALS = r'>='
t_LOWER = r'<'
t_LOWER_EQUALS = r'<='
t_EQUALS = r'='
t_NUMBER = r'[1-9][0-9]*'
t_ITERATION_NUMBER = r'\([1-9][0-9]*\)'
t_STRING = r'"[A-Za-z][A-Z a-z]*"'




def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    if(t.value[0] != ' '): raise Exception("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
 

lexer = lex.lex()

data = None