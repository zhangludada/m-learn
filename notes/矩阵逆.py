import numpy as np
import random


def r():
    return random.randint(0,10)

#建立一个矩阵，必须为mat
a=list([r(),r(),r(),r()] for x in range(4))
a=np.array(a)
a=np.mat(a)
#求矩阵的逆
b=a.I




