from sklearn import datasets        #用来导入数据
from collections import Counter #为了投票
from sklearn.model_selection import train_test_split
import numpy as np 

#导入iris数据
iris = datasets.load_iris()
X = iris.data
y=iris.target
X_trian, X_test, y_train, y_test = train_test_split(X,y,random_state=3)

def euc_dis(instance1,instance2):
    '''
    计算欧式距离即两点间的距离
    instance1,instance2  array型
    '''
    dist = np.sqrt(sum((instance1-instance2)**2))
    return dist

def knn_classify(X,y,testInstance,k):
    '''
    给定一个训练数据testInstance,通过KNN算法来预测它的标签。
    X:训练数据的特征
    y:训练数据的标签
    testInstance:测试数据，这里假定一个测试数据 array型
    k:选择多少个neighbors?
    '''
    #TODO 返回testInstance的预测标签={0,1,2}
    distances = [euc_dis(x,testInstance) for x in X]
    kneighbors = np.argsort(distances)[:k]      #计算排名，转化为索引排序
    count = Counter(y[kneighbors])              #计算标签的数量
    return count.most_common()[0][0]            #返回数量最多的标签

if __name__=='__main__':
    #预测结果
    for k in range(1,13,2):
        predictions = [knn_classify(X_trian, y_train,data,k) for data in X_test]
        correct=np.count_nonzero((predictions==y_test)==True)   #通过比对预测的值和测试预留的值相对比得到正确的数量
        print('k=%d Accuracy is:%.3f'%(k,correct/len(X_test)))


