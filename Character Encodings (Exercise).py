# modules we'll use
import pandas as pd
import numpy as np

# helpful character encoding module
import charset_normalizer

# set seed for reproducibility
np.random.seed(0)

#%%
sample_entry = b'\xa7A\xa6n'
print(sample_entry)
print('data type:', type(sample_entry))
# b'\xa7A\xa6n'
# data type: <class 'bytes'>

#%% 将sample_entry的编码转化为UTF-8，注意字符串现在的编码为‘大五码’（"big5-tw"）
# 先解码decode，再转码encode到utf-8
print(sample_entry.decode('big5-tw'))
new_entry = sample_entry.decode('big5-tw').encode('utf-8')
print(new_entry)

#%% 读入有编码错误的数据文件
police_killings = pd.read_csv("C:/Users/Jade Tong/Desktop/KAGGLE/Data Cleaning/PoliceKillingsUS.csv")
#显示数据不是'utf-8'编码

#%% 检查一下数据的编码类型，注意！！检查数据集的参数要大于数据集实际量，hence the 1000000
with open("C:/Users/Jade Tong/Desktop/KAGGLE/Data Cleaning/PoliceKillingsUS.csv", 'rb') as rawdata:
    result = charset_normalizer.detect(rawdata.read(1000000))
print(result)
#{'encoding': 'windows-1250', 'language': 'English', 'confidence': 1.0}
#编码是'windows-1250'

#%%
police_killings = pd.read_csv("C:/Users/Jade Tong/Desktop/KAGGLE/Data Cleaning/PoliceKillingsUS.csv",
                              encoding='windows-1250')

#%% 将数据集保存为UTF-8编码
police_killings.to_csv('C:/Users/Jade Tong/Desktop/KAGGLE/Data Cleaning/PoliceKillingsUS_UTF-8.csv')



















