f = open("example2.txt", "r")

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

#sound
if (str[1] in ['#','b','\\'] or str[1] in ['', '1', '2', '3']):
    str = str + f.read(1)
    if (str[2] in ['', '1', '2', '3']):
        print("dzwiek")

