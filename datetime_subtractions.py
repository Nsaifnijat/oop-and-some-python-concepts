# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:17:36 2021

@author: Hamdard PC
"""

import pandas as pd
import datetime

s=pd.Series(pd.date_range('2012-1-1',periods=3, freq='D'))
td=pd.Series([pd.Timedelta(days=i) for i in range(3)])
df=pd.DataFrame({'A':s,"B":td})
df['C']=df['A']+df['B']
df.dtypes
s-(s.max())
s-datetime.datetime(2011,1,1,3,5)
print(df)