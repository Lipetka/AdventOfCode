# problem 1

# Rock Papier Scissors
# Calculate the overall points

from functions import *                     # import all functions from functions.py

################ PART 1 ################

input_file = '2022\Problem2\input.txt'      # path to input file
data = open(input_file,'r')                 # open input file
points = 0                                  # initialize points calculator

# iterate through input data and sum all points


for line in data:
    points = points + pointsForChosenPlay(line)     # add points for chosen play
    points = points + pointsForWinning(line)        # add points for winning

print("Total points: " + str(points))




