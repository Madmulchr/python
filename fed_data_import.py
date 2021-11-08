#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader.data import DataReader
from datetime import date #date&time functionality

#https://fred.stlouisfed.org/

series_code= 'DGS10'#10yr T rate

data_source = 'fred' #fed Economic Data Service

start = date(1962, 1, 1)

data = DataReader(series_code, data_source, start)

series_name = '10 Year Treasury' #renaming column --> .rename(columns={old_name: new_name})

data = data.rename(columns={series_code: series_name})

data.plot(title=series_name); plt.show()


