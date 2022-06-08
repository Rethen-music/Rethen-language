from scanner import *
from parser import * 

parser = yacc.yacc()
text = data #file.read()
parser.parse(text, lexer=lexer)

#print(tokensList)

currentMeasure.show()