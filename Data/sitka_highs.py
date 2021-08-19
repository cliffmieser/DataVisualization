#sitka_highs.py

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '/home/pi/PythonCrashCourse/GeneratingData/Data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #get dates and high temps from this file. 
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

        

#plot the high temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#format plot
ax.set_title("Daily high temperatures", fontsize = 24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temerature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
