
def main():
    f = open("problem3data.txt","r") # load data as txt file

    gamma_rate = [0]*(len(f.readline())-1) # create an array with length of one line to store the final value

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
                gamma_rate[pos] = gamma_rate[pos] + 1
            # increase the position (up to 13)
            pos = pos + 1

    [gamma,epsilon] = convert_array_to_dec(gamma_rate) # pass the result of sum to function
    answer = gamma*epsilon # the final result
    print(answer)



def convert_array_to_dec(array):
    # define variables
    gamma = 0
    epsilon = 0
    digit = 0
    # cycle through all numebers
    for i in array:

            # redefine the answer to ones and zeros
            if(i < 500):
                digit = 0
            elif (i > 500):
                digit = 1
            gamma = gamma*2 + int(digit) # calculate decimal number

            # epsilon is the opposite of gamma (could be done faster probably)
            if(i < 500):
                digit = 1
            elif (i > 500):
                digit = 0
            epsilon = epsilon*2 + int(digit) # calculate decimal number

    return [gamma,epsilon] # return result

main()
