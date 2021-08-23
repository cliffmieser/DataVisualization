#Sitka_DeathValley.py

import csv
from datetime import datetime

import matplotlib.pyplot as plt


"""
filename = 'SanFran_weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
"""



def get_weather_data(filename, dates, highs, lows, date_index, high_index,low_index):
    '''Get highs and lows from a data file'''
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        #get dates and high and low temps from this file. 
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
                
#Getting Sitka data
filename = 'sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows, date_index=2, high_index = 5, low_index=6)
        

#plot Sitka data
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c = 'blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

#SanFrancisco data
filename = 'SanFran_weather.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows, date_index = 2, high_index=7, low_index=8)

#adding SF to plot
ax.plot(dates, highs, c='yellow', alpha=0.3)
ax.plot(dates, lows, c = 'green', alpha=0.3)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

#format plot
title = "Daily high and low temperatues - 2018"
title += "\nSitka, AK and San Francisco"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis='both', which='major', labelsize =16)
plt.ylim(10, 130)


plt.show()


