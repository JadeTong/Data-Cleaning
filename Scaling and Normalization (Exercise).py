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

kickstarters_2017=pd.read_csv('C:/Users/Jade Tong/Desktop/KAGGLE/Data Cleaning/ks-projects-201801.csv')
#%% 将每场campaign的筹款目标缩放到0-1之间
original_data = pd.DataFrame(kickstarters_2017.usd_goal_real)

# scale the goals from 0 to 1
scaled_data = minmax_scaling(original_data, columns=['usd_goal_real'])

print('Original data\nPreview:\n', original_data.head())
print('Minimum value:', original_data.min(),
      '\nMaximum value:', original_data.max())
print('_'*30)

print('\nScaled data\nPreview:\n', scaled_data.head())
print('Minimum value:', scaled_data.min(),
      '\nMaximum value:', scaled_data.max())
#%%  标准化每场筹款的pledged金额
#取正值 (Box-Cox变换只能处理正值)
positive_pledges=kickstarters_2017.usd_pledged_real.loc[kickstarters_2017.usd_pledged_real > 0]

# normalize the pledges (w/ Box-Cox)
normalized_pledges = pd.Series(stats.boxcox(positive_pledges)[0], 
                               name='usd_pledged_real', index=positive_pledges.index)

print('Original data\nPreview:\n', positive_pledges.head())
print('Minimum value:', float(positive_pledges.min()),
      '\nMaximum value:', float(positive_pledges.max()))
print('_'*30)

print('\nNormalized data\nPreview:\n', normalized_pledges.head())
print('Minimum value:', float(normalized_pledges.min()),
      '\nMaximum value:', float(normalized_pledges.max()))

#%% plot normalized data
ax = sns.histplot(normalized_pledges, kde=True)
ax.set_title("Normalized data")
plt.show()















