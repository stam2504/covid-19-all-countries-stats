import pandas as pd 
import matplotlib as plt
complete_df=pd.read_csv('https://covid.ourworldindata.org/data/ecdc/full_data.csv')
complete_df.iloc[[0,1250,9500,9501,20500]]
today=complete_df[complete_df['date']=='2020-06-04']
today_more_than_100k=today[today['total_cases'] >= 100000]
today_more_than_100k.plot.barh(x='location',y='total_cases', figsize=(10,6))
today_more_than_100k.plot.area(x='location',y='total_deaths',figsize=(10,6))
today_more_than_100k.plot.bar(x='location',y='new_cases',figsize=(10,5))
today_more_than_100k.plot.line(x='location',y='new_deaths',figsize=(10,6))
today_more_than_100k.sort_values('total_cases',ascending=False)
today_more_than_100k[['location','total_cases','new_cases','total_deaths','new_deaths']]
ds=today_more_than_100k[['location','total_cases','new_cases','total_deaths','new_deaths']]
ds.style.hide_index()