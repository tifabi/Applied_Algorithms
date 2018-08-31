import numpy as np
import time
import matplotlib.pyplot as plt

# set file path
#file = 'C:/Users/tiffany.fabianac/Desktop/Class/Applied_Algorithms/input.txt'
#file = 'C:/Users/tiffany.fabianac/Desktop/Class/Applied_Algorithms/input-30000numbers.txt'
file = 'C:/Users/tiffany.fabianac/Desktop/Class/Applied_Algorithms/input-100000numbers.txt'

# load file as numpy list
A_unsorted = np.loadtxt(file, delimiter="\t")

# create a sorted list to use as a verifier that the bublesort list is correct
verify = sorted(A_unsorted)

runTime = {}

for repeat in range(3):
    A = A_unsorted
    # reset interval for each repeat
    countInterval = 500

    # set start time
    t0 = time.clock()

    # bubblesort
    for i in range(len(A) - 1):
        for j in reversed(range(i + 1, len(A))):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]

        # add times for each interval
        if i + 1 == countInterval or i == len(A) - 2:
            t1 = time.clock()

            if countInterval not in runTime:
                runTime[countInterval] = (t1 - t0)
            else:
                runTime[countInterval] = (runTime[countInterval] + (t1 - t0)) / 2

            countInterval += 500

# verify that that original sorted list and the bubblesorted list match
for i in range(len(A)):
    if verify[i] != A[i]:
        print([i, verify[i], A[i]])

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
