from scanner import *
from parser import * 

parser = yacc.yacc(start='create_bar')
text = data #file.read()
parser.parse(text, lexer=lexer)

#print(tokensList)

showNotes()
#currentMeasure.show()
#print(voice_list)