import numpy as np
def my_pascal(dim):

    P = np.zeros((dim, dim))
    for i in range(dim):
        P[i,0],P[0,i] = 1,1
    for i in range(1,dim):
        for j in range(1,dim):
            if i>j:
                P[i,j] = P[i-1,j-1+1] + P[i-1+1,j-1]
    return P 
print(my_pascal(6))

