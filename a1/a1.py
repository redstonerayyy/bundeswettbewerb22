import re

def getalicetext():
    with open("Alice_im_Wunderland.txt") as file:
        temp = file.read().split("\n")
        lines = []
        for i in temp:
        # if not (i in ["\n", "", " "]): # remove certain occurences, messes up line count
            lines.append(i.replace("\n", ""))

    return lines, " ".join(lines) # check per line and check full text

def getdistortion(filename):
    with open(filename) as file:
        diss = file.readline().split(" ")
        return diss

def makeregex(distortion):
    diss = distortion[:] # local variable so argument doesn't get messed up
    # regex for a word
    matchword = "[a-zA-ZöäüßÖÄÜ]+"
    # replace _ with regex matching any word
    for i in range(len(diss)):
        if diss[i] == "_":
            diss[i] = matchword
    # generate pattern
    regexstring = " ".join(diss)
    regexstring = "(" + regexstring + ")"
    print(regexstring)
    regex = re.compile(regexstring, re.IGNORECASE) # ignore case
    return regex


for i in range(6):
    # main code
    print(f"------stoerung{i}.txt------")
    alicelines, fulltext = getalicetext()
    distortion = getdistortion(f"stoerung{i}.txt")
    regex = makeregex(distortion)

    # for output
    print("Stoerung:", distortion)

    # line = "»Das kommt mir gar nicht richtig vor,"
    linenumber = 1
    for line in alicelines:
        res = re.findall(regex, line)
        if res:
            print("Linenumber:", linenumber, "Appearances:", len(res),"Line:", line)
        
        linenumber += 1
    
    #fulltext
    print("------Fulltext matching------")
    res = re.findall(regex, fulltext)
    if res:
        print("Appearances:", len(res))
        print("Text", res)
        