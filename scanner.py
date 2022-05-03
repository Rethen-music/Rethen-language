f = open("example2.txt", "r")

tokens = []   # list of all tokens
ktora_linia = 1

str =""
#str = str + f.read(1)
#str = str + f.read(1)

#clef"""
"""
if (str[1] == 'l'):
    i = 3
    flaga = False
    while (i):
        str = str + f.read(1)
        if (i == 3 and str[2] == 'e'): flaga = True
        if (i == 2 and str[3] == 'f'): flaga = True
        if (i == 1 and str[4] == ':'): flaga = True
        i = i - 1
        if flaga == False:
            break
        flaga = False
    if(i == 0):
        tokens.append(("clef",""))
        str =""
#       (("clef",""))
#       (("napis","bass"))

"""
#sound   na start mamy 2 znaki

flaga = True
aktualny_indeks = 1

def loadKey(str):
    char = f.read(1)
    temp =""
    # sharp
    if char == 's' :
        temp = 's' + f.read(4)
        if(temp != "sharp") :
            while char not in [' ', '', '\n']:
                str = str + char
                char = f.read(1)
            tokens.append(("error", str))
            return
        char = f.read(1)
        if(char != '-' ):
            while char not in [' ', '', '\n']:
                str = str + char
                char = f.read(1)
            tokens.append(("error", str))
            return
    #flat
    elif char == 'f':
        temp = 's' + f.read(3)
        if temp != "flat":
            while char not in [' ', '', '\n']:
                str = str + char
                char = f.read(1)
            tokens.append(("error", str))
            return
        if (char != '-'):
            while char not in [' ', '', '\n']:
                str = str + char
                char = f.read(1)
            tokens.append(("error", str))
            return
    #no sharp no flat
    if (char != '-'):
        while char not in [' ', '', '\n']:
            str = str + char
            char = f.read(1)
        tokens.append(("error", str))
        return
    str = str + char
    temp = f.read(5)
    str = str + temp
    if( temp in ["minor", "major"] ):
        i = False
        while char not in [' ', '', '\n']:
            i = True
            str = str + char
            char = f.read(1)
        if i:
            tokens.append(("error", str))
            str = ""
        else:
            tokens.append(("key",str))
            str = ""


char = f.read(1)
str = str + char
if str[0] in ['C', 'D', 'E', 'F', 'G', 'A', 'H', 'c', 'd', 'e', 'f', 'g', 'a', 'h']:
    #char = f.read(1)
    #if(char == '') : tokens.append(("sound", str))


    while char not in [' ', '' , '\n']:
        char = f.read(1)
        #str = str + char
    # TONACJA
        if(char == '-'):
            loadKey(str)
        elif char.isdigit() or char in ['#','b','\\']:
            i = False
            str = str + char
            char = f.read(1)
            while char not in [' ', '', '\n']:
                if not char.isdigit(): i = True
                str = str + char
                char = f.read(1)
            if i:
                tokens.append(("error", str))
                str = ""
            else:
                tokens.append(("sound",str))
                str = ""
        else:
            while char not in [' ', '', '\n']:
                str = str + char
                char = f.read(1)

    # C--minor, C-sharp/flat--minor/major
    # C#





    #if str[1] == ' ':
    #    char = f.read(1)
     #   if char.isdigit() :
     #       tokens.append(("sound", str))
     #       flaga = False
     #   else:
     #       tonacja()


        # tu moze byc tak samo tonacja    C Major


    if flaga == True:
        while 1:
            char = f.read(1)
            if(char == '' or char == ' '):
                    break
            else:
                str = str + char

        print(str)






        #if str[1] in ['1', '2', '3']:
        #    tokens.append(("sound", str))
        #if str[1] in ['#', 'b', '\\']:
        #    str = str + f.read(1)
        #    if (str[2] in ['1', '2', '3']):
        #        tokens.append(("sound", str))
        #if str[1] in ['#', 'b', '\\']:
        #    tokens.append(("sound", str))






print(tokens)