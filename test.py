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
from get_ccl1_data import get_ccl1_data_from_csv

df = get_ccl1_data_from_csv("https://raw.githubusercontent.com/iamtonyc/ccl.data/master/ccl.csv")

df.head()
