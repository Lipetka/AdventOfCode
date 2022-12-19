import math
################ PART 1 ################

input_file = '2022\Problem4\input.txt'      # path to input file
data = open(input_file,'r')                 # open input file

pairs = 0       # placeholder for pairs
notpairs = 0    # placeholder for no pairs to check correctness of code
overlaps = 0    # placeholder for overlap counter
nooverlaps = 0  # placeholder for no overlap counter

for line in data:
    split       = line.split(',')   # split input data by ,
    firstID     = split[0]          # save first pair
    secondID    = split[1]          # save second pair

    ID11 = int(firstID.split('-')[0])   # get first number of first ID
    ID12 = int(firstID.split('-')[1])   # get second number of first ID
    ID21 = int(secondID.split('-')[0])  # get first number of second ID
    ID22 = int(secondID.split('-')[1])  # get second number of second ID

    # check for overlaps from both IDs, if there is overlap increase pair count, if no increase nopair count
    if (ID11 <= ID21 ) and (ID12 >= ID22):
        pairs = pairs + 1       
    elif (ID21 <= ID11 ) and (ID22 >= ID12):
        pairs = pairs + 1
    else:
        notpairs += 1

    # check for IDs that dont overlap at all
    if (ID22<ID11)or(ID21>ID12):
        nooverlaps += 1



# print answer, pairs+nopairs should be 1000

print('Number of incl. pairs (Part 1 answer):' + str(pairs))
print(notpairs)
print(pairs+notpairs)

print('Number of overlaps IDs (Part 2 answer):' + str(pairs + notpairs - nooverlaps))
print(nooverlaps)

# --xxx--
# ----xx--