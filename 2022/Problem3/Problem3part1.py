import math
################ PART 1 ################

input_file = '2022\Problem3\input.txt'      # path to input file
data = open(input_file,'r')                 # open input file

results = []    # preallocate results list

for line in data:
    length_of_line = len(line)                          # get length of line
    first_half_length = math.floor(length_of_line/2)    # get lenfth of half
    first_half = line[0:first_half_length]              # get first half of line
    second_half = line[first_half_length:-1]            # get second half of line

    new_word_flag = 0           # flag to go to new word

    # iterate through all letters and check if they are the same
    for i in first_half:
        if new_word_flag:
            break
        for j in second_half:
            if new_word_flag:
                break
            if i==j:
                # if they are the same, append the 'same' char to results list
                results.append(i)
                new_word_flag = 1   # go to new word


## calculating sum of points

sum = 0 # sum placeholder

for i in results:
    if i.islower():
        sum = sum + ord(i) - 96     # convert to ascii and substract constant to fit scoreboard
    else:
        sum = sum + ord(i) - 38      # convert to ascii and substract constant to fit scoreboard
        
print(results)
print(sum)

