import numpy as np

def rebinning(data):
    Nch = 8192
    rbNch = 2**9
    K = int(Nch/rbNch)
    
    rbxch = np.zeros(rbNch)
    for i in range(rbNch):
        rbxch[i] = K*i
        
    rbdata = np.zeros(rbNch)
    for i in range(rbNch):
        for j in range(K):
            rbdata[i] += data[i*K+j] 
    return rbxch, rbdata