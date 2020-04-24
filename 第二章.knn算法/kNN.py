#机器学习实战第二章内容
from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX, dataSet, labels,k):
    dataSetSize = dataSet.shape[0] #shape返回数组的维度
    diffMat = tile(inX, (dataSetSize,1)) - dataSet  #tile瓷砖的意思，把数组像瓷砖一样铺展开来,计算原矩阵和0矩阵的差
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)     #axis=1矩阵每行的和，axis=0矩阵每列的和
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1     #每有一个目标值+1

    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

