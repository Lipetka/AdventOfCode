# NOT WORKING #

import string

def main():
    input_file = 'Problem7\input.txt'    # path to input file
    data = open(input_file,'r')          # open input file

    treesList = []
    i = 0

    for line in data:
        treesList.append(line.strip('\n'))  # append each line to trees list
        i += 1                              # iterate through list

    sumLeft     = checkFromLeft(treesList)
    sumRight    = checkFromRight(treesList)
    sumTop      = checkFromTop(treesList) 
    sumBottom   = checkFromBottom(treesList)
    totalSum    = sumLeft+sumRight+sumBottom+sumTop
    print(totalSum)
        
def checkFromLeft(treesList):
    sum = len(treesList)
    for i in range(len(treesList)):
        for j in range(len(treesList[i])):
            if treesList[i][j] < treesList[i][j+1]:
                sum += 1
            else:
                break
    return sum

def checkFromRight(treesList):
    sum = len(treesList)
    for i in range(len(treesList)):
        for j in range(len(treesList[i])):
            if treesList[i][-j] < treesList[i][-j+1]:
                sum += 1
            else:
                break
    return sum

def checkFromTop(treesList):
    sum = len(treesList)
    for j in range(len(treesList)):
        for i in range(len(treesList[j])):
            if treesList[i][j] < treesList[i+1][j]:
                sum += 1
            else:
                break
    return sum

def checkFromBottom(treesList):
    sum = len(treesList)
    for j in range(len(treesList)):
        for i in range(len(treesList[j])):
            if treesList[-i][j] < treesList[-i+1][j]:
                sum += 1
            else:
                break
    return sum

main()
