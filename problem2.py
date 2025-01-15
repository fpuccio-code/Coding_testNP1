# Write a python program that takes a list of file names.
# Each file name refers to a provided CSV file without a header and with three columns representing a batch of values of Ai, Bi and Wi.
# All Wi values are positive. The program outputs values Xi that maximizes sum(Ai*Xi - Wi*Xi^2) subject to constraint sum(Bi*Xi)=0,
# where summation is performed over values from all the files. The sizes of arrays are such that a single batch of values fits in memory, 
# but none of the full length arrays A, B, W, X fit in memory.

import pandas as pd
import numpy as np


#test input name1="file1.csv", name2="file2.csv", name3="file3.csv"
data={"Ai":np.random.random(10), "Bi":np.random.random(10), "Wi":np.random.random(10)}
df = pd.DataFrame(data,columns=[ "Ai", "Bi", "Wi"])
df.to_csv("file1.csv")

data={"Ai":np.random.random(10), "Bi":np.random.random(10), "Wi":np.random.random(10)}
df = pd.DataFrame(data,columns=[ "Ai", "Bi", "Wi"])
df.to_csv("file2.csv")

data={"Ai":np.random.random(10), "Bi":np.random.random(10), "Wi":np.random.random(10)}
df = pd.DataFrame(data,columns=[ "Ai", "Bi", "Wi"])
df.to_csv("file3.csv")


def solution2(name1,name2,name3):
    df1=pd.read_csv(name1)
    df2=pd.read_csv(name2)
    df3=pd.read_csv(name3)
    
    
    A=np.array(pd.concat([df1,df2,df3]).reset_index()["Ai"])
    B=np.array(pd.concat([df1,df2,df3]).reset_index()["Bi"])
    W=np.array(pd.concat([df1,df2,df3]).reset_index()["Wi"])
    
    #Lagrangian multiplier solution
    l=np.sum(B*B/(2*W))
    X=np.multiply((l*B+A),2*W)
    
    return X


