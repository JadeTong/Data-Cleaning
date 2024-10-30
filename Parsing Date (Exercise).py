import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# read in our data
earthquakes = pd.read_csv("C:/Users/Jade Tong/Desktop/KAGGLE/Data Cleaning/database.csv")

# set seed for reproducibility
np.random.seed(0)

earthquakes.head()

#%%检查日期列的字符串类型
earthquakes.Date.dtype
#dtype('O')  为object，不是datetime64

#%%将数据类型转换成日期格式，entry3378的格式不符合month/day/year
earthquakes.Date[3378:3383] 
#1975-02-23T02:58:41.000Z，是日期和时间的结合

#%%看一下这样的异常数据有多少个
date_lengths = earthquakes.Date.str.len()
date_lengths.value_counts()
#Date
#10    23409
#24        3    异常值有三个

#%%定位三个异常值的index
indices = np.where([date_lengths == 24])[1]
print('Indices with corrupted data:', indices)
earthquakes.loc[indices]

#%%新建一列，叫'date_parsed'将日期格式化，将异常值分开处理
#先将异常字符串切割成日期
earthquakes.Date=earthquakes.Date.str.split('T',expand=True)[0]
#但是那三个异常的格式与其它不同，所以format='mixed'
earthquakes['date_parsed']=pd.to_datetime(earthquakes.Date,format='mixed')

#%% 抽取日期中的精确日子day of the month
day_of_month_earthquakes = earthquakes.date_parsed.dt.day

#%% 画day of the month的直方图
day_of_month_earthquakes=day_of_month_earthquakes.dropna()
sns.histplot(day_of_month_earthquakes, kde=False, bins=31)
























