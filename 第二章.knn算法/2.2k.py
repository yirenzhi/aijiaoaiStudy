#2.2 K近邻的决策边界以及K的影响
import matplotlib.pyplot as plt 
import numpy as np 
from itertools improt product 
from sklearn.neighbors import KNeighborsClassifier

#生成随机样本
n_point = 100
X1 = np.random.multivariate_normal([1,50],[[1,0],[0,10]],n_point)
X2 = np.random.multivariate_normal([2,50],[[1,0],[0,10]],n_point)
X = np.concatenate([X1,X2])
y = np.array([0]*n_point+[1]*n_point)
print(X.shape,y.shape)

#kNN模型的训练过程
clfs=[]
for k in range(1,20,2):
    clfs.append(KNeighborsClassifier(n_neighbors=k).fit(X,y))

#可视化结果
x_min, x_max = X[:,0].min()-1,X[:,0].max()+1
y_min, y_max = X[:,1].min()-1,X[:,1].max()+1

xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

