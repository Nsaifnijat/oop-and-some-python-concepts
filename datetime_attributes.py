# -*- coding: utf-8 -*-

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
df=pd.read_csv('concepts\multiple.csv',header=[0,1],index_col=[0],parse_dates=[0])
closha=df.loc[:,'Close'].copy()

#its used only when there is date index, not datetime index
closha.index
closha.index.day
closha.index.day_name()
closha.index.weekday_name()
closha.index.month_name()
closha.index.weekday
closha.index.quarter
closha.index.days_in_month
closha.index.week
closha.index.weekofyear
closha.index.is_month_end