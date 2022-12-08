def pointsForChosenPlay(line):
    if(line[2] == 'X'):
        return 1
    elif(line[2] == 'Y'):
        return 2
    elif(line[2] == 'Z'):
        return 3
    
def pointsForWinning(line):
    if(line[0] == 'A'):

        if(line[2] == 'X'):
            return 3
        elif(line[2] == 'Y'):
            return 6
        elif(line[2] == 'Z'):
            return 0

    elif(line[0] == 'B'):

        if(line[2] == 'X'):
            return 0
        elif(line[2] == 'Y'):
            return 3
        elif(line[2] == 'Z'):
            return 6

    elif(line[0] == 'C'):

        if(line[2] == 'X'):
            return 6
        elif(line[2] == 'Y'):
            return 0
        elif(line[2] == 'Z'):
            return 3