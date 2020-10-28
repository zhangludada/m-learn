import numpy as np
import random

def r():
    return random.randint(0,10)

#建立一个矩阵，必须为mat
a=np.mat(np.arange(20).reshape(10,2))
#矩阵转置
print(a.T)
