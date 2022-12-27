import string
################ PART 1/2 ################

def main():
    input_file = 'Problem5\input.txt'       # path to input file
    data = open(input_file,'r')             # open input file

    # initial condition for boxes
    boxes = [
        'PFMQWGRT',
        'HFR',
        'PZRVGHSD',
        'QHPBFWG',
        'PSMJH',
        'MZTHSRPL',
        'PTHNML',
        'FDQR',
        'DSCNLPH'
    ]

    for line in data:
        # read each line, extract commands
        line_split  = line.split(' ')
        number      = int(line_split[1])
        frm         = int(line_split[3])
        to          = int(line_split[5])

        # get boxes which will be moved
        movedString = boxes[frm-1][-number:]
        # reverse order (for part 1 uncomment, for part 2 comment out)
        #movedString = movedString[::-1]

        # delete moved boxes from last position
        boxes[frm-1] = boxes[frm-1][:-number]

        # add moved boxes to new column
        boxes[to-1] = boxes[to-1]+movedString

    
    finalMessage = ""   # placeholder for final answer

    for i in range(len(boxes)):
        finalMessage = finalMessage + boxes[i][-1]  # append last numbers
    
    print(finalMessage)

main()
