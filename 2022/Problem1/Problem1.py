# problem 1

# Find which elf is carrying the most calories,
# Elves are divided by empty line and total calories
# carried by one elf is the sum of all numbers in one section

################ PART 1 ################

# iterate through input file and save the sum of all calories
# in one list, than find index of max in the list and that is the
# answer to part one

input_file = '2022\Problem1\input.txt'      # path to input file
data = open(input_file,'r')                 # open input file
elfs = []                                   # initiate list of elf calories
elf_index = 0
sum = 0

# read line by line

for line in data:
    # if we get new line, append number of calories to elfs list and add i to calculate sum for next elf
    if(line == '\n'):

        elfs.append(sum)    # append list for "previous elf"
        elf_index += 1              # increse elf counter
        sum = 0             # reset sum
        continue            # skip loop for '\n' line

    sum = sum + int(line)   # sum inputs


print("Elf carrying the most calories is carrying " + str(max(elfs)) + " calories") # print the answer

## PART 2 ##

# find the sum of calories carried by top three elves

# using the list from part 1
# to find top three elves we must iterate and in each iteration
# find the max and remove it from list and sum their calories
top_three_calories_sum = 0

for i in range(3):
    top_three_calories_sum = top_three_calories_sum + max(elfs)     # add calories
    index_of_top_elf = elfs.index(max(elfs))                        # get the index of the top elf
    elfs.pop(index_of_top_elf)                                      # remove the top elf

print("The sum of calories for top three elves is: " + str(top_three_calories_sum)) # print answer
