import numpy as np
# Write a Python function that takes numpy array of booleans and returns a numpy array of type int64. 
# The i-th element in the resulting array should contain the distance from the closest true in the input array at or before position i.
# The resulting array should have a -1 if there is no True value at the current or any previous position. 
# The input array size will be on the order of 1e8, number of true value is of the order of 1e7. 
# Implementation with python loop over all elements or over all true values is not considered sufficiently efficient.


#generate random bool array (input test)
test= np.random.randint(2, size=20, dtype=bool)

def solution1(test):
    #convert to int
    testint =test.astype(int)

    #index where 0
    pos0 = np.where(testint == 0)[0]
    # set 0 -> -1
    testint[pos0]=-1

    #index where 1
    pos1 = np.where(testint == 1)[0]

    #distance on the left
    distm = abs(pos1-np.roll(pos1,-1))

    #distance on the rigth
    distp = abs(pos1-np.roll(pos1,1))

    #set distances
    testint[pos1] = np.minimum(distm,distp)

    return testint

print(test)
print(solution1(test))
exit()