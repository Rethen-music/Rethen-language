f = open("example2.txt", "r")

tokens = []   # list of all tokens


str = ""
str = str + f.read(1)
str = str + f.read(1)

#clef
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


#sound   na start mamy 2 znaki

if(str[0] in ['C','D','E','F','G','A','H','c','d','e','f','g','a','h'] ):
    if(str[1] == ' '): tokens.append(("sound",str))
    if (str[1] in ['1', '2', '3']):
        tokens.append(("sound",str))

    if(str[1] in ['#','b','\\'] ):
        str = str + f.read(1)
        if (str[2] in ['1', '2', '3']):
            tokens.append(("sound", str))
    if(str[1] in ['#','b','\\']): tokens.append(("sound",str))





print(tokens)