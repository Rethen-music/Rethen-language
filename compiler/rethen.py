import sys
import os
from scanner import *
from parser import * 

filePath = None

def checkArguments():
        global filePath
        global data
        global lexer
        if(len(sys.argv)) != 5:
            msg = """
            Wrong arguments.\n
            While script calling you should give parameters listed below:\n
            -i [path to input file]
            -o [path to output file (*.mid, *.pdf, MUSE_SCORE)]\n
            """
            raise Exception(msg)
        else:
            if sys.argv[1] == "-i":
                filePath = sys.argv[2]
                if filePath[-3:] != "txt": raise Exception("Input file shoud be *.txt")
                try:
                    f = open(filePath, "r")
                    data = f.read()
                    lexer.input(data)
                    parser = yacc.yacc(start='start')
                    parser.parse(data, lexer=lexer)
                except:
                    raise Exception("Wrong input file path")
            else:
                msg = """
                Wrong arguments.\n
                While script calling you should give parameters listed below:\n
                -i [path to input file]
                -o [path to output file (*.mid, *.pdf, MUSE_SCORE)]\n
                """
                raise Exception(msg)
            
            if sys.argv[3] == "-o":
                filePath = sys.argv[4]
                if filePath[-3:] != "pdf" and filePath[-3:] != "mid" and filePath != "MUSE_SCORE": raise Exception("Input file shoud be *.pdf or *.mid or MUSE_SCORE")
                try:
                    if(filePath == "MUSE_SCORE"):
                        showNotes("")
                    else:
                        showNotes(filePath)
                except:
                    raise Exception("Wrong input file path")
            else:
                msg = """
                Wrong arguments.\n
                While script calling you should give parameters listed below:\n
                -i [path to input file]
                -o [path to output file (*.mid, *.pdf, MUSE_SCORE)]\n
                """
                raise Exception(msg)



checkArguments()
