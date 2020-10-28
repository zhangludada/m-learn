import numpy as np

#if a=x,b=3,y=2x+3 == [5,7,9]
#a为样本 1,2,3
#把a做成3*2的矩阵
a=[[1,1],[2,1],[3,1]]
a=np.mat(a)

#假设线性关系
x=[[2],[3]]
x=np.mat(x)
#矩阵dot(a,x)就是要求的y
y=np.dot(a,x)
print(y)



