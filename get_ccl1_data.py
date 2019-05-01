def get_ccl1_data_from_excel(fileName):
	import pandas as pd

	xls = pd.ExcelFile(fileName)
	df = xls.parse("Sheet1")
	return get_ccl1_data_from_data_frame(df)



def get_ccl1_data_from_csv(url):
	import pandas as pd
	
	df=pd.read_csv(url,parse_dates=['date'])
	return get_ccl1_data_from_data_frame(df)	




def get_ccl1_data_from_data_frame(df):
	import numpy as np
	import pandas as pd
	import matplotlib as plt
	#import seaborn as sns
	import matplotlib.dates as date
	import datetime
	#%matplotlib inline
	from numpy.random import randn
	import plotly
	import plotly.plotly as py
	import plotly.graph_objs as go
	import os

	#plotly.tools.set_credentials_file(username='iamtonyc', api_key='9Q3RlU4RrMOpm8AFAMzX')
	# filename, file_extension = os.path.splitext(filename)
	# if file_extension==".csv"
	# df = pd.read_csv('https://raw.githubusercontent.com/iamtonyc/ccl.data/master/ccl.csv',parse_dates=['date'])



	dfMonthHigh=df.groupby(df['date'].dt.strftime('%Y-%m'))['ccl'].max().sort_values()
	dfMonthHigh=dfMonthHigh.reset_index()

	dfMonthLow=df.groupby(df['date'].dt.strftime('%Y-%m'))['ccl'].min().sort_values()
	dfMonthLow=dfMonthLow.reset_index()

	dfOpenDate=df.groupby(df['date'].dt.strftime('%Y-%m'))['date'].min().sort_values()
	dfOpenDate=pd.DataFrame({'month':dfOpenDate.index, 'open_date':dfOpenDate.values})
	dfOpenDate=dfOpenDate.set_index('month')
	dfMergeOpenDate=dfOpenDate.merge(df,left_on='open_date',right_on='date')
	dfMonthOpen=dfMergeOpenDate.groupby(dfMergeOpenDate['open_date'].dt.strftime('%Y-%m'))['ccl'].min().sort_values()
	dfMonthOpen=dfMonthOpen.reset_index()
	dfMonthOpen.columns=['date','ccl']

	dfCloseDate=df.groupby(df['date'].dt.strftime('%Y-%m'))['date'].max().sort_values()
	dfCloseDate=pd.DataFrame({'month':dfCloseDate.index, 'close_date':dfCloseDate.values})
	dfCloseDate=dfCloseDate.set_index('month')
	dfMergeCloseDate=dfCloseDate.merge(df,left_on='close_date',right_on='date')
	dfMonthClose=dfMergeCloseDate.groupby(dfMergeCloseDate['close_date'].dt.strftime('%Y-%m'))['ccl'].max().sort_values()
	dfMonthClose=dfMonthClose.reset_index()
	dfMonthClose.columns=['date','ccl']

	dfMerge1=dfMonthOpen.merge(dfMonthHigh, on='date')
	dfMerge1=dfMerge1.merge(dfMonthLow, on='date')
	dfMerge1=dfMerge1.merge(dfMonthClose, on='date')

	dfMerge1.columns=['month','open','high','low','close']

	dfMerge1=dfMerge1.sort_values(by=['month'])
	dfMerge1=dfMerge1.reset_index(drop=True)

	return dfMerge1
