def get_ccl2_data_from_excel(fileName):
	import pandas as pd

	xls = pd.ExcelFile(fileName)
	df = xls.parse("Sheet1")
	return get_ccl2_data_from_data_frame(df)



def get_ccl2_data_from_csv(url):
	import pandas as pd
	
	df=pd.read_csv(url,parse_dates=['date'])
	return get_ccl2_data_from_data_frame(df)	


def get_ccl2_data_from_data_frame(df):
	import numpy as np
	import pandas as pd
	import matplotlib as plt
	#import seaborn as sns
	import matplotlib.dates as date
	import datetime
	#%matplotlib inline
	from numpy.random import randn

	df['0.96']=df['ccl']*0.96
	df['1.06']=df['ccl']*1.06

	return df