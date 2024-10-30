#数据缩放（一般为归一化）和标准化与它们之间的区别
import pandas as pd
import numpy as np

# for Box-Cox Transformation
from scipy import stats

# for min_max scaling
from mlxtend.preprocessing import minmax_scaling

# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt

# set seed for reproducibility
np.random.seed(0)

#%%
# scaling means将数据缩放到某个具体区间, like 0-100 or 0-1.
#当用到基于数据点之间的距离的算法时，就要先scale，如SVM和KNN
#By scaling your variables, you can help compare different variables on equal footing.

#%% 生成1000个服从指数分布的随机数
original_data = np.random.exponential(size=1000)

# mix-max scale the data between 0 and 1  将数据归一化
scaled_data = minmax_scaling(original_data, columns=[0])

# 画分布图比较两组数据有什么不同
fig, ax = plt.subplots(1, 2, figsize=(15, 3))
sns.histplot(original_data, ax=ax[0], kde=True, legend=False)
ax[0].set_title("Original Data")
sns.histplot(scaled_data, ax=ax[1], kde=True, legend=False)
ax[1].set_title("Scaled data")
plt.show()
#scaling不会改变分布，改变数据的range

#%%   Normalization 标准化
#标准化程序将数据分布正态化，如果要使用到机器学习或者假设你的数据为正态分布的统计技巧时，就要事先标准化数据
# normalize the exponential data with boxcox 
normalized_data = stats.boxcox(original_data)

# plot both together to compare
fig, ax=plt.subplots(1, 2, figsize=(15, 3))
sns.histplot(original_data, ax=ax[0], kde=True, legend=False)
ax[0].set_title("Original Data")
sns.histplot(normalized_data[0], ax=ax[1], kde=True, legend=False)
ax[1].set_title("Normalized data")
plt.show()

#分布从L型变为类似正态分布























