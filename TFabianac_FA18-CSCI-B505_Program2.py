import numpy as np
import time
import matplotlib.pyplot as plt

def plotResults(runTime):
    # create a sorted list of tuples from the run time dictionary
    sortedTime = sorted(runTime.items())

    # plot the run times
    x_val, y_val = zip(*sortedTime)
    plt.plot(x_val, y_val)
    plt.plot(x_val, y_val, 'or')
    plt.title('Mean Run Time for Each Interval')
    plt.xlabel('n Sorted')
    plt.ylabel('Mean Run Time')
    plt.show()

def updateTime(runTime_dict, countInterval_num, startTime, endTime):
    # if the countInterval is not in the runTime dictionary add it
    if countInterval_num not in runTime_dict:
        runTime_dict[countInterval_num] = (endTime - startTime)

    # if the countInterval is in the runTime dictionary, take average, add average
    else:
        runTime_dict[countInterval_num] = (runTime_dict[countInterval_num] + (endTime - startTime)) / 2



file = 'input_p2.txt'

# load file as numpy list
input_list = np.loadtxt(file, delimiter="\t")

runTime = {}
maxDict = {}
countInterval = 1000
maxBrute = -1000
maxBruteList = []

while countInterval <= 5000:
    testList = [input_list[i] for i in range(countInterval)]
    for repeat in range(1):
        # set start time
        t0 = time.clock()

        # brute force
        for i in range(countInterval):
            numCombo = []
            for y in testList[i:]:
                numCombo.append(y)
                checkSum = np.sum(numCombo)
                if checkSum > maxBrute:
                    maxBrute = checkSum
                    maxBruteList = [numCombo[0], numCombo[-1]]

    # add times for each interval
    if i + 1 == countInterval or i == len(testList) - 2:
        t1 = time.clock()
        updateTime(runTime, countInterval, t0, t1)
    maxDict[countInterval] = [maxBrute, maxBruteList]
    # increase countInterval after 3 runs with the same interval
    countInterval += 1000

print(maxDict)
plotResults(runTime)



