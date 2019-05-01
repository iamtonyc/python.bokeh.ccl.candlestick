from bokeh.plotting import figure, output_file, show
import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import CustomJS, ColumnDataSource, HoverTool, NumeralTickFormatter
from get_ccl2_data import get_ccl2_data_from_csv

# https://bokeh.pydata.org/en/latest/docs/user_guide/tools.html

def line_plot(df, name):
	xaxis_dt_format = '%Y-%m-%d'
	source = ColumnDataSource(data=dict(
		index = df.index,
		ccl= df.Ccl,
		date=df.Date,
		sma52_096=df.Sma52_096,
		sma52_106=df.Sma52_106
	))

	tooltips=[
	            ("Date", "@date{" +  '%Y-%m-%d' + "}"),
	            ("CCL", "$y"),
	            ("52 Week Moving Average X 0.96", "@sma52_096"),
	            ("52 Week Moving Average X 1.06", "@sma52_106"),
		     ]


	fig = figure(sizing_mode='stretch_both',
                 tools="crosshair,xpan,xwheel_zoom,reset,save",
                 active_drag='xpan',
                 active_scroll='xwheel_zoom',
                 x_axis_type='linear',
                # x_range=Range1d(df.index[0], df.index[-1], bounds="auto"),
                # x_range=(df.index[0], df.index[-1]),
                 title=name,
                 tooltips=tooltips
                 )
	fig.yaxis[0].formatter = NumeralTickFormatter(format="5.3f")


	fig.line(df.index, df['ccl'],line_width=3)
	fig.line(df.index, df['sma52 X 0.96'],line_width=1, color='#B2DF8A', legend='52 Week Moving Average X 0.96')
	fig.line(df.index, df['sma52 X 1.06'],line_width=1, color='#FB9A99', legend='52 Week Moving Average X 1.06')
	fig.legend.location = "top_left"

	fig.xaxis.axis_label = 'Date'
	fig.yaxis.axis_label = 'CCL'
	fig.ygrid.band_fill_color = "olive"
	fig.ygrid.band_fill_alpha = 0.1

	# Add date labels to x axis
	
	fig.xaxis.major_label_overrides = {i: date.strftime(xaxis_dt_format) for i, date in enumerate(pd.to_datetime(df["Date"]))}

	

 #    # Finalise the figure
	show(fig)




# Main function
if __name__ == '__main__':
	xaxis_dt_format = '%Y-%m-%d'
	df=get_ccl2_data_from_csv("https://raw.githubusercontent.com/iamtonyc/ccl.data/master/ccl.csv")
	df['sma52'] = df['ccl'].rolling(window=52).mean()
	# df=df.sort_values(by=['date'],ascending=False)
	df=df.reset_index(drop=True)
	df['sma52 X 0.96']=df['sma52']*0.96
	df['sma52 X 1.06']=df['sma52']*1.06

	df['Date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')  # Adjust this
	df.Ccl=df['ccl']
	df.Date=df['Date']
	df.Sma52_096=df['sma52 X 0.96']
	df.Sma52_106=df['sma52 X 1.06']


	output_file("ccl2_plot.html")
	line_plot(df, "CCL with 0.96 X 52 Week Moving Average and 1.06 X 52 Week Moving Average ")



			
			