#Sitka_rainfall.py


import csv
from datetime import datetime
import matplotlib.pyplot as plt

"""
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
"""

filename  = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #get dates and high temps from this file. 
    dates, prec = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rain = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            prec.append(rain)

        

#plot the amount of precipitation
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prec, c='green', alpha=0.5)
#ax.fill_between(dates, prec, facecolor='blue', alpha=0.1)

#format plot
title = "Daily amount of pecipitation\nSitka 2018"
ax.set_title(title, fontsize = 20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show() 
