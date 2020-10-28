import numpy as np

#y为正确结果
y=1
#x为样本数据
x=np.mat([1])

#正规方程，求极值
o=(x.T*x).I*x.T*y