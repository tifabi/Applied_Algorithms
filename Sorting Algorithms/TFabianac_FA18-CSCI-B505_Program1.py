import numpy as np
import time
import matplotlib.pyplot as plt

# set file path
file = 'C:/Users/tiffany.fabianac/Desktop/Class/Applied_Algorithms/input.txt'
#file = 'C:/Users/tiffany.fabianac/Desktop/Class/Applied_Algorithms/input-30000numbers.txt'
#file = 'C:/Users/tiffany.fabianac/Desktop/Class/Applied_Algorithms/input-100000numbers.txt'

# load file as numpy list
A_unsorted = np.loadtxt(file, delimiter="\t")

# create a sorted list to use as a verifier that the bublesort list is correct
verify = sorted(A_unsorted)

runTime = {}
countInterval = 500

while countInterval <= len(A_unsorted):
    for repeat in range(3):
        # reset interval for each repeat
        A = A_unsorted

        # set start time
        t0 = time.clock()

        # create a boolean to check if the list is sorted
        sortBoolean = True

        # bubblesort
        for i in range(countInterval):
            for j in reversed(range(i + 1, countInterval)):
                if A[j] < A[j - 1]:
                    A[j], A[j - 1] = A[j - 1], A[j]
                    # if the input requires an exchange, it is unsorted, the sortBoolean will be set to False
                    sortBoolean = False
            # if a whole inner loop is made without needing to sort, break, the input is sorted
            if sortBoolean == True:
                break

            # add times for each interval
            if i + 1 == countInterval or i == len(A) - 2:
                t1 = time.clock()
                # if the countInterval is not in the runTime dictionary add it
                if countInterval not in runTime:
                    runTime[countInterval] = (t1 - t0)
                # if the countInterval is in the runTime dictionary, take average, add average
                else:
                    runTime[countInterval] = (runTime[countInterval] + (t1 - t0)) / 2

    # increase countInterval after 3 runs with the same interval
    countInterval += 500


# verify that that original sorted list and the bubblesorted list match
if countInterval > len(A_unsorted):
    print('Checking Order...')
    checkCorrect = []
    for i in range(len(A)):
        if verify[i] != A[i]:
            checkCorrect.append([i, verify[i], A[i]])
    if len(checkCorrect) > 0:
        print('Ordered Lists Do Not Match! Check Variables:\n'
              'List Position, Sorted, BubbleSort'
              ' \n{}'.format(checkCorrect))
    else:
        print('Ordered Lists Match!')

# create a sorted list of tuples from the run time dictionary
sortedTime = sorted(runTime.items())

#plot the run times
x_val, y_val = zip(*sortedTime)
plt.plot(x_val,y_val)
plt.plot(x_val,y_val,'or')
plt.title('Mean Run Time for Each Interval of 500 Sorted Values')
plt.xlabel('n Sorted')
plt.ylabel('Mean Run Time')
plt.show()