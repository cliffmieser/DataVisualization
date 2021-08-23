#Weather data from 2015-2021
#WeatherData.py

import csv
from datetime import datetime

import matplotlib.pyplot as plt


### Below is for showing column headers and it's index
"""
filename = 'WPBAirportData.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
"""
       

filename = 'WPBAirportData.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #get dates and high temps from this file. 
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[7])
            low = int(row[8])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
       

        

#plot the low and high temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c = 'blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#format plot
ax.set_title("Temperature highs and lows from 2015 - 2021", fontsize = 24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temerature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()



