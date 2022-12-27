import string
################ PART 1 ################

def main():
    input_file = 'Problem6\input.txt'           # path to input file
    data = open(input_file,'r').read()          # open input file
    dataLength = 14                             # change to "14" for part 2 and "4" for part 1

    for i in range(len(data)):
        
        checkedSubString = data[i:i+dataLength] # extract substring to be checked
        duplicateFlag = 0                       # duplicate character flag

        for char in checkedSubString:
            if checkedSubString.count(char) > 1:
                # if there are more duplicate characters raise flag
                duplicateFlag = 1
        
        # if there are no duplications return index i and break loop
        if duplicateFlag == 0:
            print(i+dataLength)
            break

main()
