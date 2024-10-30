# 先看下数据
import pandas as pd
import numpy as np

# read in all our data
nfl_data = pd.read_csv("C:/Users/Jade Tong/Desktop/KAGGLE/Data Cleaning/NFL Play by Play 2009-2017 (v4).csv")

# set seed for reproducibility
np.random.seed(0) 

nfl_data.head()

#%% 有多少缺失值
missing_values_count = nfl_data.isnull().sum()
missing_values_count[0:10]  #前10个特征的缺失值数
#Date                0
#GameID              0
#Drive               0
#qtr                 0
#down            61154
#time              224
#TimeUnder           0
#TimeSecs          224
#PlayTimeDiff      444
#SideofField       528

#%%  看看缺失值占矩阵的比例
total_cells = np.product(nfl_data.shape) #矩阵的笛卡尔积
total_missing = missing_values_count.sum() #缺失值数

(total_missing/total_cells) * 100
# 27.67% 缺失率有点大了啊

#%% 数据缺失是因为它没有被记录还是不存在？
#如果是不应该存在的数据，你就keep it as NaN；如果是数据没被记录，那就填充它
missing_values_count[0:10]
#Date                0
#GameID              0
#Drive               0
#qtr                 0
#down            61154
#time              224
#TimeUnder           0
#TimeSecs          224
#PlayTimeDiff      444
#SideofField       528

#%% drop missing data
#如果没有办法搞清楚为什么数据缺失，那其中一个办法是删除有缺失值的行或者列（不推荐)
nfl_data.dropna()    #删除有缺失值的行

nfl_data.dropna(axis=1)   #删掉有缺失值的列

columns_with_na_dropped = nfl_data.dropna(axis=1)
columns_with_na_dropped.head()
#特征从102个被删剩37个

#%%          另一个方法是填充缺失值
#用数据集里切割一个小集来演示一下
subset_nfl_data = nfl_data.loc[:, 'EPA':'Season'].head()
subset_nfl_data
#%% 用0将缺失值代替
subset_nfl_data.fillna(0)

#%% 用空值后一个位置的数据填充它（make sense如果观察值带有某种逻辑顺序）
#后面有数据的填充数据，没有数据的填充0
subset_nfl_data.bfill().fillna(0)















