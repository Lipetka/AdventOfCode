#ADVENT OF CODE PROBLEM 1 : https://adventofcode.com/2021/day/1

import problem1data as input #import the data

# number of times the depth has decreased

# define the main function
def main():

    decreaseManeuvers = depthChangeSum() # get the number of decrease times
    print("The depth has increased " + str(decreaseManeuvers) + " times") # print the answer

    betterMeasurementSum = meanChangeSum() # get the filtered data
    print("After filtering the data the depth has increased "+str(betterMeasurementSum)+" times")


def depthChangeSum():

    depthIncr = 0 # init the variable

    for i in range(len(input.data)): # get the size of data
        if(input.data[i] > input.data[i-1]): # check if the new value is higher than previous value
            depthIncr += 1 # if the depth has increased, add counter

    return depthIncr

def meanChangeSum():

    depthIncr = 0 # init the variable

    for i in range(len(input.data)): # get the size of data

        currentValue = input.data[i] + input.data[i - 1] + input.data[i - 2] # calculate current value
        previousValue = input.data[i - 1] + input.data[i - 2] + input.data[i - 3] # calculate last value

        if(currentValue > previousValue): # if the current value if higher than the sub has sank
            depthIncr += 1 # add 1 to counter

    return depthIncr



main() # init of main
