#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv
import glob


# In[2]:


path = r'C:\Users\elampa\Desktop\citibike\ridedata' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
frame.head()


# In[ ]:


frame.to_csv(r'C:\Users\elampa\Desktop\citibike\agg_data1018_032019.csv')


# In[ ]:




