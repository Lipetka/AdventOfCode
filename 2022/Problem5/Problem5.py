import math
################ PART 1 ################

global boxes

def main():
    input_file = '2022\Problem5\input.txt'      # path to input file
    data = open(input_file,'r')                 # open input file

    boxes = [
        'ZN',
        'MCD',
        'P'
    ]

    for line in data:
        line_split  = line.split(' ')
        number      = int(line_split[1])
        frm         = int(line_split[3])
        to          = int(line_split[5])
        print(number)
        print(frm)
        print(to)

        
        new_Boxes = moveBoxes(boxes,number,frm,to)
        boxes = new_Boxes
        print(boxes)

    print(boxes)

def moveBoxes(boxes,number,frm,to):
    movedString = boxes[frm-1][-number:]
    print('moved string: ' + movedString)

    newBoxes = boxes[to-1].join(movedString[::-1])


    return newBoxes
main()