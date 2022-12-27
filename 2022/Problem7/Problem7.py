import string

def main():
    input_file = 'Problem7\input.txt'           # path to input file
    data = open(input_file,'r')          # open input file

    treesList = []
    i = 0

    for line in data:
        treesList.append(line.strip('\n'))
        i += 1

        

main()
