#特征缩放

'''
1.线性归一化(Min-max Normalization)
x(new) = (x-min(x))/(max(x)-min(x))
2.标准差标准化(Z-score Normalization)
x(new) = (x-avg(x))/std(x)
std(x)标准差   sqrt(x-avg(x)**2/len(x))
其中，线性归一化指的是把特征值的范围映射到[0,1]区间，标准差标准化的方法使得把特征值映射到均值为0，标准差为1的正态分布。
'''