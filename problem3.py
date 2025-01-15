# Write Python code that performs the following computation. 
# Given a numpy length N floating point array A (1<=A[i]<=2) and a numpy length N integer array S (0<=S[i]<=i),
# return length N floating point numpy array X with elements X[i] = sum of A[k] * exp(-50*k/N)) for k in range S[i]<=k<=i. 
# The value of N is around 100000000. Implementation with python loop over all elements is not considered sufficiently efficient.

import numpy as np

#input test
N=100
A=np.linspace(1,2,N)
S=np.array([0]+[np.random.randint(0,i) for i in range(1,N)])


def solution3(A,S,N):
    R=np.tile([np.arange(0,N,1)], (N, 1))
    Rt=R.transpose()
    s=np.tile([S], (N, 1))
    cond1= (R-Rt < 0).astype(int)
    cond2=(S-R < 0).astype(int)
    cond=np.logical_and(cond1,cond2)
    return cond*(A*np.exp(-(50/N)*np.arange(0,N,1)))
