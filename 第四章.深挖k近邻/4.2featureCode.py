#特征编码
'''
-标签编码：把字符的值替换成数字的值  如果类别没有大小关系，不可取
-独热编码：适用于类别特征（没有大小关系）
0:(1,0,0)  1:(0,1,0)  2:(0,0,1) 

-变量的离散化（Discretization）
通过区域映射将数据变小且非线性化，再用独热编码 
'''