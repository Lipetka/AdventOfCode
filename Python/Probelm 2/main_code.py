
f = open("problem2data.txt") # load data as txt file

# define main function
def main():
    print(str(determinePoisitionSimple())) # print the returned result

def determinePoisitionSimple():
    depth = 0 # init position
    vertical = 0 # init position

    for i in f:
        # every i is a new line
        # count the moves

        command = i.split() #split by whitespace

        # determine the command and the added/substracted value

        if(command[0] == "forward"):
            vertical += int(command[1])
        elif(command[0] == "down"):
            depth += int(command[1])
        elif(command[0] == "up"):
            depth -= int(command[1])
        else:
            print("error")

    # final check of correct position

    finalCheck = depth*vertical
    return finalCheck

def determinePoisitionComplicated():
    #TBD
    pass

main()
