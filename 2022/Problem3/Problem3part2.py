################ PART 2 ################

input_file = '2022\Problem3\input.txt'      # path to input file
data = open(input_file,'r')                 # open input file

answers = []

while(1):
    group = []

    group.append(data.readline().strip('\n'))
    group.append(data.readline().strip('\n'))
    group.append(data.readline().strip('\n'))

    # check if the group is empty
    if group[0] == '':
        break
    
    new_word_flag = 0

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
                    answers.append(i)
                    new_word_flag = 1

sum = 0

for i in answers:
    if i.islower():
        sum = sum + ord(i) - 96
    else:
        sum = sum + ord(i) - 38
print(answers)
print(sum)

