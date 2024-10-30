import pandas as pd
import numpy as np

# helpful modules
import fuzzywuzzy
from fuzzywuzzy import process
import charset_normalizer

# set seed for reproducibility
np.random.seed(0)

# read in all our data
professors = pd.read_csv("C:/Users/Jade Tong/Desktop/KAGGLE/Data Cleaning/pakistan_intellectual_capital.csv")
professors.head()

#%% 查一下'Country'这列有没有inconsistencies
#看下这列有多少个unique values
countries=professors.Country.unique()
countries.sort()
countries

#%% 可以看到前几个国家名前有一个空格，后面的有一个'USofA'和一个开头小写的'germany'
#先把所有的国家名改成开头小写，然后将空格删掉
# 改小写
professors['Country'] = professors['Country'].str.lower()
# 删空格
professors['Country'] = professors['Country'].str.strip()  #.strip()可以将字符串前面或者后面的空格删掉

#%% 用fuzzy来改
# 再看看'Countrty'这列有没有inconsistency
countries=professors.Country.unique()
countries.sort()
countries
#还有一个问题，'south korea','southkorea'

#%% fuzzywuzzy可以检测到数据中的相似的字符串，返回两个字符串之间的相似比，越靠近100越相似
matches = fuzzywuzzy.process.extract("south korea", countries, limit=5, 
                                     scorer=fuzzywuzzy.fuzz.token_sort_ratio)
matches
#[('south korea', 100),
# ('southkorea', 48),
# ('saudi arabia', 43),
# ('norway', 35),
# ('ireland', 33)]

#%% 将'sounthkorea'改为'south korea'
southkorea_index=professors.Country=='southkorea'
professors.loc[southkorea_index,'Country']='south korea'
# 再看看'Countrty'这列有没有inconsistency
countries=professors.Country.unique()
countries.sort()
countries
