# -*- coding: utf-8 -*-
import pandas as pd
#import datetime
#dataset=pd.read_excel("NIFTY25JUN2010000PE (3).xlsx"), parse_dates=[ 'Time'])
data = pd.read_excel("NIFTY25JUN2010000PE (3).xlsx")
data.set_index("Time",inplace=True)

print(data.head(500))


data.index = pd.to_timedelta(data.index.astype(str))
dataset=data.resample('3T').sum()

dataset=dataset.reset_index()
print(dataset.head(150))
writer = pd.ExcelWriter('Output.xlsx', engine='xlsxwriter',datetime_format='hh:mm:ss.000')

dataset.to_excel(writer,sheet_name='Sheet1')
writer.save()
writer.close()

"""data = pd.read_excel("NIFTY25JUN2010000PE (3).xlsx")


print(data.head())


data["Time"] = pd.to_timedelta(data.astype(str))
dataset=data.resample('3T').mean()
print(data.head())"""