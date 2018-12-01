#!/usr/bin/python
from fbprophet import Prophet
import numpy as np
import pandas as pd

import plotly.plotly as py
import plotly
import plotly.graph_objs as go


sales_df = pd.read_csv('retail_sales.csv',parse_dates=['ds'])

#Plotly account credentials
plotly.tools.set_credentials_file(username='bajwa.kanwar',api_key='VEYcqOPQsxNyBR1OTSfd')

model = Prophet(daily_seasonality=True,changepoint_prior_scale=0.05) #instantiate Prophet
model.add_seasonality(name='monthly', period=30.5, fourier_order=5)
model.fit(sales_df); #fit the model with your dataframe
future = model.make_future_dataframe(periods=365, freq = 'd')
forecast = model.predict(future)

merge = pd.merge(forecast,sales_df, on='ds',how='left')

print merge


filename="test.csv"
merge.to_csv(filename, sep=',')

trace1 = go.Scatter(x=sales_df['ds'], y=sales_df['y'], name='y')
trace2 = go.Scatter(x=forecast['ds'], y=forecast['yhat'], name='yhat')
trace3 = go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], fill='tonexty', mode='none', name='upper')
trace4 = go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], fill='tonexty', mode='none', name='lower')
trace5 = go.Scatter(x=forecast['ds'], y=forecast['trend'], name='Trend')

data = [trace1,trace2,trace3,trace4,trace5]
py.plot(data, filename='pandas-time-weekly-series')