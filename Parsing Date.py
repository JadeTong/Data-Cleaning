#数据是发生于2007年到2016年之间的山泥倾泻
import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# set seed for reproducibility
np.random.seed(0)

# read in our data
landslides = pd.read_csv("C:/Users/Jade Tong/Desktop/KAGGLE/Data Cleaning/catalog.csv")
landslides.head()

#%%重点看一下时间戳‘date’
print(landslides['date'].head())
#0     3/2/07
#1    3/22/07
#2     4/6/07
#3    4/14/07
#4    4/15/07
#Name: date, dtype: object
#似乎python不知道这特征是日期，因为日期的dtype是'datetime64'而不是'object'

#也可以用.dtype来查看
landslides['date'].dtype
#dtype('O')

#%%将特征转换为日期类型，最常见年月日为 %Y（四位年份）或%y（两位年份）、%m和%d
#新建一个列'date_parsed'
landslides['date_parsed'] = pd.to_datetime(landslides['date'], format="%m/%d/%y")
landslides['date_parsed'].head()
#0   2007-03-02
#1   2007-03-22
#2   2007-04-06
#3   2007-04-14
#4   2007-04-15
#Name: date_parsed, dtype: datetime64[ns]

#如果数据里面有多种不同格式的日期，那可以让pandas自动识别格式然后转化
#landslides['date_parsed'] = pd.to_datetime(landslides['Date'],infer_datetime_format=True)

#%%从转化好的日期中提取信息
day_of_month_landslides = landslides['date_parsed'].dt.day
day_of_month_landslides.head()

#%% 画直方图看看山泥倾泻的具体日子day，来double check一下数据有没有出错
#预计区间是1-31，因为山泥倾泻并不被日期影响，所以应该是均匀分布，且31号下倾
#去除缺失值
day_of_month_landslides = day_of_month_landslides.dropna()
# plot the day of the month
sns.distplot(day_of_month_landslides, kde=False, bins=31)


































