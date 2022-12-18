################ PART 2 ################

input_file = '2022\Problem3\input.txt'      # path to input file
data = open(input_file,'r')                 # open input file

answers = []        # placeholder for answers

while(1):
    group = []      # placeholder for group reading

    # read three lines and substract the '\n' line end character
    group.append(data.readline().strip('\n'))
    group.append(data.readline().strip('\n'))
    group.append(data.readline().strip('\n'))

    # check if the group is empty to skip the last group
    if group[0] == '':
        break
    
    new_word_flag = 0

    # iterate through all three items in list and check similarities
    for i in group[0]:
        if new_word_flag:
            break
        for j in group[1]:
            if new_word_flag:
                break
            for k in group[2]:
                if new_word_flag:
                    break
                if i==j==k:
                    answers.append(i)       # append to answer list
                    new_word_flag = 1       # go to new word

## sum of score
sum = 0

for i in answers:
    if i.islower():
        sum = sum + ord(i) - 96     # convert char to ASCII and substract constant to fit scoreboard
    else:
        sum = sum + ord(i) - 38     # convert char to ASCII and substract constant to fit scoreboard
        
print(answers)
print(sum)

