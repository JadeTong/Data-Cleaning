import pandas as pd
import numpy as np

# helpful character encoding module
import charset_normalizer

# set seed for reproducibility
np.random.seed(0)

#%% 字符编码：从二进制到可读的文字
#UTF-8是标准的文本编码，所有Python代码都是UTF-8，ideally数据也应该是。

#把Unicode编码转化为“可变长编码”
#UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。

#%%  string是文本的默认类型
before = "This is the euro symbol: €"
type(before)     #str

#%% bytes 字节
#可以将string转化为bytes by specifying which encoding it's in:
after = before.encode("utf-8", errors="replace")
type(after)      #bytes

#%% 看下after变成什么
after
# b'This is the euro symbol: \xe2\x82\xac'

#%%
print(after.decode("utf-8"))
#This is the euro symbol: €

#%%
# try to decode our bytes with the ascii encoding
print(after.decode("ascii"))

#%%
kickstarters=pd.read_csv('C:/Users/Jade Tong/Desktop/KAGGLE/Data Cleaning/ks-projects-201801.csv')

#%%
with open("C:/Users/Jade Tong/Desktop/KAGGLE/Data Cleaning/ks-projects-201801.csv", 'rb') as rawdata:
    result = charset_normalizer.detect(rawdata.read(1000000))
print(result)












