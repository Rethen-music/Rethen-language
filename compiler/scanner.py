
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



# A regular expression rule with some action code


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
 # A string containing ignored characters (spaces and tabs)
#t_ignore  = r'[ ]{1}'

 # Error handling rule
def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    if(t.value[0] != ' '): print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
 
# Build the lexer
lexer = lex.lex()

data = '''
create piece:
    author = "Frideric Chopin"
    title = "Polonaise"
    time_signature(1/4)
    key(c-flat)
    create group:
        create staff:
            clef(alto)
            time_signature(1/2)
            create bar:
                time_signature(3/8)
                [{C,'1/2'},{A,'1/4',dynamics(cresc),description="vibrato",lyrics="slowo"}]
                [{D,'1/2'},{G,'1/4'}]
            create bar:
                [{D,'1',key(g-sharp)},{B,'1',key(B-sharp)}]
                [{E,'1'},{F,'1',key(B-sharp)}]
        create staff:
            clef(bass)
            create bar:
                [{F,'1/16'},{G},{R}] repeat(8) & apply [,clef(treble),key(C-sharp),dynamics(ppp),tempo="adagio",articulation(staccato),description="vibrato",lyrics="aua"] for [16]
 create piece:
 '''
 # Give the lexer some input
lexer.input(data)
 
tokensList = []
 # Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    tokensList.append(tok)

