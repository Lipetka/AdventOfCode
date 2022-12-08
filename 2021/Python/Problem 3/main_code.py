
def main():
    f = open("problem3data.txt","r") # load data as txt file

    max_num_rate = [0]*(len(f.readline())-1) # create an array with length of one line to store the final value
    epsilon = [0] * len(max_num_rate)
    gamma = [0] * len(max_num_rate)
    # read all lines
    for line in f:
        pos = 0
        # rad all numbers
        for i in line:
            # if the char is \n skip it
            if i == '\n':
                break
            # sum all ones
            if int(i) == 1:
                max_num_rate[pos] = max_num_rate[pos] + 1
            # increase the position (up to 13)
            pos = pos + 1

    for i in range(12):
        if int(max_num_rate[i]) > 500:
            max_num_rate[i] = 1
            gamma[i] = 1
            epsilon[i] = 0
        else:
            max_num_rate[i] = 0
            gamma[i] = 0
            epsilon[i] = 1

    gamma = convert_array_to_dec(gamma)
    epsilon = convert_array_to_dec(epsilon)
    print(gamma*epsilon)
################################################
    f.seek(0)
    contents = f.readlines()
    truth_table = [1]*1000

    for i in range(12):
        for j in range(1000):

            if truth_table.count(1) == 1:
                continue
            if truth_table[j] == 0:
                continue
            if int(contents[j][i]) != max_num_rate[i]:
                truth_table[j] = 0

    most_common = contents[truth_table.index(1)]
    most_common = convert_string_to_dec(most_common)

#################################################

    f.seek(0)
    contents = f.readlines()
    truth_table = [1]*1000

    for i in range(12):
        for j in range(1000):

            if truth_table.count(1) == 1:
                continue
            if truth_table[j] == 0:
                continue
            if int(contents[j][i]) == max_num_rate[i]:
                truth_table[j] = 0

    least_common = contents[truth_table.index(1)]
    least_common = convert_string_to_dec(least_common)
    f.close()

    print(most_common*least_common)


##################################
def convert_array_to_dec(array):
    # define variables
    dec = 0
    digit = 0
    # cycle through all numebers
    for i in range(len(array)):

            dec = dec*2 + array[i] # calculate decimal number

    return dec # return result


##################################
def convert_string_to_dec(string):

    # define variables
    dec = 0
    digit = 0
    # cycle through all numebers
    for i in range(len(string)):
            if string[i] == '\n':
                continue
            dec = dec*2 + int(string[i]) # calculate decimal number

    return dec # return result


main()
